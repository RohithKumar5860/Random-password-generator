import random
pass_len = int(input("Enter a length  of the password: "))
pass_data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[];,./?:><{}!@#$%^&*()_-"
password =  "".join(random.sample(pass_data,pass_len))
print(password)
