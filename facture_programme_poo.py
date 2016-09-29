# coding: utf-8
from __future__ import unicode_literals
import time
import os
import json
from lxml import etree

class Client:
    client = []
    client_n = 0
    selected_client = ""
    with open('clients_file.json', 'r') as cfile:
        client = json.load(cfile)

    def choice_client(self, client_c):
        return Client.client[client_c - 1]
    def add_client(self, client_a):
        Client.client.append(client_a)
        with open('clients_file.json', 'w') as cfile:
            json.dump(Client.client, cfile)
        Client.selected_client = Client.client[len(Client.client) -1]
    def show_clients(self):
        for c in Client.client:
			Client.client_n += 1
			print "N° %d: %s" % (Client.client_n, c)

client_obj = Client()

class Product:
    products_stock = []
    with open('products_file.json', 'r') as pfile:
        products_stock = json.load(pfile)
    n_p = 0
    selected_products = []
    selected_products_q = []
    selected_products_p = []
    add_product = {"nom": "", "qty": 0, "prix unitaire": 0}
    add_product_q = 0

    def product_select(self,product_n,product_q):
        #return
        Product.selected_products.append(Product.products_stock[product_n -1]["nom"])
        Product.selected_products_q.append(product_q)
        Product.selected_products_p.append(Product.products_stock[product_n -1]["prix unitaire"])
        Product.products_stock[product_n -1]["qty"] -= product_q
        with open('products_file.json', 'w') as pfile:
            json.dump(Product.products_stock, pfile)
    def product_add(self,product_n,product_q_stock,product_q_invoice,product_p):
        #return
        Product.add_product["nom"] = product_n
        Product.add_product["qty"] = product_q_stock
        Product.add_product["prix unitaire"] = product_p
        Product.add_product_q = product_q_invoice
        Product.selected_products.append(Product.add_product["nom"])
        Product.selected_products_q.append(Product.add_product_q)
        Product.selected_products_p.append(Product.add_product["prix unitaire"])

        Product.products_stock.append(Product.add_product)
        with open('products_file.json', 'w') as pfile:
            json.dump(Product.products_stock, pfile)
    def show_products_stock(self):
        for p in Product.products_stock:
            if Product.n_p < len(Product.products_stock):
                Product.n_p += 1
            print "N° %d:" % Product.n_p, p

product_obj = Product()

class Invoice:
    inv_no = 0
    client_name = client_obj.selected_client
    Date = time.strftime("%d/%m/%Y %H:%M")
    total_h = 0
    Taxe = 0
    total_ttc = 0
    n = 0

    def total_HT(self):
        for p in product_obj.selected_products_p:
            Invoice.total_h += p * product_obj.selected_products_q[Invoice.n]
            Invoice.n += 1

invoice_obj = Invoice()

print "-----------------------------------"
no = int(raw_input("N° Facture : "))
invoice_obj.inv_no = no
print "-----------------------------------"
print "Choix du client :\n> 1: Selection\n> 2: Nouveau"
new_old = int(raw_input("Votre choix ? 1 / 2 :"))
if new_old == 1:
    print "----------------- Clients -----------------"
    client_obj.show_clients()
    print "-----------------------------------"
    y_choice = int(raw_input('N° du client souhaité :'.encode('utf-8')))
    client_obj.selected_client = client_obj.choice_client(y_choice)
elif new_old == 2:
    print '----------------- Nouveau Client ------------------'
    new_client = raw_input("Nom du nouveau client :")
    client_obj.add_client(new_client)
    print "> Nouveau client ajouté <"
print '\n-----------------------------------'

autre_prod = True
while autre_prod == True:
    print "Saisie des produits\n> 1: Nouveau produit ?\n> 2: Choisir un produit existant"
    product_new_old = int(raw_input("Votre choix ? 1 / 2 :"))

    if product_new_old == 1:
        prod_name = raw_input("> Nom Produit :")
        stock_q = int(raw_input("> Quantité Stock :"))
        price = int(raw_input("> Prix Unitaire :"))
        invoice_q = int(raw_input("> Quantité Facture :"))
        product_obj.product_add(prod_name,stock_q,invoice_q,price)
        s_autre_prod = raw_input("Saisir un autre produit ? oui/non :")
        if s_autre_prod == "oui" or s_autre_prod == "o":
            autre_prod = True
        else:
            autre_prod = False
    elif product_new_old == 2:
        print "---------- Stock ----------"
        product_obj.show_products_stock()
        no_prod = int(raw_input("N° du produit :"))
        qte_prod = int(raw_input("Quantité :"))
        product_obj.product_select(no_prod, qte_prod)
        s_autre_prod = raw_input("Saisir un autre produit ? oui/non :")
        if s_autre_prod == "oui" or s_autre_prod == "o":
            autre_prod = True
        else:
            autre_prod = False
invoice_obj.total_HT()
tva = int(raw_input("> La Taxe (%) :"))
print "------------------------ Facture N° %d ----------------------" % invoice_obj.inv_no
invoice_obj.Taxe = tva
invoice_obj.total_ttc =  tva * invoice_obj.total_h / 100 + invoice_obj.total_h
print "Nom du client:", client_obj.selected_client
print "Date:", invoice_obj.Date
print "-------------------------------------------"
print "Liste des produits :"
print "-------------------------------------------"
n = 0
for e in product_obj.selected_products:
    print "Nom :", e
    print "Quantité :", product_obj.selected_products_q[n]
    print "Prix Unitaire :", product_obj.selected_products_p[n], "DZD"
    print "Sous total :", invoice_obj.total_h, "DZD"
    n += 1
    print "-----------------------"

print "Total HT :", invoice_obj.total_h, "DZD"
print "--------------------------------------------"
print "Taxe :", invoice_obj.Taxe, "%"
print "--------------------------------------------"
print "Total TTC :", invoice_obj.total_ttc, "DZD"
print "--------------------------------------------"

''' = etree.Element("Facture")
root.set("id", invoice_obj.inv_no)
root.set("Date", invoice_obj.Date)
client = etree.SubElement(root, "Client")
client.text = str(client_obj.selected_client)
print root'''


os.system("pause")
