class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):
    #classmethod na thakle e1 obj er jonno eta call korle shudhu oi obj er jonno e eta chng hobe. puro class er jonnoi company name chng korte chaile @classmethod use hobe. tokhon e1.changeCompany() dile oi obj er sathe sob obj er jonno e eta chng hobe. and classmethod dile first e instance(self) ney na. instead (cls) ney.
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
e2 = Employee()
e2.name = "Tonmoy"
e2.changeCompany("Google")
e2.show()

##Helo, hello mike testing...

print("hello")