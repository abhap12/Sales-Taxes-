# Defining a class to calculate price based on the typr of product
import math
class product:

    # Init function having a product information
    def __init__(self,prod_info):

        self.prod_info = prod_info
        self.quantity = int(prod_info[0])
        self.tax=0
        self.imptax = 0
        self.idx = self.prod_info.find('at ')
    
    # Function to calculate sales tax on certain typr of products at the rate of 10%
    def sale_tax(self):

        if 'book' in self.prod_info or 'chocolate' in self.prod_info or 'chocolates' in self.prod_info or 'food' in self.prod_info or 'pills' in self.prod_info :
            self.tax = 0
            
        else:
            self.tax = 10 * self.quantity * float(self.prod_info[ self.idx + 3 : ]) / 100
            self.tax = round(math.ceil(self.tax / 0.05) * 0.05, 2)
        
        return self.tax

    # Function to calculate additional tax on imported products at the rate of 5%
    def imported(self):

        if 'imported' in self.prod_info:
            self.imptax = 5 * self.quantity * float(self.prod_info[self.idx + 3 : ]) / 100
            self.imptax = round(math.ceil(self.imptax / 0.05) * 0.05, 2)
        else:
            self.imptax = 0
            
        return self.imptax

    #Function to extract price from the product information
    def price(self):

        return float(self.prod_info[self.idx + 3 : ]) * self.quantity
        
for i in range(int(input('Enter total number of receipts : '))):
    tax = 0
    total = 0
    products_lst = []
    price = []
    
    for _ in range(int(input('Enter the total number of different products for receipt ' + str(i+1) + ' : '))):
        prod = input()
        products_lst.append(prod)
        p1 = product(prod)
        price.append(round(p1.sale_tax() + p1.imported()+p1.price(),2))
        tax += p1.sale_tax() + p1.imported()
        total += p1.price()
    
    print()
    print('Output ' + str(i+1))
    k=0
    for p in products_lst:
        index = p.find('at ')
        print(p[ : index] + ': ' + str(price[k]))
        k+=1

    print('Sales Taxes: ' + str(round(tax,2)))
    print('Total: ' + str(round((total + tax),2)))
    print()





