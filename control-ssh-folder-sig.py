#!/usr/bin/python3
#coding: utf-8

import json
from os import system
import gzip
import base64
import hashlib

class FileSigControl(object):
    def __init__(self):
        self.tmp_file = "/tmp/control-ssh-folder.lst"
        self.storage_sig_versions = "~/.sig_files_control/"

    def made_checksums_tmp_file(self):
        with open(self.tmp_file, 'rb') as f1:
            H_ = hashlib.sha3_512()
            H_.update(f1.read())
            self.tmp_hexdigest = H_.hexdigest()
            f1.close()

    def made_checksums_all_files(self):
        with open(self.tmp_file, 'rb') as f2:
            self.files_hashed_lst = []
            for it in f2.read().decode().split("\n"):
                H_ = hashlib.sha3_512()
                H_.update(it.encode())
                self.files_hashed_lst.append(H_.hexdigest())
            f2.close()

    
                

