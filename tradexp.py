current_stock_price = 100
company_stocks = 100
my_stocks = 0
my_money = 0

def log():
    global company_stocks, my_stocks
    return "Company Stocks: " + str(company_stocks) + " | Current Stock Value: $" + str(current_stock_price) + " | My Stocks: " + str(my_stocks) + " | My Money: $" + str(my_money)

def borrow_stock(amount):
    global company_stocks, my_stocks, my_money
    if company_stocks < amount:
        print(log(), "- There is no enough stocks in the company")

    else:
        company_stocks -= amount
        my_stocks += amount
        print(log(), "- Borrowing Completed!")

def return_stock(amount):
    global company_stocks, my_stocks, my_money
    if my_stocks <= 0:
        print(log(), "- There is no enough stocks in the my account")
    else:
        my_stocks -= amount
        company_stocks += amount
        print(log(), "- Returning Completed!")

def sell_stocks(amount):
    global my_stocks, my_money, current_stock_price
    if my_stocks <= 0:
        print(log(), "- There is no enough stocks in the my account")
    else:
        my_stocks -= amount
        my_money = amount * current_stock_price
        print(log(), "- Selling Completed!")


def buy_stocks(amount):
    global my_stocks, my_money, current_stock_price
    if my_money < current_stock_price:
        print(log(), "- There is no enough money in the my account")
    else:
        my_money -= amount * current_stock_price
        my_stocks += amount
        print(log(), "- Buying Stocks Completed!")
    
print(log())
borrow_stock(1)
sell_stocks(1)

# Changed the market price
current_stock_price = 60

buy_stocks(1)
return_stock(1)