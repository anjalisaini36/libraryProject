class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t ***"+book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry,this book has alreasy been issued to someone else.Please wait until the book is returned.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")
    

class Student:
    def requestBook(self):
        self.book=input("enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book=input("enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary=Library(["Python Notes","C","C++","Java","HTML","CSS","Flask","Django"])
    student=Student()
    centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg='''####Welcome to Central Library####
        please choose an option:
        1. listing all the books 
        2. request a book
        3.return a book
        4. exit the library'''

        print(welcomeMsg)

        a=int(input("Enter a choice: "))
        if a== 1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Central library. Have a gread day ahead!")
            exit()
        else:
            print("Invalid Choice!")
        



