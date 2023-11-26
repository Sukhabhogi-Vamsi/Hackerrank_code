class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1 = Student("Vamsi",239)
s2 = Student("Prince",200)
s1.show()
lap1 = Student.Laptop()
lap1.show()

