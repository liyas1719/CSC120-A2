from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory: list
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list, 
                 description: str, 
                 processor_type: str, 
                 hard_drive_capacity: int, 
                 memory: int, 
                 operating_system: str,
                 year_made: int,
                 price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        self.inventory = inventory

    def buy(self):
        if self.description in self.inventory:
            pass
        else:
            self.inventory.append(self.description)
    
        print (self.inventory)

def main():
    resale_shop = ResaleShop()


    
        # global itemID
        # itemID += 1 # increment itemID
        # inventory[itemID] = computer
        # return itemID

    # def update_price(self):
    #     if self.description in self.inventory:
    #         inventory[item_id]["price"] = new_price
    #     else:
    #         print("Item", item_id, "not found. Cannot update price.")
    
    # def sell(self):
    # if item_id in inventory:
    #     del inventory[item_id]
    #     print("Item", item_id, "sold!")
    # else: 
    #     print("Item", item_id, "not found. Please select another item to sell.")

    # def print_inventory():
    # # If the inventory is not empty
    # if inventory:
    #     # For each item
    #     for item_id in inventory:
    #         # Print its details
    #         print(f'Item ID: {item_id} : {inventory[item_id]}')
    # else:
    #     print("No inventory to display.")

    # def refurbish(self):
    #     if item_id in inventory:
    #         computer = inventory[item_id] # locate the computer
    #         if int(computer["year_made"]) < 2000:
    #             computer["price"] = 0 # too old to sell, donation only
    #         elif int(computer["year_made"]) < 2012:
    #             computer["price"] = 250 # heavily-discounted price on machines 10+ years old
    #         elif int(computer["year_made"]) < 2018:
    #             computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
    #         else:
    #             computer["price"] = 1000 # recent stuff

    #         if new_os is not None:
    #             computer["operating_system"] = new_os # update details after installing new OS
    #     else:
    #         print("Item", item_id, "not found. Please select another item to refurbish.")

    # def main():
    #     buy({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000})
    #     print_inventory()
    #     # What methods will you need?