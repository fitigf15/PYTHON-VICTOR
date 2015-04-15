# Modifiqueu el programa avg.py per a que calculi el promig de tres exàmens. 
# Escriviu-lo en el fitxer avg1.py i executeu-lo.
# avg.py
# Càlcul de la nota promig entre tres examens.
# Il.lustra l’us de l’entrada multiple de Python
def main():
    print "Aquest programa calcula el promig de la nota de tres examens."
    score1, score2, score3 = input("Entra les notes de tres examens separades per una coma: ")
    average = (score1 + score2 + score3) / 3.0
    print "El promig es:", average
main()