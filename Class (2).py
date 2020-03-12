class Student:
     def __init__ (self, clg = "Acropolis", id = 0):
          print("Clg: ", clg)
          print("ID: ", id)
     def getdata(self):
          self.Physics = int(input("Enter marks of Physics: "))
          self.Maths = int(input("Enter marks of maths: "))
          self.Chemistry = int(input("Enter marks of chemistry: "))
     def get_grades(self):
          print("Percent obtained are: ", (self.Physics+self.Maths+self.Chemistry)/3)

ob =Student()
ob.getdata()
ob.get_grades()
