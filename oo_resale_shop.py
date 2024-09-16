from computer import Computer, main


class ResaleShop:
    #computer_info: list
    inventory: list
    new_price: int
    new_operating_system: int

    def __init__ (self,
                #computer_info: list,
                inventory: list,
                new_price: int,
                new_operating_system: int):
        #self.computer_info = computer_info
        self.inventory = inventory
        self.new_price = new_price
        self.new_operating_system = new_operating_system
        #self.computer_info = Computer

    def buy(self, computer):
        if computer in self.inventory:
            pass
        else:
            print(self.inventory)
            self.inventory.append(computer)
            # self.inventory.append([computer.description, 
            #                        computer.processor_type, 
            #                        computer.hard_drive_capacity, 
            #                        computer.memory,
            #                        computer.operating_system,
            #                        computer.year_made,
            #                        computer.price])
            print ("Added ", computer.description, "to inventory")

    def update_price(self, computer):
        if computer in self.inventory:
            computer.price = self.new_price
            print (computer.description, "price now $", computer.price)
        else:
            print("Item", computer.description, "not found. Cannot update price.")

    def sell(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item", computer.description, "sold!")
        else: 
            print("Item", computer.description, "not found. Please select another item to sell.")
    
    def print_inventory(self):
        if self.inventory:
            print("Inventory currently contains:")
            for computer in self.inventory:
                print(computer.description, 
                        computer.processor_type, 
                        computer.hard_drive_capacity, 
                        computer.memory,
                        computer.operating_system,
                        computer.year_made,
                        computer.price)
        else:
            print("No inventory to display.")
    
    def refurbish(self, computer):
        if computer in self.inventory:
            if computer.year_made < 2000:
                computer.price = 0 # too old to sell, donation only
                print (computer.description, "price is now", computer.price)
            elif computer.year_made < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
                print (computer.description, "price is now", computer.price)
            elif computer.year_made < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
                print (computer.description, "price is now", computer.price)
            else:
                computer.price = 1000 # recent stuff
                print (computer.description, "price is now", computer.price)

            if computer.operating_system is not 0:
                computer.operating_system =  self.new_operating_system # update details after installing new OS
                print (computer.description, "OS updated to", self.new_operating_system)
        else:
            print("Item", computer.description, "not found. Please select another item to refurbish.")


def main():
    
    computer1 = Computer( [],
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500, 
    )    # What methods will you need?
    resaleshop = ResaleShop([], 2000, 1)
    resaleshop.buy(computer1)
    resaleshop.update_price(computer1)
    #resaleshop.sell(computer1)
    resaleshop.print_inventory()
    resaleshop.refurbish(computer1)
    computer2 = Computer( [],
        "Mac Air (2020)",
        "3.5 GHc 6-Core Intel Xeon E5",
        3065, 125,
        "macOS Big Sur", 2020, 3000, 
    )    # What methods will you need?
    resaleshop.buy(computer2)
    resaleshop.update_price(computer2)
    resaleshop.sell(computer2)
    resaleshop.print_inventory()
    resaleshop.refurbish(computer2)


    #print(Computer.description)

#only call main() if i am running this program directly
if __name__ == "__main__":
    main()
    # What attributes will it need?
    # inventory: list
    # description: str
    # processor_type: str
    # hard_drive_capacity: int
    # memory: int
    # operating_system: str
    # year_made: int
    # price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # def __init__(self, inventory: list, 
    #              description: str, 
    #              processor_type: str, 
    #              hard_drive_capacity: int, 
    #              memory: int, 
    #              operating_system: str,
    #              year_made: int,
    #              price: int):
    #     self.description = description
    #     self.processor_type = processor_type
    #     self.hard_drive_capacity = hard_drive_capacity
    #     self.memory = memory
    #     self.operating_system = operating_system
    #     self.year_made = year_made
    #     self.price = price
    #     self.inventory = inventory

#     def print_inventory():
#     # If the inventory is not empty
#     if inventory:
#         # For each item
#         for item_id in inventory:
#             # Print its details
#             print(f'Item ID: {item_id} : {inventory[item_id]}')
#     else:
#         print("No inventory to display.")

#     def refurbish(self):
#         if item_id in inventory:
#             computer = inventory[item_id] # locate the computer
#             if int(computer["year_made"]) < 2000:
#                 computer["price"] = 0 # too old to sell, donation only
#             elif int(computer["year_made"]) < 2012:
#                 computer["price"] = 250 # heavily-discounted price on machines 10+ years old
#             elif int(computer["year_made"]) < 2018:
#                 computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
#             else:
#                 computer["price"] = 1000 # recent stuff

#             if new_os is not None:
#                 computer["operating_system"] = new_os # update details after installing new OS
#         else:
#             print("Item", item_id, "not found. Please select another item to refurbish.")

#     def main():
#         buy({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000})
#         print_inventory()
#         # What methods will you need?

# def main():
#     resale_shop = ResaleShop()