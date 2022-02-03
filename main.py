import math as m


class Person:
    def __init__(self, name, ht, wt):
        self.name = name
        self.heigth=ht
        self.weight=wt

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    def get_bmi(self):
        bmi = self.weight / (self.heigth * self.heigth)
        return  bmi

    def wellcome_msg(self):
        return f"wellcome {self.name} and your height is {self.heigth} and weigth {self.weight}"


a_person = Person('bitue', 6, 90)
b_person = Person('farha', 5, 60)

print(b_person.wellcome_msg())
b_person.set_name('nazia')
print(b_person.get_bmi())

class Student(Person):
    def __init__(self,name, ht, wt, email, id ) :
        super().__init__(name,ht,wt)
        self.email=email
        self.student_id=id


    def get_summary(self):
        return f"name:{self.get_name()} and the bmi is {self.get_bmi()} and email {self.email}"



student = Student('ashik', 233, 900, 'ashik@gg.com', 121)

print(student.get_summary())









