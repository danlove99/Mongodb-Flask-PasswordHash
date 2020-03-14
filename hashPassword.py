import bcrypt

def hashPassword(psw):
	password = bytes(psw, 'utf8')
	hashed = bcrypt.hashpw(password, bcrypt.gensalt())
	return hashed