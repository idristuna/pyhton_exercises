#! /usr/bin/python3

#using string.format to dispaly the data below 

totalMoney = int(input("Enter totalMoney"))
quantity = int(input("Enter quantitiy"))
price = int(input("Enter price"))

statement1 = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars "
print(statement1.format(totalMoney, quantity, price))
