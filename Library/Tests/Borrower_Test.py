import Borrower

class TestBookClass:

    def test_Create_Student_By_Constructor(self):
        borrower = Borrower.Borrower("Teststudent", 1, True, False)
        assert "Borrower Name: Teststudent" in  repr(borrower)
        assert "Borrower ID: 1" in repr(borrower)
        assert "Borrower is Student" in repr(borrower)
        assert "Borrower is Teacher" not in repr(borrower)
    
    def test_Create_Teacher_By_Constructor(self):
        borrower = Borrower.Borrower("TestTeacher", 1, False, True)
        assert "Borrower Name: TestTeacher" in  repr(borrower)
        assert "Borrower ID: 1" in repr(borrower)
        assert "Borrower is Student" not in repr(borrower)
        assert "Borrower is Teacher" in repr(borrower)

    def test_Create_Student_By_Class_Method(self):
        borrower = Borrower.Borrower.borrower_student("TestStudent", 1)
        assert borrower.is_student == True
        assert borrower.is_teacher == False

    def test_Create_Teacher_By_Class_Method(self):
        borrower = Borrower.Borrower.borrower_teacher("TestTeacher", 1)
        assert borrower.is_student == False
        assert borrower.is_teacher == True