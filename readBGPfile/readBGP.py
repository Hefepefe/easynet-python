#!/usr/bin/env python
"""
Print both local AS number and the BGP peer IP address to the screen from a saved BGP text file
 """

#Makes this text compatible with legacy python versions
from __future__ import print_function, unicode_literals

#Opens a BGP text file and reads it
with open('show_ip_bgp_summ.txt', 'r') as file:
    bgp_output = file.read()
    lines = bgp_output.splitlines()

# obtaining the local AS number and the the BGP peer IP address
as_local = lines[0].split(",")
as_number = as_local[1].split(" ")
bgp_peer_ip = lines[-1].split(" ")

print("The local AS number is:", as_number[4] + "\nThe BGP peer IP address is:", bgp_peer_ip[0])
#Closes the BGP text file
file.close()
