import os.path
from Product import Product
from Inventory_Manager import Inventory_Manager

class Main:
    def __init__(self):
        self.Product = None
        self.Product_list =[]
        self.Inventory_Manager = Inventory_Manager(self.Product_list)

    def showMainMenu(self):
        run_Menu = 1
        self.load_Product_Data_From_File()
           
        while (run_Menu == 1):
            #self.clear_console()
            print("Please select your choices: ")
            print("1: Add product")
            print("2: Read product")
            print("3: Edit product")
            print("4: Delete product")
            print("5: Exit")
            choice = int(input("Select your choice: "))
            if choice == 1:
                 self.add_Product()
                 print("Add product")
                 
            if choice == 2:
                self.view_Product()
                print("View product")
                
            if choice == 3:
                self.edit_Product()
                print("Update product")
                
            if choice == 4:
                self.delete_Product()
                print("Delete product")

            if choice == 5:
                self.save_Product_Data_To_File()
                print("Product information saved successfully before exit")
                run_Menu = 0
                self.Product_list = []

    def add_Product(self):
        productId=len(self.Product_list)
        productName = input("Please Enter Product Name: ")
        productAmount = self.get_user_input_float( "Enter Product Amount (0.01-1000):  ",  0.01,  1000.00)
        self.Product = Product(productId,productName, productAmount)
        self.Inventory_Manager.add_Product(self.Product)

    def view_Product(self):
       self.Inventory_Manager.view_Product()

    def edit_Product(self):
        self.view_Product()

        productId_To_Edit = int(input("Enter product ID to edit: "))
        productName = input("Please Enter Product Name: ")
        productAmount = self.get_user_input_float( "Enter Product Amount (0.01-1000):  ",  0.01,  1000.00)
  
        self.Inventory_Manager.edit_Product(productId_To_Edit, productName, productAmount)
        print(f'productId:{productId_To_Edit} Edited')
        self.view_Product()

    def delete_Product(self):
        self.view_Product()

        productId_To_Delete = int(input("Enter product ID to delete: "))
        for productItem in self.Product_list:
            if productItem.productId == productId_To_Delete:
                self.Product_list.remove(productItem)
        print(f'productId:{productId_To_Delete} deleted')
        self.view_Product()

    def load_Product_Data_From_File(self):

        if os.path.isfile("productFile.txt"):
            product_File = open("productFile.txt", "r")
            for product_line in product_File:           
                product_Line_List=product_line.split(',')
                print(f'{product_Line_List[0]}')
                productId = product_Line_List[0]
                productName = product_Line_List[1]
                productAmount = product_Line_List[2]
                self.Product = Product(productId,productName, productAmount)
                self.Product_list.append(self.Product) 
            product_File.close()

    def save_Product_Data_To_File(self):
        productFile = open("productFile.txt", "w")
        for productItem in self.Product_list:
            productFile.write(f'{productItem.productId},{productItem.productName},{productItem.productAmount} \n')
        productFile.close()

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
                

    def clear_console(self):
        print("\033[H\033[2J", end="")

    def run(self):
        run_program = 1
        while (run_program == 1):
            self.clear_console()
            print("1: show Main Menu")
            print("2: Exit")
            choice = int(input("Select your choice: "))
            if choice == 1:
                self.showMainMenu()
            else:
                run_program=0




if __name__ == "__main__":
    app = Main()
    app.run()

