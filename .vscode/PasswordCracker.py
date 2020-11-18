# There are currently bugs with this current file

import hashlib

flag = 0

print("                            __                 ")
print("  ________________    ____ |  | __ ___________ ")
print("_/ ___\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \ """)
print("\  \___|  | \// __ \\  \___|  <  \  ___/|  | \/")
print(" \___  >__|  (____  /\___  >__|_ \\___  >__|   ")
print("     \/           \/     \/     \/    \/      ")

pass_hash = input("Enter a md5 hash: ")
wordlist = "D:\VenomshitGoBrrr\Passwords\passwords.txt"
pass_file = open(wordlist, "r")

for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(word.strip()).hexdigest()

    if digest == pass_hash:
        print("Password found")
        print("=====>" + word + "<=====")
        flag = 1
        break

if flag == 0:
    print("Password was not found in the list")