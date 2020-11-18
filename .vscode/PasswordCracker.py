# There are currently bugs with this current file

import hashlib

flag = 0

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