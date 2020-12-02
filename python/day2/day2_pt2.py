passwords = []
valid_passwords = 0


with open('input.txt') as f:
	for line in f:
		passwords.append(line.strip())

for password in passwords:
	context = password.split()
	
	character = context[1].replace(':', '')
	plain_password = context[2]
	positions = context[0].split('-')
	splitted_pass = list(plain_password)
	
	verification = []
	if splitted_pass[int(positions[0]) -1] == character:
		verification.append(True)
	if splitted_pass[int(positions[1]) -1] == character:
		verification.append(True)
	
	if verification.count(True) == 1:
		print('{} is valid'.format(password))
		valid_passwords += 1
	else:
		print('{} is not valid'.format(password))

print(valid_passwords)


