Gross = int(input("Please enter your gross profit: "))
Cost = int(input("Please enter your total cost: "))
Sales = int(input("Please enter your sales for the year: "))
Net = Gross - Cost
GPM = (Gross/Sales)*100
NPM = (Net/Sales)*100
print("Your Gross Profit Margin is: " , GPM , "%")
print("Your Net Profit Margin is: " , NPM , "%")
