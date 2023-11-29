
```markdown
# File and Folder Encryption Script

This Python script allows you to encrypt files and folders using the AES encryption algorithm. It uses the `Cryptodome` library to perform the encryption.

## Usage

To use the script, open your terminal and run the following command:

```bash
python encrypt.py path
```

Replace `path` with the file or folder you want to encrypt. The script will automatically determine if the provided path is a file or a folder.

### Examples

#### Encrypting a File

To encrypt a single file, use the script as follows:

```bash
python encrypt.py test.txt
```

This will generate an encrypted file with the name `test.txt.bin` in the same location as the original file.

#### Encrypting a Folder

To encrypt an entire folder and its contents, use the script like this:

```bash
python encrypt.py ./testdir
```

This will recursively encrypt all files within the `testdir` folder, preserving their original folder structure. Encrypted files will be generated with the `.bin` extension in their original locations.

Please note that the encryption key used in the script is hardcoded (`b'this is a 16 key'`). For security reasons, you may want to enhance the key management by securely storing or generating keys.

## Encrypted File Format

The script generates encrypted files with the same name as the original files but with a `.bin` extension. These encrypted files can only be decrypted using the appropriate decryption key and the script.

## Special Files

The script will detect and skip special files (e.g., sockets, FIFOs, device files) during the encryption process.

## Dependencies

The script relies on the `Cryptodome` library for encryption. You can install it using pip:

```bash
pip install pycryptodome
```

