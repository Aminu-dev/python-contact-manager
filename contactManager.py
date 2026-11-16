import csv

search_for_user = input("Do you want to search for a user?\n 1. Yes\n 2. No ")

with open("data3_test.csv") as csv_data:
    contact_data = list(csv.DictReader(csv_data, delimiter="\t"))


def search_users(contacts, field, search_value):
    found = False

    for user in contacts:
        if search_value.lower() == user[field].lower():
            print(f"{user['first_name']}, {user['last_name']}, {user['email']}")
            found = True

    return found


while search_for_user == "1":
    choice = input(
        "1. Search by firstname\n"
        "2. Search by lastname\n"
        "3. Search by email address\n"
        "4. Show all Contacts "
    )

    found = False

    while choice not in ("1", "2", "3", "4"):
        print("Try again!")
        choice = input(
            "Please select a choice:\n"
            "1. Search by firstname\n"
            "2. Search by lastname\n"
            "3. Search by email address\n"
            "4. Show all Contacts  "
        )

    if choice == "1":
        first_name = input("What is the user's first name? ")

        found = search_users(contact_data, "first_name", first_name)

    elif choice == "2":
        last_name = input("What is the user's last name? ")

        found = search_users(contact_data, "last_name", last_name)

    elif choice == "3":
        email = input("What is the user's email? ")

        found = search_users(contact_data, "email", email)

    elif choice == "4":
        for user in contact_data:
            print(f"{user['first_name']}, {user['last_name']}, {user['email']}")

    if choice in ("1", "2", "3") and not found:
        print("User not found")

    search_for_user = input("Search again? 1. Yes\n 2. No \n")

if search_for_user == "2":
    print("Thank you !")
