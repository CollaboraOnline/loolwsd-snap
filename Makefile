
all:
	APT_CONFIG=$$PWD/src/repository/apt.conf snapcraft

install:
	sudo snap install loolwsd_2.0.3_amd64.snap --dangerous

clean:
	snapcraft clean
