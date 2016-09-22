# coding: utf-8
from __future__ import unicode_literals
import os
import random
import time

client = ["Client 1", "Client 2", "Client 3", "Ajouter un client"]
produits = {
    "Imac 21.5" : 140000,
    "Ps4" : 48000,
    "Oculus rift" : 85000,
    "Xperia z" : 79000,
    "Manette xbox" : 6900
    }
num_produit = 0
num_client = 0
client_choisi = ""
num_facture = random.randint(1, 2000)
nombre_produits_choisi = 0
commande_acheve = False
qte_produits_achete = {
    "Xperia z" : 0,
    "Imac 21.5" : 0,
    "Oculus rift" : 0,
    "Ps4" : 0,
    "Manette xbox" : 0
    }
tva = 18
total_HT = 0
total_TTC = 0
xperia_HT = 0
xperia_TTC = 0
buy_xperia = False
imac_HT = 0
imac_TTC = 0
buy_imac = False
oculus_HT = 0
oculus_TTC = 0
buy_oculus = False
ps4_HT = 0
ps4_TTC = 0
buy_ps4 = False
manette_HT = 0
manette_TTC = 0
buy_manette = False

print "Choisissez un client :"
for xclient in client:
    num_client += 1
    print num_client,"-", xclient

while client_choisi == "":
    choix = raw_input("?")
    if choix == "1" or choix == "client 1":
        client_choisi = client[0]
    elif choix == "2" or choix == "client 2":
	client_choisi = client[1]
    elif choix == "3" or choix == "client 3":
        client_choisi = client[2]
    elif choix == "4" or choix == "ajouter un client":
	client_choisi = client[3]
if client_choisi == client[3]:
    while client_choisi == client[3] or client_choisi == '' or client_choisi == ' ':
        client_choisi = raw_input("Donner un nom a votre client :")
print client_choisi, "| OK"

print "------------------------------------------------------------"
print "Facture N° %d              " % (num_facture), time.strftime("%d/%m/%Y %H:%M")
print "------------------------------------------------------------"

print "\nChoisissez le produit souhaité: (tapez t ou terminer pour finir votre commande)"
print "\n    Produit   |   Prix HT\n"
for xproduit in produits:
    num_produit += 1
    print num_produit,"-", xproduit, " | ", produits[xproduit], "D.A"

while commande_acheve != True or nombre_produits_choisi < 1:
    ajouter_produit = raw_input("\n>")
    if ajouter_produit == "1" or ajouter_produit == "xperia z":
        nombre_produits_choisi += 1
        total_HT += produits["Xperia z"]
        total_TTC += tva * produits["Xperia z"] / 100 + produits["Xperia z"]
        qte_produits_achete["Xperia z"] += 1
        if buy_xperia == False:
    		xperia_HT = produits["Xperia z"]
    		xperia_TTC = tva * xperia_HT / 100 + xperia_HT
    		buy_xperia = True
        print "Nombre de produits choisi: %d    Total HT: %d D.A" % (nombre_produits_choisi, total_HT)
    elif ajouter_produit == "2" or ajouter_produit == "imac 21.5":
    	nombre_produits_choisi += 1
    	total_HT += produits["Imac 21.5"]
    	total_TTC += tva * produits["Imac 21.5"] / 100 + produits["Imac 21.5"]
    	qte_produits_achete["Imac 21.5"] += 1
    	if buy_imac == False:
    		imac_HT = produits["Imac 21.5"]
    		imac_TTC = tva * imac_HT / 100 + imac_HT
    		buy_imac = True
    	print "Nombre de produits choisi: %d    Total HT: %d D.A" % (nombre_produits_choisi, total_HT)
    elif ajouter_produit == "3" or ajouter_produit == "oculus rift":
    	nombre_produits_choisi += 1
    	total_HT += produits["Oculus rift"]
    	total_TTC += tva * produits["Oculus rift"] / 100 + produits["Oculus rift"]
    	qte_produits_achete["Oculus rift"] += 1
    	if buy_oculus == False:
    		oculus_HT = produits["Oculus rift"]
    		oculus_TTC = tva * oculus_HT / 100 + oculus_HT
    		buy_oculus = True
    	print "Nombre de produits choisi: %d    Total HT: %d D.A" % (nombre_produits_choisi, total_HT)
    elif ajouter_produit == "4" or ajouter_produit == "ps4":
    	nombre_produits_choisi += 1
    	total_HT += produits["Ps4"]
    	total_TTC += tva * produits["Ps4"] / 100 + produits["Ps4"]
    	qte_produits_achete["Ps4"] += 1
    	if buy_ps4 == False:
    		ps4_HT = produits["Ps4"]
    		ps4_TTC = tva * ps4_HT / 100 + ps4_HT
    		buy_ps4 = True
    	print "Nombre de produits choisi: %d    Total HT: %d D.A" % (nombre_produits_choisi, total_HT)
    elif ajouter_produit == "5" or ajouter_produit == "manette xbox":
    	nombre_produits_choisi += 1
    	total_HT += produits["Manette xbox"]
    	total_TTC += tva * produits["Manette xbox"] / 100 + produits["Manette xbox"]
    	qte_produits_achete["Manette xbox"] += 1
    	if buy_manette == False:
    		manette_HT = produits["Manette xbox"]
    		manette_TTC = tva * manette_HT / 100 + manette_HT
    		buy_manette = True
    	print "Nombre de produits choisi: %d    Total HT: %d D.A" % (nombre_produits_choisi, total_HT)
    elif ajouter_produit == "t" or ajouter_produit == "T" or ajouter_produit == "terminer":
    	commande_acheve = True
    	print "Nombre de produits choisi: %d    Total HT: %d D.A" % (nombre_produits_choisi, total_HT)

print "\n\n------------------------ FACTURE ---------------------------\n\n"

print "Nom Client:", client_choisi
print "\nFacture N°:", num_facture
print "\nDate et Heure:", time.strftime("%d/%m/%Y %H:%M")

print "\n\n  PRODUIT   | Quantité | %TVA | PRIX UNITAIRE HT | PRIX TOTAL HT"

if buy_manette == True:
	print "Manette xbox    ", qte_produits_achete["Manette xbox"], "      ", tva, "      ", produits["Manette xbox"], "D.A         ", produits["Manette xbox"] * qte_produits_achete["Manette xbox"], "D.A"
	
if buy_ps4 == True:
	print "Ps4             ", qte_produits_achete["Ps4"], "      ", tva, "     ", produits["Ps4"], "D.A        ", produits["Ps4"] * qte_produits_achete["Ps4"], "D.A"
	
if buy_oculus == True:
	print "Oculus rift     ", qte_produits_achete["Oculus rift"], "      ", tva, "     ", produits["Oculus rift"], "D.A        ", produits["Oculus rift"] * qte_produits_achete["Oculus rift"], "D.A"
	
if buy_imac == True:
	print "Imac 21.5       ", qte_produits_achete["Imac 21.5"], "      ", tva, "    ", produits["Imac 21.5"], "D.A       ", produits["Imac 21.5"] * qte_produits_achete["Imac 21.5"], "D.A"
	
if buy_xperia == True:
	print "Xperia z        ", qte_produits_achete["Xperia z"], "      ", tva, "     ", produits["Xperia z"], "D.A        ", produits["Xperia z"] * qte_produits_achete["Xperia z"], "D.A"
	
print "\n\nNombre de produits achetés:", nombre_produits_choisi, "         Prix total des achats HT:", total_HT,"D.A"
print "\nTaux TVA sur chaque produit:", tva,"%", "     Prix total des achats TTC:", total_TTC, "D.A"

print "\n\n----------------------------------------------------------------------------"
os.system("pause")
