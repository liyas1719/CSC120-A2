from computer import Computer, main


class ResaleShop:
    inventory: list
    new_price: int
    new_operating_system: int

    def __init__ (self,
                inventory: list,
                new_price: int,
                new_operating_system: int):
        self.inventory = inventory
        self.new_price = new_price
        self.new_operating_system = new_operating_system

    def buy(self, computer):
        if computer in self.inventory:
            pass
        else:
            self.inventory.append(computer)
            print ("Added ", computer.description, "to inventory!")

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

            if computer.operating_system != 0:
                computer.operating_system =  self.new_operating_system # update details after installing new OS
                print (computer.description, "OS updated to", self.new_operating_system)
        else:
            print("Item", computer.description, "not found. Please select another item to refurbish.")


def main():
    
    computer1 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500, 
    )    # What methods will you need?
    resaleshop = ResaleShop([], 2000, 1)
    resaleshop.buy(computer1)
    resaleshop.update_price(computer1)
    resaleshop.sell(computer1)
    resaleshop.print_inventory()
    resaleshop.refurbish(computer1)
    computer2 = Computer(
        "Mac Air (2020)",
        "3.5 GHc 6-Core Intel Xeon E5",
        3065, 125,
        "macOS Big Sur", 2020, 3000, 
    )    # What methods will you need?=
    resaleshop.buy(computer2)
    resaleshop.update_price(computer2)
    resaleshop.sell(computer2)
    resaleshop.print_inventory()
    resaleshop.refurbish(computer2)

#only call main() if i am running this program directly
if __name__ == "__main__":
    main()