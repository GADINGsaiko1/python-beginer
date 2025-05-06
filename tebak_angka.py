import random

user = input("mau main tebak angka (y/n) ?").lower()
if user == "y":
    kesempatan = 3
    random_number = random.randint(1,10)
    while kesempatan > 0:
        try:
            user_input = int(input("tebak angka dari 1 -10 :"))
            if user_input > 10 or user_input < 1:
                print("angka ga boleh lebih dari 10 dan kurang dari 1 | input harus angka !")
                continue
            else:
                if user_input > random_number:
                    kesempatan -= 1
                    print(f"angka kamu kebesaran, sekarang kesempatan kamu tinggal {kesempatan}x tebak lagi")
                elif user_input < random_number:
                    kesempatan -= 1
                    print(f"angka kakmu kekecilan, sekarang kesempatan kamu tinggal {kesempatan}x tebak lagi")
                elif user_input == random_number:
                    print(f"sipp angka yang kamu tebak bener")
        except ValueError:
            print("input harus berupa angka")
    if kesempatan == 0:
        print(f"kamu gagal menebak angka yang benar, angka yang benar adalah {random_number}")
elif user == "n":
    print("okee yaudah")
else:
    print("invalid input!")