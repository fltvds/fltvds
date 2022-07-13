from random import randint

raskusaste = input("Valige raskusaste - kerge/keskmine/raske: ")
raskus = 5
if raskusaste == "keskmine":
    raskus = 4
elif raskusaste == "raske":
    raskus = 3
    
a = [randint(0,9) for i in range(5)]
b = [i for i in range(10)]


while len(a) > 0 and raskus > 0:
    print("Valikuvõimalused: ", b)
    num = int(input("Arvake, milline arv leidub listis: "))
    if num in b:
        b.remove(num)
        if num in a:
            print("Arvasid õigesti!")
            c = a.count(num)
            for i in range(c):
                a.remove(num)
        else:
            print("Arvasid valesti")
            raskus -= 1
if raskus == 0:
    print("Sa kaotasid mängu! Listis jäi veel järgi: ", a)
else:
    print("WIN")