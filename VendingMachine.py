# In Class Assignment 1
# this file creates classes Coffee, Espresso, and Cappuccino using inheritance, and allows users to interact with "Vending Machine"

class Coffee:
    def __init__(self, sugar = 0, milk = 0):
        self.beverage = "Regular Coffee"
        self.sugar = sugar
        self.milk = milk
        self.price = 1.10

    def set_condiments(self, sugar = 0, milk = 0):
        if sugar >= 0  and milk >= 0:
            if sugar + milk <=3:
                self.sugar = sugar
                self.milk = milk

            else:
                print("Too much milk and sugar! Max 3 total")

        else:
            print("Cannot have negative milk or sugar")


    def condiment_price(self):
        return self.sugar * .1 + self.milk * .15

    def get_price(self):
        return self.price + self.condiment_price()

    def __str__(self):
        return "\nYour " + self.beverage + " costs $" + str(format(self.get_price(), ".2f"))


class Espresso(Coffee):
    def __init__(self, sugar = 0, milk = 0):
        super().__init__(sugar, milk)
        self.beverage = "Espresso"


    def get_price(self):
        return self.price * 1.20 + super().condiment_price()


class Cappuccino(Espresso):
    def __init__(self, sugar = 0, milk = 0):
        super().__init__(sugar, milk)
        self.beverage = "Cappuccino"

    def set_condiments(self, sugar, milk):

        if sugar != 0 or milk != 0:
            print("Cappuccinos cannot have milk or sugar. Set milk and sugar to 0.")

        else:
            self.sugar = sugar
            self.milk = milk


    def get_price(self):
        if self.sugar == 0 and self.milk == 0:
            return self.price * 1.15 * 1.2
        else:
            print("Cappuccinos cannot have milk or sugar. Set milk and sugar to 0.")

    def __str__(self):
        if self.sugar == 0 and self.milk == 0:
            return super().__str__()
        else:
            return "Cannot calculate cost for cappuccino. Set milk and sugar to 0."

class VendingMachine():
    def __init__(self):
        self.order = []
        self.order_number = 1
        self.vending_on = True

    def menu(self):
        print("\nHello Customer #", self.order_number, sep = "")

        print("\nHere is our menu:")
        print("Regular Coffee ... $1.10 \nEspresso ......... $1.32 \nCappuccino ....... $1.52")
        print("\nCondiments: \n- Sugar ... $0.10 / each \n- Milk .... $0.15 / each \n*** Machine Policy: Cappuccino may not add condiments.")

    def take_order(self):
        self.order_number = 1
        self.menu()
        print("Welcome to the Fully Automatic Beverage Vending Machine!")


        while self.vending_on:
            print("\nHello Customer #", self.order_number, sep = "")

            print("\nHere is our menu:")
            print("Regular Coffee ... $1.10 \nEspresso ......... $1.32 \nCappuccino ....... $1.52")
            print("\nCondiments: \n- Sugar ... $0.10 / each \n- Milk .... $0.15 / each \n*** Machine Policy: Cappuccino may not add condiments.")

            drink = input("\nWhat drink do you want? (Regular Coffee/Espresso/Cappuccino): ")
            while drink not in ["Regular Coffee", "Espresso","Cappuccino"]:
                drink = input("Please select a valid drink (Regular Coffee/Espresso/Cappuccino): ")

            if drink == "Regular Coffee" or drink == "Espresso":
                print("\nYou may add sugar or milk. Max 3 total condiments.")
                # do the sugar and the milk thing here lol
                sugar_input = int(input("How much sugar would you like? (0, 1, 2, 3): "))
                milk_input = int(input("How much milk would you like? (0, 1, 2, 3): "))
                total_cond = sugar_input + milk_input
                while sugar_input < 0 or milk_input < 0 or total_cond > 3:
                    if sugar_input < 0:
                        sugar_input = int(input("\nPlease input a non-negative sugar amount (0,1,2,3): "))

                    if milk_input < 0:
                        milk_input = int(input("Please input a non-negative milk amount (0,1,2,3): "))

                    if total_cond > 3:
                        print("\nYou have too many condiments! Max 3. Re-enter sugar and milk")
                        sugar_input = int(input("Please input valid sugar amount (0,1,2,3): "))
                        milk_input = int(input("Please input valid milk amount (0,1,2,3): "))

                    total_cond = sugar_input + milk_input

                sugar = sugar_input
                milk = milk_input


                if drink == "Regular Coffee":
                    my_drink = Coffee(sugar, milk)

                elif drink == "Espresso":
                    my_drink = Espresso(sugar, milk)

            elif drink == "Cappuccino":
                my_drink = Cappuccino(0,0)
                print("No condiments in Cappuccino... calculating price...")

            print(my_drink)
            ########## FINISH HERE



            next_order = input("\nWould you like to play another order? y/n: ")
            if next_order == "y":
                self.order_number += 1
            elif next_order == "n":
                self.vending_on = False
                print("\nGoodnight zzz")
            else:
                while next_order != "y" or next_order != "n":
                    if next_order == "y":
                        self.order_number += 1
                    elif next_order == "n":
                        self.vending_on = False
                        print("\nGoodnight zzz")

                    else:
                        next_order = input("\nWould you like to play another order? y/n: ")




def main():
    vending_machine = VendingMachine()
    vending_machine.take_order()


main()