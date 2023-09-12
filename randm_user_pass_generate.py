import random
from datetime import datetime

def username(b, n):
    key = datetime.now()
    for u in range(b):
        l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
        str2 = ""
        str1 = ''
        w = ['@', '#', '$', '*', '!','&','%']
        e = random.randint(0, 100)
        for i in range(n + 1):
            index = random.randint(0, 25)
            str2 = str2 + l[index]
        for y in range(3):
            index2 = random.randint(0, 25)
            index3 = random.randint(0, 25)
            # password pattern first-letter upperCase second LowerCase number and symebols
            str1 = str1 + l[index2].upper() + l[index3].lower() + str(e) + w[random.randint(0, 6)]
        print("TIMESTAMP", key, "//", "Username: ", str2, "Password: ", str1)


b = int(input("Enter number of usernames and passwords that's you want: "))
n = int(input("Enter the length of username: "))
username(b,n)