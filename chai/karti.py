def naminal_karti(card: tuple):
    if card[0].isdigit():
        return int(card[0])
    return 10
def kruchenie(kolodakart:list):
    k = kolodakart[25:]
    ok=kolodakart[25:52]
    y=0
    for i in range(3):
        b=naminal_karti(k[0])
        y+=b
        k=k[9 - b:]
    ok.append(k)
    return ok[y]




a=input()
koloda_kart=a.split()
newkoloda_kart=[]
for  i in koloda_kart:
    newkoloda_kart.append((i[0],i[1]))
print(kruchenie(a))
