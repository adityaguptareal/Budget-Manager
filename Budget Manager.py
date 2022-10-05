salary=int(input("Enter your salary: "))   
#spend
if (salary<100000):
    expense=(salary*50/100)
    print("Your ideal monthly expense would be:",expense)
else:
    expense=(salary*20/100)
    print("Your ideal monthly expense would be:",expense)

#wants
wants=(salary*30/100)
print("Your Ideal amount for wants would be:",wants)
if (salary<100000):
    investment=(salary*20/100)
else:
    investment=(salary*50/100)
    
#investment
print("Your ideal investment amount would be:",investment)
print("investment Diversification")

#investment diversification
index_fund=(investment*50/100)
print("Index Fund:",index_fund)

us_investment=(investment*20/100)
print("Us Stocks:",us_investment)

indian_stocks=(investment*20/100)
print("Indian stock", indian_stocks)

Gold_bond=(investment*10/100)
print("Gold Bond:",Gold_bond)



