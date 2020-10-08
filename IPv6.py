"""
Create three different variables the first variable should use all
lower case characters with underscore ( _ ) as the word separator.
The second variable should use all upper case characters with underscore as the word separator.
The third variable should use numbers, letters, and underscore, but still be a valid variable
Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
"""

string_1 = "2001:0db8:0001:0000:0000:0ab9:C0A8:0102"
STRING_2 ="684D:1111:222:3333:4444:5555:6:77"
str1ng_ONE ="2001:0db8:0001:0000:0000:0ab9:C0A8:0102"

if (string_1 == STRING_2) and (string_1 != str1ng_ONE):
    print(True)
else:
    print(False)
