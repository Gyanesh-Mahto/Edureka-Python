#Class Variable and Instance Variable:
#-------------------------------------#

class Edureka:                  #Defining a class Variable: Variable declared inside class are called as class Variable
    domain=("Data Science")     #domain:--> Class variable
    def Setcourse(self,name):
        self.name=name      #name:-->class variable
    def Print_Course(self):
        print("{}".format(self.name))

ob_1=Edureka()      #Defining an Instance of class Edureka: ob_1 and ob_2
ob_2=Edureka()

ob_1.Setcourse("Python")    #Instance Variable of object ob_1
ob_2.Setcourse("Machine Learning")

print(ob_1.domain)  #Data Science
ob_1.domain="GOD"
print(ob_1.domain)  #GOD            #Class variable is shared by both instances
print(ob_2.domain)  #Data Science

ob_1.Print_Course() #Python
ob_2.Print_Course() #Machine Learning