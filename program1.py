'''Write a Python program that takes the prices of 3 food items and the total number of
 friends as inputs. It must calculate the total food bill, add an 18% GST tax, 
 how much each friend needs to pay, and finally check if the total bill is greater than ₹1500
 to determine premium discount eligibility'''

food1= int(input("Enter the price of first food: " ))
food2= int(input("Enter the price of second food: " ))
food3= int(input("Enter the price of third food: " ))

total_friends= int(input("Enter the number of friends: "))

bill_without_gst=food1+food2+food3

final_bill = bill_without_gst + 0.18*(bill_without_gst)

print("Your total bill is (gst included 18%): ",final_bill)
print("Each Friend has to pay: ",final_bill / total_friends)
print("Eligible For special Discount:", final_bill>1500 )