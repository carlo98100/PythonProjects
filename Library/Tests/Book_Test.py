import datetime
import Book
import pytest

class TestBookClass:

    def test_Create_a_Book_By_Constructor(self):
        book = Book.Book("Testboken", "TestFörfattaren", "2222222", "Literature")

        assert "Testboken" in repr(book)
        assert "TestFörfattaren" in repr(book)
        assert "2222222" in repr(book)
        assert "Literature" in repr(book)

    def test_Create_a_Litterature_Book_By_Class_Method(self):
        litteratureBook = Book.Book.literature_book("Testboken", "TestFörfattaren", "2222222")

        assert "Testboken" in repr(litteratureBook)
        assert "TestFörfattaren" in repr(litteratureBook)
        assert "2222222" in repr(litteratureBook)
        assert "Literature" in repr(litteratureBook)

    def test_Create_a_Sience_Book_By_Class_Method(self):
        sienceBook = Book.Book.Science_book("Testboken", "TestFörfattaren", "2222222")

        assert "Testboken" in repr(sienceBook)
        assert "TestFörfattaren" in repr(sienceBook)
        assert "2222222" in repr(sienceBook)
        assert "Science" in repr(sienceBook)

    def test_Create_a_Entertainment_Book_By_Class_Method(self):
        entertainmentBook = Book.Book.Entertainment_book("Testboken", "TestFörfattaren", "2222222")
        
        assert "Testboken" in repr(entertainmentBook)
        assert "TestFörfattaren" in repr(entertainmentBook)
        assert "2222222" in repr(entertainmentBook)
        assert "Entertainment" in repr(entertainmentBook)

    def test_is_Book_available(self):
        book = Book.Book("Testboken", "TestFörfattaren", "2222222", "Literature")
        assert book.is_available() == True
    
    def test_Borrow_Book_That_Is_Available(self): 
        book = Book.Book("Testboken", "TestFörfattaren", "2222222", "Literature")
        assert book.borrow_book(4) == True

    # def test_Borrow_Book_That_Is_Not_Available(self): 
    #     entertainmentBook = Book.Book.Entertainment_book("Testboken", "TestFörfattaren", "2222222")
    #     assert entertainmentBook.borrow_book(4) == True
        
    #     with pytest.raises(Exception) as exception:
    #         entertainmentBook.borrow_book(4)
    #         assert "HEJ" in str(exception.value)

    def test_Return_Book(self):
        book = Book.Book("Testboken", "TestFörfattaren", "2222222", "Literature")
        book.return_book()
        assert book.status_week == datetime.date.today().isocalendar()[1]