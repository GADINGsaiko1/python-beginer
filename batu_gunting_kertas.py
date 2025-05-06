import random

main = input("mau main batu gunting kertas (y/n) ?")

while main == "y":
    pilihan_bot = ["batu", "gunting", "kertas"]
    bot = random.choice(pilihan_bot)
    input_user = str(input("pilih (batu/gunting/kertas) :")).lower()

    rules = {
        'batu':'gunting',
        'gunting':'kertas',
        'kertas':'batu'
    }

    if input_user not in rules:
        print("invalid input!!!!!")
        continue
    else:
        if input_user == bot:
            print(f"SERI! kamu = {input_user} bot = {bot} ")
        elif rules[input_user] == bot:
            print(f"kamu MENANG kamu = {input_user} bot = {bot}")
        else:
            print(f"kamu KALAH kamu = {input_user} bot = {bot}")
    main = input("mau main lagi (y/n) ?")