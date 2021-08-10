#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("welcome to the tip calculator.")
Total_bill = input("What was the total bill? $")
Total_bill_USD = int(Total_bill)
#print(type(Total_bill_USD))

Tip = input("What percentage top would you like to give? 10, 12, or 15?")
#print(type(Tip))
Tip_USD = int(Tip)
Final_amount = Tip_USD/100 * Total_bill_USD + Total_bill_USD
#Tip1 = (Tip_USD + Total_bill_USD)
#print(type(Tip1))
#Final = Total_bill_USD + Tip1
People = input("How many people to split the bill?")
People_int = int(People)
#print(type(People_int))
PP = round(Final_amount/People_int, 2)
Per_person = input(f"Each person should pay: ${PP}")
#PP = int(Per_person)
#print(type(PP))


#print(type(Final_int))



