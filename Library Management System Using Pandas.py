import pandas as pd
import datetime

class LibraryManagementSystem:
    def __init__(self) -> None:
        self.users = None
        self.data = None

    def decision(self):
        self.library_data = pd.read_csv("library_data.csv")
        self.library_users = pd.read_csv("library_users.csv")
        print("Type an option from the following choice")
        print("1. View User List\n2. View User, Book List\n3. Take a book\n4. Return Book\n5. Exit")
        choice = int(input("Choice?: "))
        if choice == 1:
            self.userList()

        elif choice == 2:
            self.userBookList()

        elif choice == 3:
            self.userBookRegister()

        elif choice == 4:
            self.returnBook()

        elif choice == 5:
            exit()

        else:
            print("That choice is currently unavailable")

    def userList(self):
        print(self.library_users)
        self.decision()

    def userBookList(self):
        print(self.library_data)
        self.decision()

    def userBookRegister(self):
        username = input("Enter users name: ").upper()
        bookname = input("Enter books name: ").upper()
        userBookFrameCreate = {
            'NAME': [username],
            'BOOK': [bookname],
            'TAKEN': datetime.date.today(),
        }
        userFrameCreate = {
            'NAME': [username],
        }
        # 
        # User, Book register part
        hasUserBook = 0
        for items in range(len(self.library_data)):
            if(self.library_data["NAME"][items] == username and self.library_data["BOOK"][items] == bookname):
                hasUserBook = 1
        if(hasUserBook == 0):
            userBookFrameUpload = pd.DataFrame(userBookFrameCreate)
            userBookFrameUpload.to_csv("library_data.csv", mode="a", index=False, header=False, lineterminator="\n", sep=',')
            print(f"Book: {bookname} has been registered for User: {username}")
        else:
            print(f"User: {username} has already taken the book: {bookname}")
        
        # 
        # User Register Part
        hasUser = 0
        for items in self.library_users["NAME"]:
            # print(items)
            if(items == username):
                hasUser = 1
        if(hasUser == 0):
            userFrameUpload = pd.DataFrame(userFrameCreate)
            userFrameUpload.to_csv("library_users.csv", mode="a", index=False, header=False, lineterminator="\n")
        else:
            print(f"User: {username} already exists")
        self.decision()

    def returnBook(self):
        username = input("Enter Users' name: ").upper()
        bookname = input("Enter books' name: ").upper()
        for items in range(len(self.library_data)):
            if(self.library_data["RETURNED"] is not None):
                if(self.library_data["NAME"][items] == username and self.library_data["BOOK"][items] == bookname):
                    self.library_data.loc[items,'RETURNED'] = datetime.date.today()
                    # Calculate the number of days taken
                    checkdate = datetime.datetime.strptime(str(self.library_data.loc[items,'RETURNED']), "%Y-%m-%d")
                    days = (checkdate - datetime.datetime.strptime(self.library_data.loc[items,'TAKEN'], "%Y-%m-%d")).days
                    self.library_data.loc[items,'DAYS TAKEN'] = days
                    if(days > 30):
                        self.library_data.loc[items,'FINED'] = "YES"
                        print(f"{username} should pay fine")
                    else:
                        self.library_data.loc[items,'FINED'] = "NO"
                        print(f"{username} is not fined")
                    self.library_data.to_csv("library_data.csv", index=False)
        self.decision()
    

diwas = LibraryManagementSystem()
diwas.decision()