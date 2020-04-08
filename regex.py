# Regular Expressions ###############

# (.) - any character
# (.*) - 0 or more characters
# (.+) - 1 or more characters

# (?) - optional
# (^) - start of input
# ($) - end of input

# Example
# import re
#
# s = input("Do you agree?\n")
#
# if re.search("^y(es)?$", s, re.IGNORECASE):
#     print("Agreed.")
# elif re.search("^n(o)|(ope)?$", s, re.IGNORECASE):
#     print("Not agreed.")

# Validating 10 digits phone number that start with 7,8 0r 9
# import re
#
#
# for i in range(int(input())):
#     n = input()
#     if re.match(r"^(7|8|9)\d{9}$", n):  # or (r"^[789]\d{9}$", n)
#         print("YES")
#     else:
#         print("NO")


# Print the space-separated name and email address pairs containing valid email addresses only.
# Each pair must be printed on a new line in the following format:

# Sample input:

# 2
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>

# import re, email.utils
#
# for i in range(int(input())):
#     s = email.utils.parseaddr(input())
#     if re.match(r"^[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$", s[1]):
#         print (email.utils.formataddr(s))


# Other way

# import re
# n = int(input())
# for _ in range(n):
#     x, y = input().split(' ')
#     m = re.match(r'<[A-Za-z][\w-._]+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
#     if m:
#         print(x,y)