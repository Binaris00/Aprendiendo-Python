import re
"""
1-Write a regular expression to match email addresses in a given string.
2-Write a regular expression to match phone numbers in a given string.
3-Write a regular expression to match dates in the format of "MM/DD/YYYY" in a given string.
4-Write a regular expression to match URLs in a given string.
5-Write a regular expression to match IP addresses in a given string.
6-Write a regular expression to match hexadecimal color codes in a given string.
7-Write a regular expression to match social security numbers in the format of "XXX-XX-XXXX" in a given string.
8-Write a regular expression to match credit card numbers in a given string.
9-Write a regular expression to match HTML tags in a given string.
10-Write a regular expression to match words that start with a capital letter in a given string.
"""
#1 (In other situations I can use a loop with a list but in this case I only use re.search)
email = "pythonlover@gmail.com"
emails_to_find = "@gmail.com"
email_finded = re.search(emails_to_find, email)

#2 
phone = "809-532-4893"
secret_number_pattern =  r"\d{3}-\d{3}-\d{3}"
phone_finded = re.search(secret_number_pattern, phone)

#3
date = "2/12/2000"
date_finder = r"(0?[1-9]|1[0-2])/(0?[1-31])/\d{4}"
date_finded = re.search(date_finder, date)
print(date_finded)
