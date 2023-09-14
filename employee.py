"""
  File: employee.py
  Description: This python file creates a class called employee with mulitple subcalsses 
  branching off of it to showcase inheritance.



  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 9/11/23
  Date Last Modified: 9/11/23

"""
class Employee:
    """
    Super class
    """

    def __init__(self, **kwargs):
        # Add your code here!
        self.name = kwargs.get("name")
        self.identifier = kwargs.get("identifier")
        self.salary = kwargs.get("salary")


    def __str__(self):
        # Add your code here!
        return "Employee \n" + str(self.name) + "," + str(self.identifier) + "," + str(self.salary)


############################################################
############################################################
############################################################

class PermanentEmployee(Employee):
    """ subclass of employee"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get("benefits")

    def cal_salary(self):
        """ this calculates salary based on what benefits"""
        if self.benefits == ["health_insurance"]:
            return self.salary * 0.9
        if self.benefits == ["retirement"]:
            return self.salary * 0.8
        if self.benefits == ["retirement", "health_insurance"]:
            return self.salary * 0.7
        return None


    def __str__(self):
        return "PermanentEmployee \n" + str(self.name) + "," + str(self.identifier) + \
            "," + str(self.salary) + "," + str(self.benefits)

############################################################
############################################################
############################################################

class Manager(Employee):
    """ subclass of employee"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get("bonus")

    def cal_salary(self):
        """ this calculates salary for the manager based on the bonus"""
        return float(self.salary + self.bonus)

    def __str__(self):
        return "Manager \n" + str(self.name) + "," + str(self.identifier) + \
            "," + str(self.salary) + "," + str(self.bonus)


############################################################
############################################################
############################################################

class TemporaryEmployee(Employee):
    """ subclass of employee"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get("hours")

    def cal_salary(self):
        """this calculates the salary based on hours"""
        return float(self.salary * self.hours)

    def __str__(self):
        return "TemporaryEmployee \n" + str(self.name) + "," + str(self.identifier) + \
            "," + str(self.salary) + "," + str(self.hours)


############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    """subclass of temporary employee which is a subclass of employee"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get("travel")

    def cal_salary(self):
        return float(self.salary * self.hours + self.travel * 1000)

    def __str__(self):
        return "Consultant \n" + str(self.name) + "," + str(self.identifier) + \
            "," + str(self.salary) + "," + str(self.hours) + "," + str(self.travel)
############################################################
############################################################
############################################################


class ConsultantManager(Manager, Consultant):
    """ subclass of both manager and consultant"""
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        Consultant.__init__(self, **kwargs)

    def cal_salary(self):
        return float(self.salary * self.hours + self.travel * 1000 + self.bonus)

    def __str__(self):
        return "ConsultantManager \n" + str(self.name) + "," + str(self.identifier) + \
            "," + str(self.salary) + "," + str(self.hours) + "," + str(self.travel) + \
                "\nConsultantManager \n" + str(self.name) + "," + str(self.identifier) + \
                    "," + str(self.salary) + "," + str(self.bonus)



############################################################
############################################################
############################################################





###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
    main()
