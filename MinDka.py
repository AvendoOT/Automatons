stanja = input().split(",")
simboli = sorted(input().split(","))
prihvatljivaStanja = input()
if prihvatljivaStanja == "":
    prihvatljivaStanja = []
else:
    prihvatljivaStanja = sorted(prihvatljivaStanja.split(","))
neprihvatljivaStanja = []
for x in stanja:
    if x not in prihvatljivaStanja:
        neprihvatljivaStanja.append(x)
neprihvatljivaStanja = sorted(neprihvatljivaStanja)
q0 = input()
omega = dict()
def napraviTablicu(s, r):
    if s > r:
        s, r = r, s
    return tablica.get((s, r), 0)

def postaviTablicu(s, r):
    if (s > r):
        s, r = r, s
    tablica[(s, r)] = 1

def napraviListu(s, r):
    if (s > r):
        s, r = r, s
    return lista.get((s, r), [])

def spojiListu(s, r, a):
    if (s == r):
        return
    elif (s > r):
        s, r = r, s
    if (s, r) not in lista:
        lista[s, r] = []
    lista[s, r].append(a)

def brisi(stanja):
    for iter in range(len(stanja)-1):
        s = stanja[iter]
        duljina = len(stanja)
        for jiter in range(iter+1, duljina):
            r = stanja[jiter]
            for sim in simboli:
                s1 = omega[s, sim]
                r1 = omega[r, sim]
                if napraviTablicu(s1, r1) == 1:
                    postaviTablicu(s, r)
                    red = napraviListu(s1, r1)
                    z = 0
                    while z < len(red):
                        s2, r2 = red[z]
                        postaviTablicu(s2, r2)
                        for t in napraviListu(s2, r2):
                            if t not in red:
                                red.append(t)
                        z += 1
                else:
                    if s1 != r1:
                        spojiListu(s1, r1, (sim, r))

prijelaz = input()
while (prijelaz != "" and prijelaz != "\n"):
    prijelaz = prijelaz.split("->")
    stanje, znak = tuple(prijelaz[0].split(','))
    omega[stanje, znak] = prijelaz[1]
    try:
        prijelaz = input()
    except:
        prijelaz = ""

poc = []
iter = 0
poc.append(q0)
while (iter < len(poc)):
    skup = set()
    stanje = poc[iter]
    skup = skup | {stanje}
    for sim in simboli:
        skup = skup | {omega[(stanje, sim)]}
    for sim in skup:
        if sim not in poc:
            poc.append(sim)
    iter = iter + 1

novi = set()
novi = set(stanja) - set(poc)
    
for sim in novi:
    stanja.remove(sim)
    if sim in prihvatljivaStanja:
        prihvatljivaStanja.remove(sim)
    else:
        neprihvatljivaStanja.remove(sim)
    for skup in simboli:
        del(omega[sim, skup])
tablica = dict()
lista = dict()
# Algoritam br.3
for p in prihvatljivaStanja:
    for poc in neprihvatljivaStanja:
        postaviTablicu(p, poc)

if len(neprihvatljivaStanja) > 0:
    brisi(neprihvatljivaStanja)
    
if len(prihvatljivaStanja) > 0:
    brisi(prihvatljivaStanja)

for iter in range(len(stanja)-1, 0, -1):
    p = stanja[iter]
    # s>r
    for j in range(iter-1, -1, -1):
        poc = stanja[j]   
        if (napraviTablicu(p, poc) == 0):
            for stanje, znak in omega:
                if omega[(stanje, znak)] == p:
                    omega[(stanje, znak)] = poc
            for znak in simboli:
                if (p, znak) in omega:
                    del(omega[p, znak])
            if p in neprihvatljivaStanja:
                neprihvatljivaStanja.remove(p)
            elif p in prihvatljivaStanja:
                prihvatljivaStanja.remove(p)
            if q0 == p:
                q0 = poc

ukupnoStanje = prihvatljivaStanja + neprihvatljivaStanja
stanja = sorted(ukupnoStanje)
print(','.join(stanja))
print(','.join(simboli))
print(','.join(prihvatljivaStanja))
print(q0)
for skup in stanja:
    for sim in simboli:
        print("{},{}->{}".format(skup, sim, omega[skup, sim]))
