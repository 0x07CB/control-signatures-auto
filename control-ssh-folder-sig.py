#!/usr/bin/python3
#coding: utf-8

import json
from os import system
import gzip
import base64
import hashlib
from multiprocessing import Process


def process_notify():
    pass

def process_sound_alert():
    pass

def process_espeak_alert():
    pass



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
    
    def check_circuit(self):
        self.made_checksums_tmp_files()
        self.made_checksums_all_files()
        return self

    def getter_dict_json_output_data(self):
        self.construct_json_data()
        return self.dict_json_data

    def construct_json_data(self):
        self.dict_json_data = {}
        pass

    def write_json_data(self):
        pass

    def read_json_data(self):
        pass

    def compare_version(self):
        pass

    def notify_alert(self):
        pass

    def control_processus(self):
        return None

    
                
Fsigctrl = FileSigControl()
# =====
Result_of_detection = Fsigctrl.check_circuit().control_processus()

exit(0)
