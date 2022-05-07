#Ticket Price
age = int(input("Enter Your Age : "))
if 0<age<=3:
    print("Ticket Price Free")
elif 3<age<=10:
    print("Ticket Price 150")
elif 10<age<=60:
    print("Ticket Price 250")
else:
    print("Ticket Price 200")
