import re

with open('rawfile.txt', 'r') as f:
    for lines in f:
        pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_address = re.findall(pattern, lines)
        print(ip_address)
        with open("redawrite.txt", "a") as fw:
            for items in ip_address:
                fw.writelines("%s\n" % items)
                print("%s\n" % items)
