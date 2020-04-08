# from sys import exit
# # Using Dictionary (dict)
# people = {
#     "EMMA": "617-555-0100",
#     "RODRIGO": "617-555-0101",
#     "BRIAN": "617-555-0102",
#     "DAVID": "617-555-0103"
# }
#
# if "EMMA" in people:
#     print(f"Found {people['EMMA']}")
#     exit(0)
# print("Not found")
# exit(1)


# Creating a phonebook

# import csv

# file = open("phonebook.csv", "a")  # this a means "append"
#
# name = input("Name: ")
# number = input("Number: ")
#
# writer = csv.writer(file)
# writer.writerow((name, number))
#
# file.close()

# Other way
# import csv
#
# name = input("Name: ")
# number = input("Number: ")
#
# with open("phonebook.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow((name, number))
