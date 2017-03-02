
all:
	APT_CONFIG=$$PWD/src/repository/apt.conf snapcraft

install:
	sudo snap install loolwsd_2.0.4_amd64.snap --devmode

clean:
	snapcraft clean
