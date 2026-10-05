import csv

search_for_user = input("Do you want to search for a user?\n 1. Yes\n 2. No ")

while search_for_user == "1":

	with open('data3_test.csv') as csv_data:

		contact_data = csv.DictReader(csv_data, delimiter='\t')

		choice = input("1. Search by name\n2. Search by email\n3. Show all Contacts\n4. Search by Last name  ")

		found = False

		while choice not in ("1", "2", "3", "4"):

			print("Try again!")	
			choice = input("Please select a choice:\n1. Search by name\n2. Search by email\n3. Show all Contacts\n4. Search by Last name  ")

		if choice == "1":

			first_name = input("What is the user's first name? ")

			for user in contact_data:
				if first_name.lower() == user['first_name'].lower():
					print(f"{user['first_name']}, {user['last_name']}, {user['email']}")
					found = True

		elif choice == "2":

			email = input("What is the user's email? ")

			for user in contact_data:
				if email.lower() == user['email'].lower():
					print(f"{user['first_name']}, {user['last_name']}, {user['email']}")
					found = True

		elif choice == "3":

			for user in contact_data:
				print(f"{user['first_name']}, {user['last_name']}, {user['email']}")

		elif choice == "4":

			last_name = input("What is the user's last name ")

			for user in contact_data:
				if last_name.lower() == user["last_name"].lower():
					print(f"{user['first_name']}, {user['last_name']}, {user['email']}")
					found = True

		if  choice in ("1", "2", "4") and not found:
			print('User not found')	
					

		search_for_user = input("Search again? 1. Yes 2. No")

if search_for_user == "2":
	print("Thank you !")



