import Book
import Borrower

idCounter = 1
availableBooks = []
borrowers = []
borrowCounter = 0
funds = 0
powerOn = True


def Menu_choices():
    while powerOn:

        print("#1 Add borrower")
        print("#2 Add Book")
        print("#3 Rent a book")
        print("#4 Return a book")
        print("#5 Show all existing books")
        print("#6 Generate report")
        print("#7 Quit")

        choice = int(input("\nPlease chose one option above and type its number below:\nAnswer: "))

        match choice:
            case 1:
                Add_Borrower()
            case 2:
                AddBook()
            case 3:
                raise Exception("Not implemented yet")
            case 4:
                raise Exception("Not implemented yet")
            case 5:
                DisplayAllExistingBooks()
            case 6: 
                GenerateReport()
            case 7:
                powerOn = False


def Add_Borrower():
    id = idCounter
    name = input("\nPlease type in a name for the borrower.\nAnswer: ")

    borrowerType = input("\nPlease type in wich borrower type you want to create. (student/teacher)\nAnswer: ")

    if(borrowerType.lower() == "student"):
        newBorrower = Borrower.Borrower.borrower_student(name, id)
    else:
        newBorrower = Borrower.Borrower.borrower_teacher(name, id)
    
    borrowers.append(newBorrower)
    idCounter + 1

    showMenuAgain = input("Do you want to go back to the menu? (yes/no)\nAnswer: ")

    if(showMenuAgain == "no"):
        powerOn = False

def AddBook():

    title = input("\nPlease type in the title for the book.\nAnswer: ")
    auther_name = input("\nPlease type in the authers name.\nAnswer: ")
    isbn = input("\nPlease type in the isbn number for the new book.\nAnswer: ")

    bookType = input("\nPlease type in wich book type you want to create. (Literature/Science/Entertainment)\nAnswer: ")
    if(bookType.lower() == "literature"):
        newBook = Book.Book.literature_book(title, auther_name, isbn)

    if(bookType.lower() == "literature"):
        newBook = Book.Book.Science_book(title, auther_name, isbn)

    else:
        newBook = Book.Book.Entertainment_book(title, auther_name, isbn)
    
    availableBooks.append(newBook)

    showMenuAgain = input("Do you want to go back to the menu? (yes/no)\nAnswer: ")
    
    if(showMenuAgain == "no"):
        powerOn = False
        


# def RentBook():
#     bookTitle = input("Please type in the title of the book that you want to rent.")

def DisplayAllExistingBooks():
    for index, book in enumerate(availableBooks):
        # if(index == 0):
        #     print(f"\n\n{books}")
            
        # else:
        print(book)

    showMenuAgain = input("Do you want to go back to the menu? (yes/no)\nAnswer: ")

    if(showMenuAgain == "no"):
        powerOn = False

def GenerateReport():
    print("Here is an overall report over following:")
    print(f"\n\n Funds collected: {funds}kr")
    print(f"\n\n Total amount of books available in the library: {len(availableBooks)}")
    print(f"\n\n How many books that was borrowed: {borrowCounter}")

    showMenuAgain = input("Do you want to go back to the menu? (yes/no)\nAnswer: ")

    if(showMenuAgain == "no"):
        powerOn = False



Menu_choices()