
all:
	APT_CONFIG=$$PWD/src/repository/apt.conf snapcraft prime
	# set Linux capabilities used by loolwsd and repack snap package
	# using mksquashfs to avoid of mksquashfs option "-no-xattrs" used by snapcraft
	sudo setcap cap_fowner,cap_mknod,cap_sys_chroot=ep prime/usr/bin/loolforkit
	sudo setcap cap_sys_admin=ep prime/usr/bin/loolmount
	mksquashfs prime loolwsd_2.0.3_amd64.snap -noappend -comp xz -all-root

install:
	sudo snap install --classic *.snap --dangerous

clean:
	snapcraft clean
