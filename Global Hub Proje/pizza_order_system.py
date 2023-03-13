# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:45:19 2023

@author: musad
"""

import csv
import datetime

file = open("Menu.txt","w")

file.write("""* Lütfen Bir Pizza Tabanı Seçiniz:
1: Klasik
2: Margarita
3: TürkPizza
4: Sade Pizza
* ve seçeceğiniz sos:
11: Zeytin
12: Mantarlar
13: Keçi Peyniri
14: Et
15: Soğan
16: Mısır
* Teşekkür ederiz!
""")

file.close()


class Pizza():
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description
        
    def get_description(self):
        return self.description
            
    def get_cost(self):
        return self.cost
                        
class Classic_Pizza(Pizza):
    def __init__(self):
        self.description = "Classic Pizzadır"
        self.cost = 50
        self.name = "Classic Pizza"

class Margherita_Pizza(Pizza):
    def __init__(self):
        self.description = "Margarita Pizzadır"
        self.cost = 50
        self.name = "Margarita Pizza"   

class Turkish_Pizza(Pizza):
    def __init__(self):
        self.description = "Turkish Pizzadır"
        self.cost = 50
        self.name = "Turkish Pizza"
        
class Dominos_Pizza(Pizza):
    def __init__(self):
        self.description = "Dominos Pizzadır"
        self.cost = 50
        self.name = "Dominos Pizza"
        
class PizzaSos():
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost
    
    def get_description(self):
        return self.description
            
    def get_cost(self):
        return self.cost
    
class olive(PizzaSos):
    def __init__(self):
        self.name = "Zeytin"
        self.description = "Zeytin Sosu"
        self.cost = 2  

class mushroom(PizzaSos):
    def __init__(self):
        self.name = "Mantar"
        self.description = "Mantar Sosu"
        self.cost = 2         

class goat_cheese(PizzaSos):
    def __init__(self):
        self.name = "Keçi Peyniri"
        self.description = "Keçi Peyniri Sosu"
        self.cost = 2  

class meat(PizzaSos):
    def __init__(self):
        self.name = "Et"
        self.description = "Et Sosu"
        self.cost = 2  
        
class onion(PizzaSos):
    def __init__(self):
        self.name = "Soğan"
        self.description = "Soğan Sosu"
        self.cost = 2  
        
class sweetcorn(PizzaSos):
    def __init__(self):
        self.name = "Mısır"
        self.description = "Mısır Sosu"
        self.cost = 2  
        
def main():
    with open("Menu.txt","r") as file:
        print(file.read())
    
    pizza_select = int(input("Pizza seçimi yapınız "))
    pizza_sos_select =int(input("Sos seçimi yapınız "))
    
    cp_name = ""
    cp_cost = 0
    cp_description = ""
    if pizza_select == 1:
        cp_name = Classic_Pizza().name
        cp_cost = Classic_Pizza().get_cost()
        cp_description = Classic_Pizza().get_description()
        
    elif pizza_select == 2:
        cp_name = Margherita_Pizza().name
        cp_cost = Margherita_Pizza().get_cost()
        cp_description = Margherita_Pizza().get_description()        

    elif pizza_select == 3:
        cp_name = Turkish_Pizza().name
        cp_cost = Turkish_Pizza().get_cost()
        cp_description = Turkish_Pizza().get_description()
        
    elif pizza_select == 4:
        cp_name = Dominos_Pizza().name
        cp_cost = Dominos_Pizza().get_cost()
        cp_description = Dominos_Pizza().get_description()
        
    else:
        print("geçersiz pizza seçimi")
        
    cc_name = ""
    cc_cost = 0
    cc_descripton = ""
    if pizza_sos_select == 11:
        cc_name = olive().name
        cc_cost = olive().get_cost()
        cc_descripton = olive().get_description()
        
    elif pizza_sos_select == 12:
        cc_name = mushroom().name
        cc_cost = mushroom().get_cost()
        cc_descripton = mushroom().get_description()        
    
    elif pizza_sos_select == 13:
        cc_name = goat_cheese().name
        cc_cost = goat_cheese().get_cost()
        cc_descripton = goat_cheese().get_description()         

    elif pizza_sos_select == 14:
        cc_name = meat().name
        cc_cost = meat().get_cost()
        cc_descripton = meat().get_description() 

    elif pizza_sos_select == 15:
        cc_name = onion().name
        cc_cost = onion().get_cost()
        cc_descripton = onion().get_description() 
        
    elif pizza_sos_select == 16:
        cc_name = sweetcorn().name
        cc_cost = sweetcorn().get_cost()
        cc_descripton = sweetcorn().get_description() 
        
    else:
        print("Geçersiz sos seçimi")
        

    total_cost = cp_cost + cc_cost
    print(f"toplam tutar {total_cost}")
    customer_name = input("Name: ")
    customer_TC_number = input("TC Number: ")
    customer_credi_card = input("Credi Card: ")
    customer_credi_card_password = input("Password: ")
    times = datetime.datetime.now()
    hour = str(times.hour)
    minute = str(times.minute)
    
    with open('Orders_Database.csv', 'a', newline='') as file:
        writer = csv.writer(file)
     
        writer.writerow(["Pizza", "Souce", "Name", "TC No", "CC No", "CC Password", "Description", "Time"])
        writer.writerow([cp_name, cc_name, customer_name, customer_TC_number, customer_credi_card, customer_credi_card_password, cp_description +' ' + cc_descripton, hour + ':' +minute])
    