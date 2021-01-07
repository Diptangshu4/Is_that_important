import random

while True:
    l=input("[y/n]:")
    if l == "y":
        x = random.randint(1,6)
        print("Your no. is")
        print(x)

    elif l=="n":
        print("Thanks..")
        break