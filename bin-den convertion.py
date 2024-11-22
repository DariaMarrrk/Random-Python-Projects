def DenToBinPos(a):
    binary = ""
    x = 7
    while x >= 0:
        base = 2 ** x
        if a >= base:
            binary = binary + "1"
            a = a - base
        else:
            binary = binary + "0"
        x = x -1
    return(binary)

def DenToBinNeg(a):
    binary = "1"
    a += 128
    x = 6
    while x >= 0:
        base = 2 ** x
        if a >= base:
            binary = binary + "1"
            a = a - base
        else:
            binary = binary + "0"
        x = x -1
    return(binary)

def BinToDen(b):
    den = 0
    signed = input("enter 1 for signed and 2 for unsigned ")
    for idx in range(0, len(b)):
        if b[idx] == "1":
            if signed == "1" and idx == 0:
                den += -128
            else:
                den += 2 ** (7 - idx)
    return(den)

menu = input("enter 1 for binary and 2 for denary ")

if menu == "1":
    b = input("enter the binary number ")
    b.split()
    print(BinToDen(b))
elif menu == "2":
    a = int(input("enter the denary number "))
    if a > 0:
        print(DenToBinPos(a))
    else:
        print(DenToBinNeg(a))
