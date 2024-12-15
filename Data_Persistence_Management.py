import os.path
import json
from Product import Product

class Data_Persistence_Management:
    def __init__(self, Product_list):
        self.Product = None
        self.Product_list = Product_list

  
    def load_Product_Data_From_File(self):

        if os.path.isfile("productFile.txt"):
            product_File = open("productFile.txt", "r")
            for product_line in product_File:  
                product_line = product_line.strip('\n')     
                product_Line_List=product_line.split(',')
                productId = int(product_Line_List[0])
                productName = product_Line_List[1]
                productAmount = float(product_Line_List[2])
                productInventory = int(product_Line_List[3])
                self.Product = Product(productId,productName, productAmount,productInventory)
                self.Product_list.append(self.Product) 
            product_File.close()
        return self.Product_list

    def save_Product_Data_To_File(self):
        first_line = 1
        productFile = open("productFile.txt", "w")
        for productItem in self.Product_list:
            if first_line == 1:
                 first_line += 1
                 productFile.write(f'{productItem.productId},{productItem.productName},{productItem.productAmount},{productItem.productInventory}')
            else:
                productFile.write(f'\n{productItem.productId},{productItem.productName},{productItem.productAmount},{productItem.productInventory}')
        productFile.close()
  
    def delete_product_list(self):
        self.Product_list = []
   
