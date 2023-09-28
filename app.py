

while True:
    try:
        # insertion de la moyenne de l'utilisateur
        moyenne = int(input("Veuiller entrer votre moyenne du baccalauréat: ")) 

        # Valdation des valeurs acceptées
        if (moyenne < 0 or moyenne > 20) :
            print("\x1b[38;5;208m---------------------------------------------------------------\x1b[0m")
            print("\x1b[38;5;208mLa moyenne doit etre une valuer positive comprise entre 0 et 20\x1b[0m")
            print("\x1b[38;5;208m---------------------------------------------------------------\x1b[0m")
        else :
            #
            # enonciation de le reussite ou de l'echeque au BAC
            if moyenne < 10 :
                print("Nous somme dans le regret de vous annoncer que votre note n'est pas sufisante pour avoir votre BAC.")
            else :
                print("\x1b[32m--------------------------------------------------------------------------------\x1b[0m")
                print("\x1b[32mNous avons la joie de vous annoncer que vous avez passés votre BAC avec succes.\x1b[0m")

            #
            # enonciation de la mention obtenu
            if moyenne >= 16 :
                print("\x1b[32mVous avez obtenu la mention TRES BIEN.\x1b[0m")
                print("\x1b[32m--------------------------------------------------------------------------------\x1b[0m")
            elif moyenne >= 14 :
                print("\x1b[32mVous avez obtenu la mention BIEN.\x1b[0m")
                print("\x1b[32m--------------------------------------------------------------------------------\x1b[0m")
            elif moyenne >= 12 :
                print("\x1b[32mVous avez obtenu la mention ASSEZ BIEN.\x1b[0m")
                print("\x1b[32m--------------------------------------------------------------------------------\x1b[0m")
    except ValueError:
        print("\x1b[31m-------------------------------------------------\x1b[0m")
        print("\x1b[31mCe programme n'accepte que des valeurs numeriques\x1b[0m")
        print("\x1b[31m-------------------------------------------------\x1b[0m")



    
