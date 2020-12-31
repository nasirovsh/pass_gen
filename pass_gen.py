import string
import secrets

def gen_password(has_letters=True, has_digits=True, length=8):
	if not has_letters and not has_digits:
		print("Should have letters or/and digits!!!")
		return ""
	alpha_num = ""
	password = ""
	if has_letters:
		alpha_num +=string.ascii_letters
	if has_digits:
		alpha_num +=string.digits
	password = ''.join(secrets.choice(alpha_num) for i in range(length))
	return password

def gen_password_alpha_num(length=8):
	alpha_num = string.ascii_letters + string.digits	
	while True:
		password = ''.join(secrets.choice(alpha_num) for i in range(length))
		if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 3):
        		break
	return password

if __name__ == "__main__":
	password = gen_password()
	print(password)
	
	password = gen_password_alpha_num()
	print(password)
