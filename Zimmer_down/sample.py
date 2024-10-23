import re

# The binary string from the registry entry you found
binary_string = r"n%00o%00t%00t%00h%00e%00_%00f%00l%00a%00g%00.%00t%00x%00t%00%00%00n%002%00%00%00%00%00%00%00%00%00%00%00notthe_flag.lnk"

# Replace %00 with an empty string and decode the string
decoded_string = binary_string.replace('%00', '').encode('latin1').decode('utf-16')

# Use regex to extract potential flags
flags = re.findall(r'flag{[^}]*}', decoded_string)

if flags:
    for flag in flags:
        print("Found flag:", flag)
else:
    print("No flags found.")
