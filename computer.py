class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # computer_info: list
    # inventory: list


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                    description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int,
                    # computer_info: list,
                    # inventory: list
                    ):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        # self.computer_info = computer_info
        # self.inventory = inventory

    # def buy(self):
    #     if self.computer_info in self.inventory:
    #         pass
    #     else:
    #         self.inventory.append(self.computer_info)
    
    #     print (self.inventory)

def main():
    
    # First, let's make a computer
    computer = Computer( [],
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500, 
    )    # What methods will you need?
    # computer.buy()
    print(computer.description)

#only call main() if i am running this program directly
if __name__ == "__main__":
    main()