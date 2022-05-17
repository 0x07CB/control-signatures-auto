#!/bin/bash
ls -1 /home/$USER/.ssh/ > /tmp/control-ssh-folder.lst && python3 /opt/control-signature-auto/control-ssh-folder-sig.py < /tmp/control-ssh-folder.lst && rm -f /tmp/control-ssh-folder.lst
