import random
from time import sleep 
from tqdm import tqdm 

print("Initializing The Game")
for i in tqdm (range (100), desc="Loading..."): 
    sleep(0.01)
print("Loading Rock Paper Scissors")
for i in tqdm (range (100), desc="Loading..."): 
    sleep(0.01)
print("Let's Start")

rps = ["R", "P", "S"]

userscore=0
computerscore=0

times = int(input("How many times you want to play?"))

while times>0:
    compch = str(random.choice(rps))
    print("Comp: I made my choise..")

    usch = input("Rock(R), Paper(P) or Scissors(S): ")

    if usch==compch:
        print("It's a Tie..")

    elif usch == "R":
        print("Comp: I took "+compch)
        if compch=="P":
            print("Comp: And I won..")
            print("Better Luck Next Time..")
            computerscore += 1
        elif compch=="S":
            print("Comp: Congo..")
            userscore += 1
    
    elif usch == "P":
        print("Comp: I took "+compch)
        if compch=="S":
            print("Comp: And I won..")
            print("Comp: Better Luck Next Time..")
            computerscore += 1
        elif compch=="R":
            print("Comp: Congo..")
            userscore += 1

    elif usch == "S":
        print("Comp: I took "+compch)
        if compch=="R":
            print("Comp: And I won..")
            print("Comp: Better Luck Next Time..")
            computerscore += 1
        elif compch=="P":
            print("Comp: Congo..")
            userscore += 1

    times -= 1

print("Game Over..")

for i in tqdm (range (100), desc="Loading..."): 
    sleep(0.01)

if userscore<computerscore:
    print("Comp: I am Best..")
elif userscore==computerscore:
    print("Comp: Not bad.. but be careful next time..")
    print("Comp: Always not your luck..")
elif userscore>computerscore:
    print("Comp: Good.. Let's see again next time..")