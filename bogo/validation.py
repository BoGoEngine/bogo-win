# -*- coding: utf-8 -*-
#
# This file is part of ibus-bogo project.
#
# Copyright (C) 2012 Long T. Dam <longdt90@gmail.com>
# Copyright (C) 2012-2013 Trung Ngo <ndtrung4419@gmail.com>
# Copyright (C) 2013 Duong H. Nguyen <cmpitg@gmail.com>
#
# ibus-bogo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ibus-bogo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ibus-bogo.  If not, see <http://www.gnu.org/licenses/>.
#

import collections
from . import accent
from . import mark
from . import utils
Accent = accent.Accent


# Auto-generated lists from dictionary

# FIXME:
# Think about words composed entirely of vowels, like 'yá'.
# Perhaps let the user customize these lists?

CONSONANTS = {
    'b', 'c', 'ch', 'd', 'g', 'gh', 'gi', 'h', 'k', 'kh', 'l', 'm', 'n', 'ng',
    'ngh', 'nh', 'p', 'ph', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x', u'đ'
}

TERMINAL_CONSONANTS = {
    'c', 'ch', 'm', 'n', 'ng', 'nh', 'p', 't'
}

VOWELS = {
    'a', 'ai', 'ao', 'au', 'ay', 'e', 'eo', 'i', 'ia', 'iu', u'iê', u'iêu',
    'o', 'oa', 'oai', 'oao', 'oay', 'oe', 'oeo', 'oi', 'oo', u'oă', 'u', 'ua',
    'ui', 'uy', 'uya', 'uyu', u'uyê', u'uâ', u'uây', u'uê', u'uô', u'uôi',
    u'uơ', 'y', u'yê', u'yêu', u'â', u'âu', u'ây', u'ê', u'êu', u'ô', u'ôi',
    u'ă', u'ơ', u'ơi', u'ư', u'ưa', u'ưi', u'ưu', u'ươ', u'ươi', u'ươu'
}

TERMINAL_VOWELS = {
    'ai', 'ao', 'au', 'ay', 'eo', 'ia', 'iu', u'iêu', 'oai', 'oao', 'oay',
    'oeo', 'oi', 'ua', 'ui', 'uya', 'uyu', u'uây', u'uôi', u'uơ', u'yêu', u'âu',
    u'ây', u'êu', u'ôi', u'ơi', u'ưa', u'ưi', u'ưu', u'ươi', u'ươu'
}

STRIPPED_VOWELS = set(map(mark.strip, VOWELS))

# 'uo' may clash with 'ươ' and prevent typing 'thương'
# 'ua' may clash with 'uâ' and prevent typing 'luật'
STRIPPED_TERMINAL_VOWELS = set(map(mark.strip, TERMINAL_VOWELS)) - {'uo', 'ua'}


SoundTuple = \
    collections.namedtuple('SoundTuple',
                           ['first_consonant', 'vowel', 'last_consonant'])


def is_valid_string(string, final_form=True):
    return is_valid_combination(utils.separate(string), final_form)


def is_valid_combination(comp, final_form=True):
    return is_valid_sound_tuple(comp, final_form)


def is_valid_sound_tuple(sound_tuple, final_form=True):
    """
    Check if a character combination complies to Vietnamese phonology.
    The basic idea is that if one can pronunce a sound_tuple then it's valid.
    Sound tuples containing consonants exclusively (almost always
    abbreviations) are also valid.

    Input:
        sound_tuple - a SoundTuple
        final_form  - whether the tuple represents a complete word
    Output:
        True if the tuple seems to be Vietnamese, False otherwise.
    """

    # We only work with lower case
    sound_tuple = SoundTuple._make([s.lower() for s in sound_tuple])

    # Words with no vowel are always valid
    # FIXME: This looks like it should be toggled by a config key.
    if not sound_tuple.vowel:
        result = True
    elif final_form:
        result = \
            has_valid_consonants(sound_tuple) and \
            has_valid_vowel(sound_tuple) and \
            has_valid_accent(sound_tuple)
    else:
        result = \
            has_valid_consonants(sound_tuple) and \
            has_valid_vowel_non_final(sound_tuple)

    return result


def has_valid_consonants(sound_tuple):

    def has_invalid_first_consonant():
        return (sound_tuple.first_consonant != "" and
                not sound_tuple.first_consonant in CONSONANTS)

    def has_invalid_last_consonant():
        return (sound_tuple.last_consonant != "" and
                not sound_tuple.last_consonant in TERMINAL_CONSONANTS)

    return not (has_invalid_first_consonant() or
                has_invalid_last_consonant())


def has_valid_vowel_non_final(sound_tuple):
    # If the sound_tuple is not complete, we only care whether its vowel
    # position can be transformed into a legit vowel.

    stripped_vowel = mark.strip(sound_tuple.vowel)
    if sound_tuple.last_consonant != '':
        return stripped_vowel in STRIPPED_VOWELS - STRIPPED_TERMINAL_VOWELS
    else:
        return stripped_vowel in STRIPPED_VOWELS


def has_valid_vowel(sound_tuple):
    # Check our vowel.
    # First remove all accents
    vowel_wo_accent = accent.remove_accent_string(sound_tuple.vowel)

    def has_valid_vowel_form():
        return vowel_wo_accent in VOWELS and not \
            (sound_tuple.last_consonant != '' and
                vowel_wo_accent in TERMINAL_VOWELS)

    def has_valid_ch_ending():
        # 'ch' can only go after a, ê, uê, i, uy, oa
        return not (sound_tuple.last_consonant == 'ch' and
                    not vowel_wo_accent in {'a', u'ê', u'uê', 'i', 'uy', 'oa'})

    def has_valid_c_ending():
        # 'c' can't go after 'i' or 'ơ'
        return not (sound_tuple.last_consonant == 'c' and
                    vowel_wo_accent in {'i', u'ơ'})

    def has_valid_ng_ending():
        # 'ng' can't go after i, ơ
        return not (sound_tuple.last_consonant == 'ng' and
                    vowel_wo_accent in {'i', u'ơ'})

    def has_valid_nh_ending():
        # 'nh' can only go after a, ê, uy, i, oa, quy
        has_y_but_is_not_quynh = vowel_wo_accent == 'y' and \
            sound_tuple.first_consonant != 'qu'

        has_invalid_vowel = not vowel_wo_accent in \
            {'a', u'ê', 'i', 'uy', 'oa', u'uê', 'y'}

        return not \
            (sound_tuple.last_consonant == 'nh' and
                (has_invalid_vowel or has_y_but_is_not_quynh))

    # The ng and nh rules are not really phonetic but spelling rules.
    # Including them may hinder typing freedom and may prevent typing
    # unique local names.
    # FIXME: Config key, anyone?
    return \
        has_valid_vowel_form() and \
        has_valid_ch_ending() and \
        has_valid_c_ending()
        # has_valid_ng_ending() and \
        # has_valid_nh_ending()


def has_valid_accent(sound_tuple):
    akzent = accent.get_accent_string(sound_tuple.vowel)

    # These consonants can only go with ACUTE, DOT accents
    return not (sound_tuple.last_consonant in {'c', 'p', 't', 'ch'} and
                not akzent in {Accent.ACUTE, Accent.DOT})
