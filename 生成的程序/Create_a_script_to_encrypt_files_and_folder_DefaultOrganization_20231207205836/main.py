'''
This script allows users to encrypt files and/or folders using the AES encryption algorithm.
'''
import os
import sys
from Crypto.Cipher import AES
from Crypto.Util import Padding
KEY = b'this is a 16 key'
BLOCK_SIZE = 16
def encrypt_file(file_path):
    '''
    Encrypts a file using AES encryption algorithm.
    '''
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            plaintext = file.read()
        cipher = AES.new(KEY, AES.MODE_ECB)
        padded_plaintext = Padding.pad(plaintext, BLOCK_SIZE)
        ciphertext = cipher.encrypt(padded_plaintext)
        encrypted_file_path = file_path + '.bin'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(ciphertext)
        print(f'File encrypted: {encrypted_file_path}')
    else:
        print('Invalid file path')
def encrypt_folder(folder_path):
    '''
    Encrypts all files and subfolders in a folder recursively.
    '''
    if os.path.isdir(folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path)
    else:
        print('Invalid folder path')
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python encrypt.py <file/folder path>')
    else:
        path = sys.argv[1]
        if os.path.isfile(path):
            encrypt_file(path)
        elif os.path.isdir(path):
            encrypt_folder(path)
        else:
            print('Invalid path')