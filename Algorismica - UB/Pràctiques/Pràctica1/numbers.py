# -*- coding: cp1252 -*-
def main():
    print "Aquest programa suma, resta i multiplica un nombre"
    x = input("Escriu el nombre")
    print "Ara li sumarem 3 unitats a" x
    b = x + 3
    print "El resultat de la suma es:" b ". I ara ho multiplicarem per 2"
    c = b * 2
    print "El resultat de la multiplicacio es" c ". I ara li restarem 4 unitats"
    d = c - 4
    print "El resultat de la resta es" d ". I ara multiplicarem" d "per 2 i ho restarem a" x ", el valor inicial que hem escrit"
    e = x - 2 * d
    print "El resultat de l'operació anterior es" e ". Per acabar li sumarem 3 unitats"
    f = e + 3
    print "El resultat de tot el que hem fet és" f
main()
