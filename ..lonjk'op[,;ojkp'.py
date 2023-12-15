import math
print("  ____     _     _       ____  _   _  _         _     _____   ___   ____  ")
print(" / ___|   / \   | |     / ___|| | | || |       / \   |_   _| / _ \ |  _ \ ")
print("| |      / _ \  | |    | |    | | | || |      / _ \    | |  | | | || |_) |")
print("| |___  / ___ \ | |___ | |___ | |_| || |___  / ___ \   | |  | |_| ||  _ < ")
print(" \____|/_/   \_\|_____| \____| \___/ |_____|/_/   \_\  |_|   \___/ |_| \_\ ")

while True:
    print("-------------------------------------------------------------------------- │")
    print("                                                                           │")
    print("                                                                           │")
    print("                                                                           │")
    s = input("Знак (+, -, *, /,cosinus,stepen,koren,sinus,tanges,cotangens): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/','cosinus','stepen','koren','sinus','tanges','cotangens'):
        print("----------------------------------------------------------------           │")
        a = float(input("first number="))
        b = float(input("second number="))
        print("----------------------------------------------------------------")
        if s == '+':
            print("otvet=",(a + b))
        elif s == '-':
            print("otvet=",(a - b))
        elif s == '*':
            print("otvet=",(a * b))
        elif s == 'stepen':
            print("otvet=",math.pow(a,b))
        elif s == 'cosinus':
            print("otvet=",math.cos(a))
        elif s == 'koren':
            print("otvet=",math.sqrt(a))
        elif s == 'tanges':
            print("otvet=",math.tan(a))
        elif s == 'sinus':
            print("otvet=",math.sin(a))
        elif s == 'cotangens':
            print("otvet=",math.ctg(a))
        elif s == '/':
            if b != 0:
                print("otvet=",(a / b))
            else:
                print("delenie na 0!")
    else:
        print("wrong!")
    g=input("do you want to continue?")
    if g == "yes":
        continue
    else:
        print("programma ostonovlena")
        break
