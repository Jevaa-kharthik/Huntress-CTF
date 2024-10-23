import re

# The binary string from the registry entry you found
binary_string = r"H%00o%00w%00 %00t%00o%00 %00f%00i%00n%00d%00 %00f%00l%00a%00g%00s%00.%00m%00p%004%00%00%00%8C%002%00%00%00%00%00%00%00%00%00%00%00How to find flags.mp4.lnk"

# Replace %00 with an empty string and decode the string
decoded_string = binary_string.replace('%00', '').encode('latin1').decode('utf-16')

# Extract the path from the decoded string
match = re.search(r'(.+\.mp4\.lnk)', decoded_string)
if match:
    mp4_link = match.group(1)
    print("Found MP4 link:", mp4_link)
else:
    print("No MP4 link found.")
