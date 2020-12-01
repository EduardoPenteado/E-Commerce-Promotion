#!/usr/bin/env python
# coding: utf-8

# In[147]:


from pandas import read_excel

class Promotion:
    
    def __init__(self, client, product, price, quantity, frete, prime):
        promo = []
        self.client = client
        self.product = product
        self.price = price
        self.quantity = quantity
        self.frete = frete
        self.prime = prime
        self.promo = promo
        
    def total(self):
        return round(self.price * self.quantity,2)
    
    def __str__(self):
        return self.client

    def due(self):
        if len(self.promo) == 0:
            print('Discount: '+str(0*100)+' %')
            print('Total: R$ '+str(round(self.frete+self.total(),2)))
        else:
            print('Discount: '+str(max(self.promo)*100)+' %')
            print('Total: R$ '+str(round(self.frete + self.total() - self.total()*max(self.promo),2)))
    
    def discount(self, promotion):
        return self.promo.append(promotion)
    
    def promo_quantity(self):
        # Discount of 15 % if you buy at least 5.
        promotion = 0
        if self.quantity >= 5:
            promotion = 0.15
        return self.discount(promotion)

    def promo_total(self):
        # Discount of 30 % if the total is more or equal to 300.
        promotion = 0
        if self.total() >= 300:
            promotion = 0.3
        return self.discount(promotion)
    
    def free_shipping(self):
        # The shipping is free to a total of at least R$ 300.00
        # Or, the shipping is free if the user is Prime
        if self.total() >= 300 or self.prime == 'YES':
            self.frete = 0
            print("|Free shipping|")
        return self.frete
    
    def product_discount(self):
        # Plus of a 5 % of discount if have a specific produt
        # In the example I'll use Jeans as the product
        if self.product == 'Jeans':
            if len(self.promo) == 0:
                self.promo.append(0.05)
            else:
                for promo in range(0, len(self.promo)):
                    self.promo[promo] += 0.05
        return self.promo
        
    def main(self):
        print('Product: '+self.product)
        print('Quantity: '+str(self.quantity))
        print('Total: R$ '+str(self.total()))
        self.free_shipping()
        print('Frete: R$ '+str(self.frete))
        self.promo_quantity()
        self.promo_total()
        self.product_discount()
        self.due()
        
if __name__ == '__main__':
    df = read_excel('Promotion.xlsx')
    for i in range(0, len(df)):
        promotion = Promotion(df.loc[i][0], df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4], df.loc[i][5])
        print('Client: '+str(promotion))
        promotion.main()
        print('-'*20)

