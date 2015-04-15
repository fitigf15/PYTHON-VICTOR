#
# Practica inicial 21/09/2012 algorísmica
# Josep Boldú quirós
#

def main1():
        a = 3-4+10
        b = 5*6
        c = 7.0/8.0
        print "These are the values:", a ,b, c
        print "Increment", a, "by one: "
        a = a + 1
        print a
        print "The sum of", a , "and", b, "is"
        d = a + b
        print d
        number = input("Input a number ")
        print number

def main2():
    nom = raw_input("posa el teu nom i cognoms: ")
    print nom

def main3():
    num = input("Entra un numero sencer: ")
    numoriginal = num
    num = ((num + 3)*2)-4
    num = ((num*2)-numoriginal)+3
    print num


def main3():
   celsius = input("What is the Celsius temperature? ")
   print ("has introduit "), celsius ,(" graus Celcius")
   farenheit = 9.0 / 5.0 * celsius + 32
   print ("Fem el canvi a graus Farenheit")
   print "The temperature is " , farenheit , " degrees Farenheit."

def main():
    print ("Aquest programa calcula el promig de la nota de tres examens.")
    score1, score2, score3 = input("Entra la nota dels tres examens separades per una coma: ")
    average = (score1+score2+score3) / 3.0
    print "El promig es: ", average
    
main()

