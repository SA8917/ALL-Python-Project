dict=["abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","0123456789","!@#$%^&*()_+-="]
import random

while True:
    password=str(input("Enter your password and this program will generate a strong password: "))
    for i in range(0,len(dict)):
        password=password+dict[i][random.randint(0,len(dict[i])-1)]
    print(password)
    break