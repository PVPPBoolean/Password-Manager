Modules:
	subprocess
	cryptography
	hashlib
	sqlite3
	tkinter

Flow:
->Application password and email should be present in Database, if not present ask user to make a password[for first time only] no concept of multiple users
	->Application password is hashed and stored in database
	->If application password is forgotten otp on email (or any other method)
->Main Window
	->New Password
		->Input website name
		->Input website's username
		->Input website's password or let user auto-generate strong password
		->Encrypt website's password and store everything in database

	->Retrieve Password
		->Input website's name or website's username
		->Check in database according to what is given (using "like" clause in sqlite3)
			->If exists decrypt and show it to user and copy to clipboard feature
			->If not idk

->Optional window
		->Show all website name and their password(encrypted) (in treeview or something like in ATTM)

->As always good'ol social frame
