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
name = "Sagar"
if "a" in name:
    print("a in available")
else:
    print("Not present")    
name1 = input("Enter Your Name : ")
age1 = int(input("Enter Your Age : ")) 
if (name1[0] == "A" or name1[0] == "a") and age1>=25:
    print("You Are Permitted")
else:
    print("Not Permitted")        
