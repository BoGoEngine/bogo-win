#!/bin/bash


function build_and_run() {
	if [ -e dist/bogo.dll ]
	then
		regsvr32 //u dist/bogo.dll
	fi

	python2 setup.py py2exe &&
	regsvr32 dist/bogo.dll
}

function build_dist() {
	DIST="bogo-`git describe --tags`"
	python2 setup.py py2exe -d $DIST
	cp README.dist $DIST/README.txt
	7z a "$DIST.zip" $DIST
	rm -r $DIST
}


case "$1" in
	"run")
	build_and_run
	;;
	"dist")
	build_dist
	;;
esac
