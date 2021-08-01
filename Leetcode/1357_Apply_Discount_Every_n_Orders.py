from typing import List

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.prices = dict(zip(products, prices))
        self.cnt = 0
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt += 1
        bill = sum([self.prices[p] * a for p, a in zip(product, amount)])
        if self.cnt % self.n == 0:
            bill -= (self.discount * bill) / 100
        
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)