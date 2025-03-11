class Cash:
    available_money = 0
    
    def top_up(self, X):
        self.available_money += X
        
    def count_1000(self):
        print(self.available_money // 1000)
        
    def take_away(self, X):
        if self.available_money >= X:
            self.available_money -= X
        else:
            print("Ошибка: недостаточно денег в кассе")
            
cash = Cash()
cash.top_up(3500)
cash.take_away(1350)
cash.count_1000()
print(cash.available_money)