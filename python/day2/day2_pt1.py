passwords = []
valid_passwords = 0


with open('input.txt') as f:
	for line in f:
		passwords.append(line.strip())

for password in passwords:
	context = password.split()
	
	character = context[1].replace(':', '')
	ocurrence_limit = context[0].split('-')
	plain_password = context[2]
	

	ocurrence_range = list(range(int(ocurrence_limit[0]), int(ocurrence_limit[1]) + 1))
	actual_ocurrence = plain_password.count(character)
	
	if actual_ocurrence in ocurrence_range:
		print('{} is valid'.format(password))
		valid_passwords += 1
	else:
		print('{} is not valid'.format(password))
	

print(valid_passwords)
