#!/bin/sh
diskutil unmount force ~/mounts/vagrant
sshfs -C -p 2222 vagrant@localhost:/ ~/mounts/vagrant
