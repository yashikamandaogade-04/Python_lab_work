#vendor's detail
name=input("Enter Vendor Name: ")
year=int(input("Enter Year of Association: "))
contact=int(input("Enter Contact Number: "))
email=input("Enter Email ID: ")
total=0
print("\nEnter monthly purchase amounts:")
#Purchases for 12 months
for i in range(12):
    amount=float(input("Month purchase: "))
    total+=amount
print("\nAnnual Purchase Report")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase:", total)