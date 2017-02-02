## Build requirements

Up-to-date snapd and snapcraft packages (snapd 2.20 with the required "classic" snap confinement feature was released on 2017-01-05):

    sudo apt-get install snapd snapcraft
    sudo snap install core

## Build steps

You can set APT_CONFIG as env var or use it every time you want to build

    APT_CONFIG=$PWD/apt.conf snapcraft

## Installation

    sudo snap install loolwsd_2.0.1_amd64.snap --classic --dangerous

## Test installed Collabora Online

Open http://127.0.0.1:9980

## Remove snap

    sudo snap remove loolwsd

## Rebuild snap from scratch

    snapcraft clean && APT_CONFIG=$PWD/apt.conf snapcraft

