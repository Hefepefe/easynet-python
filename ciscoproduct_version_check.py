"""
Checks if the product version contains "881" and "Cisco and prints out the 
serial version and model. 
"""

show_version = "*0        CISCO881-SEC-K9       FTX0000038X "

show_version = show_version.split()
model = show_version[1]
serial_number=show_version[2]

print("The model is:", model,  "The serial number is:", serial_number)

if "CISCO" and "881" in model:
    print("The model:", model, "contains Cisco and 881")
else:
    print("The model:", model, "does not contain Cisco and 881")
    print(model)
