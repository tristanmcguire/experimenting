#!/usr/bin/env python3.12

"""
Filename:		hashpw.py
Date:			2026.03.28
Author:			Tristan McGuire
Description:	Testing hshlib functionality and a simple password hashing process.
License: 		Copyright 2026 Tristan McGuire

				Redistribution and use in source and binary forms, with or without modification, are permitted 
				provided that the following conditions are met:

					1. Redistributions of source code must retain the above copyright notice, this list of conditions 
					   and the following disclaimer.

					2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions 
					   and the following disclaimer in the documentation and/or other materials provided with the distribution.

					3. Neither the name of the copyright holder nor the names of its contributors may be used to 
					   endorse or promote products derived from this software without specific prior written permission.

				THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED 
				WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
				PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR 
				ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED 
				TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
				HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
				NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
				OF SUCH DAMAGE.
"""

import hashlib, secrets, argparse, string
from getpass import getpass
from cryptography.fernet import Fernet


def get_pw() -> str:
	pw1 = getpass(prompt="Enter new password: ")
	pw2 = getpass(prompt="Re-enter the password: ")

	if validate_input(pw1, pw2):
		return pw1
	else:
		return None


def validate_input(pw: str, pw2: str) -> bool:
	characters = (33, 126)
	if len(pw) < 8:
		print("Password must be at least eight characters long.\n")
		return False

	for letter in pw:
		if ord(letter) < characters[0] or ord(letter) > characters[1]:
			print(f"Password must contain only 'a' through 'z', 'A' through 'Z', '0' through '9', and/or '{string.punctuation}'.\n")
			return False

	if pw != pw2:
		print("Passwords do not match.\n")
		return False

	print("\n")
	return True


def hash_pw(password: str) -> str:
	salt = secrets.token_hex(16)
	password += salt
	hash_object = hashlib.sha3_512(password.encode())
	pwhash = hash_object.hexdigest()

	return salt, pwhash


def encrypt_credentials(clear_text: str):
	key = Fernet.generate_key()
	keyfile = open("./key", "w")
	keyfile.write(key.decode('ascii'))

	encrypted_text = Fernet(key).encrypt(clear_text.encode()).decode('ascii')
	credentials = open("credentials", "w")
	credentials.write(encrypted_text)


def read_credentials() -> list:
	data = ["", "", ""]

	key_file = open("./key", "r")
	data[0] = key_file.read()

	credentials_file = open("./credentials", 'r')
	data[1] = credentials_file.read()

	return data


def decrypt_credentials(key, encrypted_data: str) -> list:
	f = Fernet(key)
	hashed_password = f.decrypt(encrypted_data.encode()).decode("ascii")

	return hashed_password


def validate_credentials(salt: str, hashpw: str) -> bool:
	password = getpass(prompt = "Enter your password: ")
	password += salt
	hash_object = hashlib.sha3_512(password.encode()).hexdigest()

	print(f"Entered credentials: {hash_object}, Saved credentials: {hashpw}")

	if hash_object == hashpw: 
		return True
	else:
		return False



def main():
	# Get user input password
	password = get_pw()

	if password == None:
		exit(0)

	# Hash, encrypt, and store the password in a credentials file
	hash_data = hash_pw(password)  
	encrypted_data = encrypt_credentials(f"{hash_data[0]},{hash_data[1]}")

	# Decrypt password from credentials file
	encrypted_credentials = read_credentials()
	key = encrypted_credentials[0]
	password = decrypt_credentials(key, encrypted_credentials[1]).split(',')

	# Validate password
	if validate_credentials(password[0], password[1]):
		print("Success!")
	else: 
		print("Fail!!")

	print("Done.\n")


if __name__ == "__main__":
	main()

