country = input('which country: ')
age = input('age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('you can take the driving test')
	else:
		print('not yet for the driving test')
elif country == 'USA':
	if age >= 16:
		print('you can take the driving test')
	else:
		print('not yet for the driving test')



