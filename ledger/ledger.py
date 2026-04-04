#!/usr/bin/env python3.12

"""
Filename:		hashpw.py
Date:			2026.03.31
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

import datetime as dt


class Transaction():
	pass


class Account():
	pass


class Book():
	def __init__(self):
		self.book_name = ""
		self.creation_date = None
		self.fy_start_date = None
		self.today = None
		self.number_of_accounts = 0
		self.accounts = []
		self.owner = ""

	def set_name(self, book_name: str) -> None:
		self.book_name = book_name

	def set_creation_date(self) -> None:
		self.creation_date = dt.datetime.today()

	def set_fy_year_start_date(self, fy_start_date: list[int, int, int]) -> None:
		self.fy_start_date = dt.date(fy_start_date)  

	def set_today(self) -> None:
		self.today = dt.datetime.today()

	def set_number_of_accounts(self) -> None:
		self.number_of_accounts += 1

	def set_account_names(self, account_names: list) -> None:
		for x in range(len(self.number_of_accounts)):
			self.accounts[x](account_names[x])


if __name__ == "__main__":
	print(dt.date(2026, 4, 1))


