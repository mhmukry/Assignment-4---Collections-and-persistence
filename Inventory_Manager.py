import os.path
from Product import Product

class Inventory_Manager:
    def __init__(self, Product_list):
        self.Product = None
        self.Product_list = Product_list

  

    def add_Product(self, Product):
        self.Product_list.append(Product) 

    def view_Product(self):
        print(f'Id | Name | Amount')
        print(f'------------------')
        for productItem in self.Product_list:
            print(f'{productItem.productId} | {productItem.productName} | ${productItem.productAmount}')

    def edit_Product(self, productId_To_Edit, productName, productAmount):
        for productItem in self.Product_list:
            if productItem.productId == productId_To_Edit:
                productItem.productName = productName
                productItem.productAmount = productAmount


    def delete_Product(self, product, Product_list):
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
                productId = product_Line_List[0]
                productName = product_Line_List[1]
                productAmount = product_Line_List[2]
                self.product = Product(productId,productName, productAmount)
                self.Product_list.append(self.product) 
            product_File.close()

    def save_Product_Data_To_File(self):
        productFile = open("productFile.txt", "w")
        for productItem in self.Product_list:
            productFile.write(f'{productItem.productId},{productItem.productName},{productItem.productAmount} \n')
        productFile.close()

   
