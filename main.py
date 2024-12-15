import os.path
from Product import Product
from Inventory_Manager import Inventory_Manager
from Data_Persistence_Management import Data_Persistence_Management

class Main:
    def __init__(self):
        self.Product = None
        self.Product_list =[]
        self.Inventory_Manager = None
        self.Data_Persistence_Management = None

    def showMainMenu(self):
        run_Menu = 1
        self.Inventory_Manager = Inventory_Manager(self.Product_list)
        self.Data_Persistence_Management = Data_Persistence_Management(self.Product_list)
        self.Product_list = self.Data_Persistence_Management.load_Product_Data_From_File()

           
        while (run_Menu == 1):
            #self.clear_console()
            print("Please select your choices: ")
            print("1: Add product")
            print("2: Read product")
            print("3: Edit product")
            print("4: Delete product")
            print("5: Exit")
            choice = self.get_user_input_integer("Select your choice: ",  1,  5)
            if choice == 1:
                 self.choice_add_Product()
                 print("Add product")
                 
            if choice == 2:
                self.choice_view_Product()
                print("View product")
                
            if choice == 3:
                self.choice_edit_Product()
                print("Update product")
                
            if choice == 4:
                self.choice_delete_Product()
                print("Delete product")

            if choice == 5:
                self.Data_Persistence_Management.save_Product_Data_To_File()
                print("Product information saved successfully before exit")
                run_Menu = 0
                self.Product_list = []
                self.Inventory_Manager.delete_product_list()
                self.Data_Persistence_Management.delete_product_list()

    def choice_add_Product(self):
        if len(self.Product_list) == 0:
            productId = 1
        elif len(self.Product_list) > 0:
            productId= self.Product_list[len(self.Product_list)-1].productId + 1

        productName = input("Please Enter Product Name: ")
        productAmount = self.get_user_input_float( "Enter Product Amount (0.01-1000):  ",  0.01,  1000.00)
        productInventory = self.get_user_input_integer( "Enter Product Inventory (1-1000):  ",  1,  1000)
        self.Product = Product(productId,productName, productAmount,productInventory)
        self.Inventory_Manager.add_Product(self.Product)

    def choice_view_Product(self):
       self.Inventory_Manager.view_Product()

    def choice_edit_Product(self):
        self.choice_view_Product()

        productId_To_Edit = self.get_user_input_integer("Enter product ID to edit: ",  0,  100000)
        productName = input("Please Enter Product Name: ")
        productAmount = self.get_user_input_float( "Enter Product Amount (0.01-1000):  ",  0.01,  1000.00)
        productInventory = self.get_user_input_integer( "Enter Product Inventory (1-1000):  ",  1,  1000)
        self.Inventory_Manager.edit_Product(productId_To_Edit, productName, productAmount,productInventory)
        print(f'productId:{productId_To_Edit} Edited')
        self.choice_view_Product()

    def choice_delete_Product(self):
        self.choice_view_Product()

        productId_To_Delete = self.get_user_input_integer("Enter product ID to delete: ",  0,  100000)
        self.Inventory_Manager.delete_Product(productId_To_Delete)
        print(f'productId:{productId_To_Delete} deleted')
        self.choice_view_Product()

    def get_user_input_float(self,  input_str,  min_value,  max_value):
        while (1):
            try:
                input_float = float(input(input_str))
                if ((input_float >= min_value) and (input_float <= max_value)):
                    return input_float
                else:
                    print("Incorrect value")  
            except:
                print("Incorrect data type") 

    def get_user_input_integer(self,  input_str,  min_value,  max_value):
        while (1):
            try:
                input_integer = int(input(input_str))
                if ((input_integer >= min_value) and (input_integer <= max_value)):
                    return input_integer
                else:
                    print("Incorrect value")  
            except:
                print("Incorrect data type")               

    def clear_console(self):
        print("\033[H\033[2J", end="")

    def run(self):
        run_program = 1
        while (run_program == 1):
            self.clear_console()
            print("1: Show Main Menu")
            print("2: Exit")
            choice = self.get_user_input_integer("Select your choice: ",  1,  2)
            if choice == 1:
                self.showMainMenu()
            else:
                run_program=0

if __name__ == "__main__":
    app = Main()
    app.run()

