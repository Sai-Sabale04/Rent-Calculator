rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of food ordered ="))
water_bill = int(input("Enter the amount of water bill = "))
electricity_spend =int(input("Enter the total of electricity spend ="))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in flat = "))

Total_bil = electricity_spend * charge_per_unit

Ouput = (food + rent + Total_bil) //  persons
print("Each Person will pay = ", Ouput)