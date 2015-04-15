# Modifiqueu el programa convert.py per a que escrigui una presentació del 
# programa. Escriviu-lo en el fitxer convert1.py i executeu-lo.
# convert.py
# Un programa per pasar de graus Celsius a Fahrenheit
# Escrit per : Aquí el vostre nom.
print "Aquest programa converteix els graus que introduim de Celsius a Farenheit"
def main():
    celsius = input(" Quina es la temperatura en Celsius? ")
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print "La temperatura expressada en graus Farenheit es de ", fahrenheit
main()