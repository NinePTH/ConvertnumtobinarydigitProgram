decimal_input = int(input("ป้อนตัวเลขฐานสิบ : "))
binary = []
decimal = decimal_input
print("รับ input มา = " + str(decimal_input))
print("-------------------")
while decimal > 0:
    binary.append(str(decimal % 2))
    print("เศษจากการหาร2 = " + str(decimal % 2))
    print()
    decimal = int(decimal / 2)
    print("ผลจากการหาร2 = " + str(decimal))
    print()

print(binary)
print()
binary.reverse()
print(binary)
print()

if (len(binary) < 4 and len(binary) >= 2):
    binary.insert(0,"0")

if (len(binary) != 4 and len(binary) <= 3 and len(binary) >= 2):
    binary.insert(0,"0")

if (len(binary) == 1):
    binary.insert(0,"0")
    binary.insert(0,"0")
    binary.insert(0,"0")

if (len(binary) == 0):
    binary = ["0","0","0","0"]

print(binary)
print()
print(f"{decimal_input} ฐานสิบ แปลงเป็นเลขฐานสองเท่ากับ {''.join(binary)}")
