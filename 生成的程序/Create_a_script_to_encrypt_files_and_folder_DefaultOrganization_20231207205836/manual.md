# File Encryption with AES Algorithm - User Manual

## Introduction

The File Encryption program allows users to encrypt files and/or folders using the AES encryption algorithm. This manual provides detailed instructions on how to install the required dependencies and how to use the program effectively.

## Table of Contents

1. Installation
2. Usage
   - Encrypting a File
   - Encrypting a Folder
3. Key Management
4. Skipping Special Files
5. Conclusion

## 1. Installation

Before using the File Encryption program, you need to install the Pycryptodome library. Follow the steps below to install the library:

1. Open the terminal.
2. Run the following command:

   ```bash
   pip install pycryptodome
   ```

   This command will install the required library.

## 2. Usage

To encrypt files and folders, you can use the `encrypt.py` script provided. Follow the instructions below to encrypt your files and folders.

### 2.1 Encrypting a File

To encrypt a file, follow these steps:

1. Open the terminal.
2. Navigate to the location of the `encrypt.py` file.
3. Run the following command, replacing `filepath` with the path of the file to be encrypted:

   ```bash
   python encrypt.py filepath
   ```

   For example, if you want to encrypt a file located at `/path/to/file.txt`, the command would be:

   ```bash
   python encrypt.py /path/to/file.txt
   ```

   The encrypted file will be saved with the same name as the original file, but with a `.bin` extension.

### 2.2 Encrypting a Folder

To encrypt a folder and all its files and subfolders recursively, follow these steps:

1. Open the terminal.
2. Navigate to the location of the `encrypt.py` file.
3. Run the following command, replacing `folderpath` with the path of the folder to be encrypted:

   ```bash
   python encrypt.py folderpath
   ```

   For example, if you want to encrypt a folder located at `/path/to/folder`, the command would be:

   ```bash
   python encrypt.py /path/to/folder
   ```

   All the files and subfolders in the folder will be encrypted, and the encrypted files will be saved with the same name as the original files, but with a `.bin` extension.

## 3. Key Management

The encryption key used in the `encrypt.py` script is hardcoded as `'this is a 16 key'`. For security reasons, it is recommended to enhance the key management by securely storing or generating keys.

To enhance key management, you can modify the `KEY` variable in the `encrypt.py` script to use a different key. Make sure to use a strong and secure key for encryption.

## 4. Skipping Special Files

The `encrypt.py` script will automatically detect and skip special files such as sockets, FIFOs, and device files during the encryption process. These files are not encrypted for security reasons.

## 5. Conclusion

The File Encryption program provides a convenient way to encrypt files and folders using the AES encryption algorithm. By following the installation instructions and using the provided `encrypt.py` script, you can easily encrypt your files and protect them from unauthorized access.

Remember to securely manage your encryption keys and be cautious when encrypting sensitive files.