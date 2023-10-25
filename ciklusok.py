def harommal_oszthato(szam1):
    oszthatok:int= 3
    while oszthatok <= szam1:
        if oszthatok %3 == 0:
            if oszthatok == 3:
                print(oszthatok, end=',')
            else:
                print(f'{oszthatok}', end =',')
        oszthatok +=3
    print("")

def masodik_feladat(pozitiv_szam):
        if pozitiv_szam >= 0:
            szamok = pozitiv_szam
            while szamok >=1:
                if szamok ==1:
                    print(szamok, end='')
                else:
                    print(szamok, end='')
                szamok-=1
        print("")

def harmadik_feladat(bekert_szam):
    i:int=bekert_szam
    while i %5 != 0:
        print("A bekért szám nem osztható öttel")
        i:int=int(input("Adj meg egy számot: "))
    print("A bekért szám osztható öttel")

def negyedik_feladat(egy_szam):
    i:int=0
    while i <= egy_szam:
        if i % 3 == 0:
            print("BUM")
        else:
            print(i)
        if i % 2 == 0:
            print("BAM")
        else:
            print(i)
        if i % 2 == 0 and i % 3 == 0:
            print("BUMBAM")
        else:
            print(i)
    i += 1


