# coding=utf-8
# definicija automata:
# $Enka = (skupStanja, simboli, omega, q0, prihvat)
# unosimo ulazne nizove
ulazniNiz = input().split('|')
# unosimo stanja automata
skupStanja = input().split(',')
# unosimo simbole abecede i njima dodajemo epsilon znak
simboli = input().split(',').append('$')
# unosimo prihvatljiva stanja
prihvat = input().split(',')
# unosimo početno stanje (samo jedno!)
q0 = input()
# funkcija prijelaza omega u formatu rječnika
# (stanje, znak): nova stanja
# punimo ga kasnije ovisno o definiciji
omega = dict()
#MAIN
# punimo riječnik
prijelaz = input()
while (prijelaz != "\n" and prijelaz != ''):
    prijelaz = prijelaz.split("->")
    # treba nam indeksirana lista bez duplikata
    start = tuple(prijelaz[0].split(','))
    stanje = start[0]
    znak = start[1]
    # ključ = stanje,znak -- vrijednost = skup sljedećih stanja
    omega[stanje, znak] = set(prijelaz[1].split(','))
    # ovaj dio je 'posuđen' sa Stack Overflow-a jer mi baca error pa ne znam kako drugačije da napravim
    try:
        prijelaz = input()
    except:
        prijelaz = ''
del(prijelaz)

#iteracija po podnizovima ulaznog niza
for podniz in ulazniNiz:
    # podjela po znakovima
    podniz = podniz.split(',')
    # u kojem smo stanju trenutno (unija s njegovima epsilon prijelazima)
    # ako je stanje prazni skup samo ga vratiti
    if (q0 == '#'):
        skup = set()
        skup =  set('#')
    # ako stanje postoji onda dodati vrijednost od zadanog ključa
    # ako prijelaz nije definiran dodati prazan skup (default za set)
    else:
        vrijednost = omega.get((q0, '$'), set('#'))
        # stvaramo skup vrijednosti (bez duplikata)
        skup = set()
        duljina = len(skup)
        # presjek novostvorenog skupa i vrijednosti po ključu
        skup = skup | vrijednost
        while (len(skup) > duljina):
            noviSkup = set()
            duljina = len(skup)
            # gledamo epsilon okruženja
            for epsilon in skup:
                noviSkup = noviSkup | omega.get((epsilon,'$'), set('#'))
            skup = skup | noviSkup
            del(noviSkup)
        skup = skup
    presjek = set([q0]) | skup
    trenutnoStanje = presjek - set('#')
    # ispis početnog stanja
    sortirano = sorted(trenutnoStanje)
    print(','.join(sortirano), end = '')
    # iteracija po znakovima podniza
    for znak in podniz:
        # skup sljedećih stanja bez duplikata
        sljedStanje = set()
        for stanje in trenutnoStanje:
            # u koja sve stanja prelazimo za dani znak
            # slično kao i za početno stanje
            # ako je stanje prazni skup samo ga vratiti
            if (stanje == '#'):
                skup = set()
                skup = set('#')
    # ako stanje postoji onda dodati vrijednost od zadanog ključa
    # ako prijelaz nije definiran dodati prazan skup (default za set)
            else:
                vrijednost = omega.get((stanje, znak), set('#'))
        # stvaramo skup vrijednosti (bez duplikata)
                skup = set()
                duljina = len(skup)
        # presjek novostvorenog skupa i vrijednosti po ključu
                skup = skup | vrijednost
                while (len(skup) > duljina):
                    noviSkup = set()
                    duljina = len(skup)
            # gledamo epsilon okruženja
                    for epsilon in skup:
                        noviSkup = omega.get((epsilon,'$'), set('#')) | noviSkup
                    skup = skup | noviSkup
                    del(noviSkup)
                skup = skup
            sljedStanje = sljedStanje | skup
        # ako imamo skup stanja (više od jednog)
        if (len(sljedStanje) > 1):
            # ako je prazni skup u stanjima spremimo razliku dva skupa
            if ('#' in sljedStanje):
                trenutnoStanje = set(sljedStanje) - set('#')
            else:
                trenutnoStanje = set(sljedStanje)
        else:
            trenutnoStanje = set(sljedStanje)
        del(sljedStanje)
        # ispis gdje smo s očuvanim leksikografskim poretkom
        sortirano = sorted(trenutnoStanje)
        print('|{}'.format(','.join(sortirano)), end='')
    print("\n", end = '')

    
    
    

    

    
    
    





