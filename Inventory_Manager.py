import os.path
import json
from Product import Product

class Inventory_Manager:
    def __init__(self, Product_list):
        self.Product = None
        self.Product_list = Product_list

  

    def add_Product(self, Product):
        self.Product_list.append(Product) 
        return self.Product_list

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
        return self.Product_list

    def delete_Product(self, productId_To_Delete):
         for productItem in self.Product_list:
            if productItem.productId == productId_To_Delete:
                self.Product_list.remove(productItem)

    def delete_product_list(self):
        self.Product_list = []


   
