Question1 = " prenez vous l'épé des ames? Oui (O) ou Non (N)"
Question2 = " vous êtes mort"
Question3 = " Vous tourner la tête et un monstre avec des dents assérere apparés, dégainer l'épé? Oui (O) ou Non (N)"
Question4 = " le monstre vous mange tout crue"
Question5 = " Le monstre donne un coup de griffe, esquiver ou bloquer l'attaque? Esquive (E) ou Bloquer (B)"
Question6 = " le bloquage échous, vous mourrez de saignement"
Question7 = " L'esquive fonctionne, vouler vous donner un coup critique? Oui (O) ou Non (N)"
Question8 = " Le monstre profite de l'avantage et vous mourer englouti"
Question9 = " Le coup critique touche le coup, le monstre attaque de nouveau. essayer vous de bloque ou esquiver? Bloquer (B) ou Esquiver (E)"
Question10 = " L'esquive échou, vous mourer empaler"
Question11 = " Le Bloquage fonctione, vouler vous achever le dragon? Oui (O) ou Non (N)"
Question12 = " contrairement a vous le monstre na pas de pitier et vous tue d'un coup"
Question13 = " Victoire, Merci d'avoir jouer"


reponse1 = str(input(Question1)) 
if reponse1 == "O":
    reponse2 = input("vous êtes mort.")
elif reponse1 == "N":
    reponse3 = str(input(Question3))
    if reponse3 == "N":
        reponse4 = input("le monstre vous mange tout crue") 
    elif reponse3 == "O": 
        reponse5 = str(input(Question5))
        if reponse5 == "B":
            reponse6 = input(" le bloquage échous, vous mourrez de saignement")
        elif reponse5 == "E":
            reponse7 = str(input(Question7))
            if reponse7 == "N":
                reponse8 = input(" Le monstre profite de l'avantage et vous mourer englouti")
            elif reponse7 == "O":
                reponse9 = str(input(Question9))
                if reponse9 == "E":
                    reponse10 = input(" L'esquive échou, vous mourer empaler")
                elif reponse9 == "B":
                    reponse11 = str(input(Question11))
                    if reponse11 == "N":
                        reponse12 = input(" contrairement a vous le monstre na pas de pitier et vous tue d'un coup")
                    elif reponse11 == "O":
                        reponse13 = str(input(Question13))
    
    
        