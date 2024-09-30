# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:34:07 2024

@author: TIPQC
"""

from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        with open(filepath, 'r') as read_file:
            print('\nThis is now the current data in the .txt file\n',read_file.read(),'\n')
            read_file.close()
            
    def write(self, filepath, data):
        with open(filepath, 'w') as write_file:
            write_file.write(data)
            print('\nThe new contents of the .txt file will be : \n',data,'\n')
            return data