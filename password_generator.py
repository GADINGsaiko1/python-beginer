import random
char_lower = "abcdefghijklmnopqrstuvwxyz"
char_upper = char_lower.upper()
numbs = "0123456789"
symbol = "!@#$%^&*()_-+=~`':\".,><?/;"

char_up, char_low, numb, sym = True, True, True, True

all = ""

if char_up:
    all += char_upper
if char_low:
    all += char_lower
if numb:
    all += numbs
if sym:
    all += symbol

try:
    rand = int(input("mau bikin berapa password ?: "))
    length = int(input("mau seberapa panjang passwordnya ?: "))
except ValueError:
    print("input harus berupa angka ya")

for i in range(rand):
    password = "".join(random.sample(all,length))
    print(password)