import hashlib
import requests
import sys

args_list = sys.argv[1:]


def pwnedpassword_requests(first_5_hash_code):	
	try:
		res = requests.get(f'https://api.pwnedpasswords.com/range/{first_5_hash_code}')	
		return res
	except NameError as name_error:
		print('Naming Error')
		raise name_error

def password_check(password):
	hash_code = hashlib.sha1(str(password).encode()) 
	first_5_hash_code = hash_code.hexdigest().upper()[0:5]
	res = pwnedpassword_requests(first_5_hash_code)
	if res.status_code == 200:
		list_of_passwords = res.text.splitlines()
		for i in list_of_passwords:
			first,tail = i.split(':')
			if first == hash_code.hexdigest().upper()[5:]:
				print(f'The password {password} is hacked.... {tail} times\n')
				break
		else:
			print(f'This password {password} is a great password... Just carry on\n')
	elif res.status_code == 400:
		print('Sorry the hash code is not generated\n')

# Main Function:-
def main(args_list):
	for password in args_list:
		password_check(password)

if __name__ == '__main__':
  	main(args_list)
