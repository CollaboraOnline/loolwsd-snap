## Build requirements

Up-to-date snapd and snapcraft packages (snapd 2.20 with the required "classic" snap confinement feature was released on 2017-01-05):

    sudo apt-get install snapd snapcraft
    sudo snap install core

## Build steps

You can set APT_CONFIG as env var or use it every time you want to build

    export APT_CONFIG=$PWD/src/repository/apt.conf
    snapcraft

or, easier, use the make command in project folder
    make

## Installation

    sudo snap install loolwsd_2.0.3_amd64.snap --classic --dangerous

## Test configuration

Once the snap is installed, check next values in $SNAP_DATA/etc/loolwsd/loolwsd.xml config file:

     <filesystem allow="true" />
     
     <ssl desc="SSL settings">
        <enable type="bool" default="true">false</enable>

in case you need to modify any value in that file, you need to restart the daemon by

     snap disable loolwsd && snap enable loolwsd

## Test installed Collabora Online

Once the snap is installed, open browser url:
    http://127.0.0.1:9980/loleaflet/dist/loleaflet.html?file_path=file:///<path>/<to>/<local>/<file>

where <path>/<to>/<local>/<file> is the absolute url of a local document to render (odt, docx...)

## Remove snap

    sudo snap remove loolwsd

## Rebuild snap from scratch

    make clean && make

