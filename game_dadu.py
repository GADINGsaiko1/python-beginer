import random 

while True:
    user = input("mau main dice game (y/n) ?").lower()
    if user == "y":
        dadu1 = random.randint(1,6)
        dadu2 = random.randint(1,6)
        print(f"{dadu1}, {dadu2}")
    elif user == "n":
        print("bye bye")
        break
    else:
        print("invalid input!")