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

import hashlib, secrets, argparse
from getpass import getpass


def get_pw() -> str:
	pw1 = getpass(prompt="Enter new password: ")
	pw2 = getpass(prompt="Re-enter the password: ")

	if pw1==pw2:
		if validate_pw(pw1):
			del pw2
			return pw1
		else:
			del pw1, pw2
			return None
	else:
		del pw1, pw2
		return None


def validate_pw(password: str) -> bool:
	characters = (33, 126)
	if len(password) < 8:
		print("Password must be at least eight characters long.")
		return False

	for letter in password:
		if ord(letter) < characters[0] or ord(letter) > characters[1]:
			print("Password must contain only a-z, A-Z, 0-9, !@$%^&*()[]{}<>,.-_+=\\~|/?#.")
			return False

	return True


def hash_pw(password: str) -> str:
	salt = secrets.token_hex(16)
	password += salt
	hash_object = hashlib.sha3_512(password.encode())
	pwhash = hash_object.hexdigest()
	return salt, pwhash


def main():
	password = get_pw()

	if password == None:
		exit(0)

	hash_data = hash_pw(password)

	credfile = open("pwcred.txt", "w")
	credfile.write(f"{hash_data[0]},{hash_data[1]}")

	print("Done.\n")


if __name__ == "__main__":
	main()

