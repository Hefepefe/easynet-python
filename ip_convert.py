#!/usr/bin/python3
"""
Prints out a prompted IP address in decimal, binary, and hex formatted in a table.
"""

from tabulate import tabulate
from__future__ import print_function, unicode_literals

ip_address = input("Please Enter Your IP Address Separated With a Decimal(.):")
#Prompts a user to input an IP address

decimal_address=ip_address.split(".")
#Breaks the IP address into octets

results = []
for number in decimal_address:
    decimal_number=results.append(number)
    binary_number=results.append(bin(int(number)))
    hexadecimal_number=results.append(hex(int(number)))
#Puts the IP address into decimal, binary and hexadecimal

table = [["Octet1",results[0],results[1],results[2]],
["Octet2",results[3],results[4],results[5]],
["Octet3",results[6],results[7],results[8]],
["Octet4",results[9],results[10],results[11]]]
#Inputs the values into a table

print(tabulate(table, headers=["Octet","Decimal", "Binary", "Hexadecimal"], tablefmt="pretty"))
