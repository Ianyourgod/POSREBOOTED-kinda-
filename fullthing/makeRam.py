chars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"
ram = []
char = 0
for i in range(256):
    if ord(chars[char]) == i:
        ram.append(i)
        char += 1
    else:
        ram.append(0)
print("[")
for i in range(len(ram)):
    if i == 0 or i / 1 == 16 or i / 2 == 16 or i / 3 == 16 or i / 4 == 16 or i / 5 == 16 or i / 6 == 16 or i / 7 == 16 or i / 8 == 16 or i / 9 == 16 or i / 10 == 16 or i / 11 == 16 or i / 12 == 16 or i / 13 == 16 or i / 14 == 16 or i / 15 == 16 or i / 16 == 16:
        print("\n            ",end="")
    print(f"{ram[i]},",end="")
print("]")