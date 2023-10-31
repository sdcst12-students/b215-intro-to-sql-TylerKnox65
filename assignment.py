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
class main():
    def __init__(self) -> None:
        file = 'dbaseVet.db'
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
        self.cursor.execute(query)
        self.selection()

    def selection(self):
        while True:
            try:
                choice = int(input("Welcome to database editor, you can insert a new record (1), retrieve a record by their id (2), retrieve a record by the email (3), retrieve a record by phone number (4), or retrieve all (5): "))
                break
            except:
                print("Enter a valid selection")

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
        petname = input("Enter the value for petname: ")
        species = input("Enter the value for species: ")
        breed = input("Enter the value for breed: ")
        ownername = input("Enter the value for Owner Name: ")
        ownerPN = int(input("Enter the value for Owner Phone Number: "))
        owneremail = input("Enter the value for Owner Email: ")
        ownerbalance = int(input("Enter the value for Owner Balance: "))
        firstvisit = input("Enter when the first visit was in format dd/mm/yyyy: ")
        query = f"insert into customers (petname,species,breed,ownername,ownerPN,owneremail,ownerbalance,firstvisit) values ('{petname}','{species}','{breed}','{ownername}','{ownerPN}','{owneremail}','{ownerbalance}','{firstvisit}');"
        self.cursor.execute(query)
        self.connection.commit()
        self.selection()
    def retrieveID(self):
        ID = int(input("Enter the ID you want to find: "))
        query = f"select * from customers where id=={ID}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)
        self.selection()
    def retrieveEmail(self):
        email = str(input("Enter the Email you want to find: "))
        query = f"select * from customers where owneremail='{email}'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)
        self.selection()
    def retrievePhone(self):
        phone = int(input("Enter the Phone Number you want to find: "))
        #query = f"select * from customers where ownerPN=={phone}"
        self.cursor.execute(f"SELECT * FROM customers WHERE ownerPN={phone}")
        result = self.cursor.fetchall()
        print(result)
        self.selection()
    def getall(self):
        query = "select * from customers"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)
        self.selection()
main()