import os
from random import randrange #pour la creation du nombre aleatoire
import getpass #pour cacher le chiffre quand il est taper en duo



def menu_plus_ou_moin (): #def du menue jeu plus ou moin

	
	print ("                             ############################################")
	print ("                             #           JEU DU PLUS OU MOIN            #")
	print ("                             #                                          #")
	print ("                             # Quel mode voulez vous lancez :           #") #menue choix solo ou duo
	print ("                             #                                          #")
	print ("                             #  1 = Solo                                #")
	print ("                             #  2 = Duo                                 #")
	print ("                             #  3 = Sortir                              #")
	print ("                             ############################################")

	solo_multi = ()
	solo_multi = input ("\nVotre choix : ") #recuperation du choix
	

	if solo_multi == "1":
		jeu_plus_ou_moin (solo_multi)
	elif solo_multi == "2":
		jeu_plus_ou_moin (solo_multi) 		#lancement du mode
	elif solo_multi == "3":
		print ("\nA bientot\n")
	else :
		print ("\nChoix impossible\n")
		menu_plus_ou_moin ()


def jeu_plus_ou_moin (choix): #def jeu plus ou moin

	nb_taper = 0

	if choix == "1":
		os.system("cls")
		chiffre = input ("\nChoissisez le chiffre maximum :\n") 
		chiffre = int(chiffre)
		numero_mystere = randrange (1,chiffre)
		os.system("cls") 
	elif choix == "2":
		os.system("cls")
		chiffre = getpass.getpass("\nChoissisez le chiffre maximum :\n")
		chiffre = int(chiffre)
		numero_mystere = randrange (1,chiffre)
		os.system("cls") 
	else :
		print ("erreur")


	
	while nb_taper != numero_mystere:

		print ("Quel est le numero :")
		nb_taper = input()
		nb_taper = int(nb_taper)

		if nb_taper < numero_mystere:
			os.system("cls") 
			print (f"{nb_taper} est trop petit\n")

		elif nb_taper > numero_mystere:
			print (f"{nb_taper} est trop grand\n")

		elif nb_taper == numero_mystere:
			print (f"Felicitation {nb_taper} est le bon numero\n")

		else:
			print ("Erreur du programme\n")

	


menu_plus_ou_moin()

os.system ("pause")