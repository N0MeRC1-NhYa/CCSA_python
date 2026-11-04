class Kaart:
    rangen = {'aas':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '10':10,
            'boer' : 11, 
            'vrouw': 12, 
            'heer': 13}
    kleuren = {'klaveren': 1, 
               'ruiten': 2, 
               'harten': 3, 
               'schoppen': 4}
    
    def __init__(self, rang, kleur):
        
        if rang not in Kaart.rangen or kleur not in Kaart.kleuren:
            raise AssertionError("ongeldige kaart")
        self.rang = rang
        self.kleur = kleur

    def __repr__(self):
        return f"Kaart(rang='{self.rang}', kleur='{self.kleur}')"

    def __str__(self):
        return  f"{self.kleur} {self.rang}"
    
    def __le__(self, other):
        if not isinstance(other, Kaart):
            return NotImplemented
        return Kaart.rangen.get(self.rang) <= Kaart.rangen.get(other.rang) or \
                (Kaart.rangen.get(self.rang) == Kaart.rangen.get(other.rang) and Kaart.kleuren.get(self.kleur) <= Kaart.kleuren.get(other.kleur))

    def __eq__(self, other):
        if not isinstance(other, Kaart):
            return NotImplemented
        return Kaart.rangen.get(self.rang) == Kaart.rangen.get(other.rang) and self.kleur == other.kleur


    def __lt__(self, other):
        if not isinstance(other, Kaart):
            return NotImplemented
        return Kaart.rangen.get(self.rang) < Kaart.rangen.get(other.rang) or \
                (Kaart.rangen.get(self.rang) == Kaart.rangen.get(other.rang) and Kaart.kleuren.get(self.kleur) < Kaart.kleuren.get(other.kleur))


    def __gt__(self, other):
        if not isinstance(other, Kaart):
            return NotImplemented
        return Kaart.rangen.get(self.rang) > Kaart.rangen.get(other.rang) or \
                (Kaart.rangen.get(self.rang) == Kaart.rangen.get(other.rang) and Kaart.kleuren.get(self.kleur) > Kaart.kleuren.get(other.kleur))


    def __ge__(self, other):
        if not isinstance(other, Kaart):
            return NotImplemented
        return Kaart.rangen.get(self.rang) >= Kaart.rangen.get(other.rang) or \
                (Kaart.rangen.get(self.rang) == Kaart.rangen.get(other.rang) and Kaart.kleuren.get(self.kleur) >= Kaart.kleuren.get(other.kleur))


def vijfde_kaart(l):
    init_rang = l[0].rang
    init_kleur = l[0].kleur
    delta = 0
    if l[1] < l[2] and l[2] < l[3]:
        delta = 1
    if l[3] < l[2] and l[1] < l[3]:
        delta = 2
    if l[1] > l[2] and l[1] < l[3]:
        delta = 3
    if l[1] < l[2] and l[1] > l[3]:
        delta = 4
    if l[1] > l[3] and l[2] < l[3]:
        delta = 5
    if l[1] > l[2] and l[2] > l[3]:
        delta = 6
    init_rang =(Kaart.rangen.get(init_rang) + delta)
    if init_rang > len(Kaart.rangen.keys()):
        init_rang = init_rang % (len(Kaart.rangen.keys()) + 1) + 1
    print(init_rang)
    for k in Kaart.rangen.keys():
        if Kaart.rangen.get(k) == init_rang:
            init_rang = k
            print(init_rang)
            break

    return Kaart(init_rang, init_kleur)

#vijfde_kaart([Kaart('7', 'schoppen'), Kaart('vrouw', 'harten'), Kaart('8', 'klaveren'), Kaart('3', 'ruiten')])
#vijfde_kaart([Kaart('boer', 'harten'), Kaart('6', 'ruiten'), Kaart('9', 'klaveren'), Kaart('aas', 'harten')]) == Kaart(rang='2', kleur='harten')