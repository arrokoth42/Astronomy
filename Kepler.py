import math
while True:
    print("Ceci est un fichier comprenant les lois de Kepler.")
    action = input("Vous pouvez savoir la première loi (loi1), la deuxième (loi2) et la troisième (loi3). Vous pouvez également effectuer un calcul (calc). Pour quitter le programme, tapez 'quit'. ")
    if action == "quit":
        break
    if action == "loi1":
        print("Les planètes décrivent des orbites elliptiques dont le Soleil est l'un des foyers. Le point le plus proche de ce dernier est nommé périhélie et le plus éloigné aphélie.")
    if action == "loi2":
        print("Le rayon vecteur balaie des aires égales en des temps égaux, ce qui implique que la vitesse de la planète varie.")
    if action == "loi3":
        print("Le rapport du carré de la période de révolution sur le cube du grand axe est constant pour toutes les planètes du système solaire.")
    if action == "calc":
        opération = input("Que voulez-vous calculer ?\n Un demi-grand axe (a),\n un demi-petit axe (b),\n une excentricité (e),\n une apoapside (rp),\n une périapside (ra),\n ou une distance focale (c) ? ")
        if opération == "a":
            rp = float(input("Quelle est la distance au périastre ? "))
            ra = float(input("Quelle est la distance à l'apoastre ? "))
            a = (rp + ra) / 2
            print("Le demi-grand axe est égal à " + str(a))
        if opération == "b":
            a = float(input("Quelle est la distance au demi-grand axe ? "))
            e = float(input("Quelle est l'excentricité ? "))
            b = a * math.sqrt(1 - e**2)
            print("Le demi-petit axe est égal à " + str(b))
        if opération == "e":
            a = float(input("Quelle est la distance au demi-grand axe ? "))
            b = float(input("Quelle est la distance au demi-petit axe ? "))
            e = math.sqrt(1 - (b**2 / a**2))
            print("L'excentricité est égale à " + str(e))
        if opération == "rp":
            a = float(input("Quelle est la distance au demi-grand axe ? "))
            e = float(input("Quelle est l'excentricité ? "))
            rp = a * (1 - e)
            print("La distance au périastre est égale à " + str(rp))
        if opération == "ra":
            a = float(input("Quelle est la distance au demi-grand axe ? "))
            e = float(input("Quelle est l'excentricité ? "))
            ra = a * (1 + e)
            print("La distance à l'apoastre est égale à " + str(ra))
        if opération == "c":
            a = float(input("Quelle est la distance au demi-grand axe ? "))
            e = float(input("Quelle est l'excentricité ? "))
            c = a * e
            print("La distance focale est égale à " + str(c))
