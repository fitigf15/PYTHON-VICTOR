
def dni(): #Definim la funcio dni
    dni = raw_input("Escriviu el dni i us direm la seva lletra: ") #Definim la variable "dni" com un raw_input. Sera interpretat com un string.
    lletres = [ "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
                "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E" ] # La variable "lletres" es una llista que conte les lletres de la taula de l'exercici
    lletra = 0 #La variable "lletra" te aquest valor
    if len(dni) == 8: #Si el dni introduit te 8 caracters, es a dir, si es compleix la condicio A
        lletra = (int(dni))%23 #La variable lletra tindra aquest nou valor
        print "La lletra del vostre dni es: ", lletres[lletra] #Imprimirim la posicio "lletra" de la llista "lletres"
dni()
