#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""

import sqlite3 as sql
import tkinter as tk
from tkinter import font
class main():
    def __init__(self) -> None:
        file = 'dbaseVet2.db'
        self.connection = sql.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        create table if not exists customers (
            id integer primary key autoincrement,
            petname tinytext,
            species tinytext,
            breed tinytext,
            ownername tinytext,
            ownerPN int,
            owneremail tinytext,
            ownerbalance int,
            firstvisit tinytext);
        """
        self.root = tk.Tk()
        self.root.title("DataBase Finder")
        self.root.geometry("1050x300")
        self.cursor.execute(query)
        self.Label_a = tk.Label(self.root,text=f"DataBase Editor/Locator")
        self.edit= tk.Button(self.root, text="View all!", command=self.getall)
        self.Label_b = tk.Label(self.root,text="Enter:")
        self.entry = tk.Entry(self.root, font=("calibri"))
        self.Label_c = tk.Label(self.root,text="Find By?")
        
        #self.C_entry = tk.OptionMenu(self.root,variable=temp,value=1)
        options = [ 
            "ID", 
            "Phone Number", 
            "Email Address"
                ] 
        self.clicked = tk.StringVar() 
        self.clicked.set( "ID" )
        self.drop = tk.OptionMenu(self.root , self.clicked , *options ) 
        self.drop.grid(row = 3, column=2) 
        self.button = tk.Button(self.root , text = "Find!" , command = self.show ).grid(row = 3, column=3) 
        self.label = tk.Label(self.root , text = " " ) 
        self.label.grid(row = 3, column=5)

        #self.solutionButton = tk.Button(self.root, text="Find!", command=self.determineselection)
        #self.ans = tk.Entry(self.root, font=("calibri"))

        self.Label_a.grid(row=1, column=1)
        self.edit.grid(row=1, column=2)
        self.Label_b.grid(row=2, column=1)
        self.entry.grid(row=2, column=2)
        self.Label_c.grid(row=3, column=1)
        #self.C_entry.grid(row=1, column=6)
        #self.solutionButton.grid(row=2, column=1, columnspan=4)
        #self.ans.grid(row=2, column=5)
        self.displayANGY = tk.Label(self.root, text = "")
        self.displayANGY.grid(row=3, column=4, columnspan=5)
        self.petnameLable = tk.Label(self.root, text = "Petname").grid(row=4, column=1)
        self.speciesLable = tk.Label(self.root, text = "Species").grid(row=4, column=2)
        self.breedLable = tk.Label(self.root, text = "Breed").grid(row=4, column=3)
        self.ownernameLable = tk.Label(self.root, text = "Owner's Name").grid(row=4, column=4)
        self.ownerPNLable = tk.Label(self.root, text = "Owner's Phone").grid(row=4, column=5)
        self.owneremailLable = tk.Label(self.root, text = "Owner email").grid(row=4, column=6)
        self.balanceLable = tk.Label(self.root, text = "Owner balance").grid(row=4, column=7)
        self.visitLable = tk.Label(self.root, text = "first visit").grid(row=4, column=8)
        self.petnameEntry = tk.Entry(self.root, font=("calibri"))
        self.petnameEntry.grid(row=5, column=1)
        self.speciesEntry = tk.Entry(self.root)
        self.speciesEntry.grid(row=5, column=2)
        self.breedEntry = tk.Entry(self.root)
        self.breedEntry.grid(row=5, column=3)
        self.ownernameEntry = tk.Entry(self.root)
        self.ownernameEntry.grid(row=5, column=4)
        self.ownerPNEntry = tk.Entry(self.root)
        self.ownerPNEntry.grid(row=5, column=5)
        self.owneremailEntry = tk.Entry(self.root)
        self.owneremailEntry.grid(row=5, column=6)
        self.balanceEntry = tk.Entry(self.root)
        self.balanceEntry.grid(row=5, column=7)
        self.visitEntry = tk.Entry(self.root)
        self.visitEntry.grid(row=5, column=8)    
        self.enternew = tk.Button(self.root, text="Enter new file", command=self.insertRecord).grid(row=6,column=1)
        self.display = tk.Label(self.root, text="")
        self.display1 = tk.Label(self.root, text="")
        self.display2 = tk.Label(self.root, text="")
        self.display3 = tk.Label(self.root, text="")
        self.display4 = tk.Label(self.root, text="")
        self.display5 = tk.Label(self.root, text="")
        self.display6 = tk.Label(self.root, text="")
        self.display7 = tk.Label(self.root, text="")
        self.display8 = tk.Label(self.root, text="")
        self.display.grid(row=7,column=1, columnspan=8)
        self.display1.grid(row=7,column=2)
        self.display2.grid(row=7,column=3)
        self.display3.grid(row=7,column=4)
        self.display4.grid(row=7,column=5)
        self.display5.grid(row=7,column=6)
        self.display6.grid(row=7,column=7)
        self.display7.grid(row=7,column=8)




        self.openwindow()
        self.selection()
    def show(self): 
        way = self.clicked.get()
        if way == "ID":
            self.retrieveID()
        if way == "Email Address":
            self.retrieveEmail()
        if way == "Phone Number":
            self.retrievePhone()
	    #self.label.config( text = "placeholder" )
    def openwindow(self):
        self.root.mainloop()
    def determineselection(self):
        print("h")
    
    def selection(self):
        
        
        #while True:

        #    try:
        #        choice = int(input("Welcome to database editor, you can insert a new record (1), retrieve a record by their id (2), retrieve a record by the email (3), retrieve a record by phone number (4), or retrieve all (5): "))
        #        break
        #    except:
        #        print("Enter a valid selection")
        choice = None
        if choice == 1:
            self.insertRecord()
        elif choice == 2:
            self.retrieveID()
        elif choice == 3:
            self.retrieveEmail()
        elif choice == 4:
            self.retrievePhone()
        elif choice == 5:
            self.getall()
    def insertRecord(self):
        '''
        petname = input("Enter the value for petname: ")
        species = input("Enter the value for species: ")
        breed = input("Enter the value for breed: ")
        ownername = input("Enter the value for Owner Name: ")
        ownerPN = int(input("Enter the value for Owner Phone Number: "))
        owneremail = input("Enter the value for Owner Email: ")
        ownerbalance = int(input("Enter the value for Owner Balance: "))
        firstvisit = input("Enter when the first visit was in format dd/mm/yyyy: ")
        '''

        petname = self.petnameEntry.get()
        self.petnameEntry.delete(0,'end')
        species = self.speciesEntry.get()
        self.speciesEntry.delete(0,'end')
        breed = self.breedEntry.get()
        self.breedEntry.delete(0,'end')
        ownername = self.ownernameEntry.get()
        self.ownernameEntry.delete(0,'end')
        ownerPN = self.ownerPNEntry.get()
        self.ownerPNEntry.delete(0,'end')
        owneremail = self.owneremailEntry.get()
        self.owneremailEntry.delete(0,'end')
        ownerbalance = self.balanceEntry.get()
        self.balanceEntry.delete(0,'end')
        firstvisit = self.visitEntry.get()
        self.visitEntry.delete(0,'end')

        query = f"insert into customers (petname,species,breed,ownername,ownerPN,owneremail,ownerbalance,firstvisit) values ('{petname}','{species}','{breed}','{ownername}','{ownerPN}','{owneremail}','{ownerbalance}','{firstvisit}');"
        self.cursor.execute(query)
        self.connection.commit()
        #self.selection()
    def retrieveID(self):
        #ID = int(input("Enter the ID you want to find: "))
        ID = self.entry.get()
        #print(ID)
        query = f"select * from customers where id=={ID}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.displayANGY.config(text=f"{result}")
        #print(result)
       # self.selection()
    def retrieveEmail(self):
        #email = str(input("Enter the Email you want to find: "))
        email = self.entry.get()
        query = f"select * from customers where owneremail='{email}'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.displayANGY.config(text=f"{result}")
        #print(result)

        #self.selection()
    def retrievePhone(self):
        #phone = int(input("Enter the Phone Number you want to find: "))
        phone = self.entry.get()
        #query = f"select * from customers where ownerPN=={phone}"
        self.cursor.execute(f"SELECT * FROM customers WHERE ownerPN={phone}")
        result = self.cursor.fetchall()
        self.displayANGY.config(text=f"{result}")

        #print(result)
       # self.selection()
    def getall(self):
        query = "select * from customers"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.display.config(text=f"{result}")
        '''
        self.display.config(text=f"{result[0]}\n")
        self.display.config(text=f"{result[2]}\n")
        self.display.config(text=f"{result[3]}\n")
        self.display.config(text=f"{result[4]}\n")
        self.display.config(text=f"{result[5]}\n")
        self.display.config(text=f"{result[6]}\n")
        self.display.config(text=f"{result[7]}\n")
        self.display.config(text=f"{result[8]}\n")
        #print(result)
        '''
        #self.selection()
main()