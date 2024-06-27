# Day of the Week
a = int(input("enter a number:"))
print("The day of the week is:")
if a == 1:
  print("Monday")
elif a == 2:
   print("Tuesday")
elif a == 3:
   print("Wednesday")
elif a == 4:
   print("Thursday")
elif a == 5:
   print("Friday")
elif a == 6:
   print("Saturday")
elif a == 7:
   print("Sunday")
else:
  print("'Error!' there is no such day")

# Even or odd and positive or negative
a = int(input("enter an integer:"))
print("The integer is a:")
if a > 0:
  print("This is a positive number")
elif a < 0:
  print("This is a negative number")
if a % 2 == 0:
 print("This is an even number")
elif a % 3 == 0:
  print("This is an odd number")
elif a == 1:
  print("This is 1")
else:
  print("This is 0")

#Season based on Months

month_number = int(input("enter the number:"))
month = input("enter the month:")
if month_number in [12, 1 , 2]:
  print("'Winter'")
elif month_number in [3,4,5]:
  print("'Spring'")
elif month_number in [6,7,8]:
  print("'Summer'")
elif month_number in [9,10,11]:
  print("'Fall'")
else:
   print("You have entered a wrong month number!!!")

if month in ["December", "January" , "Feburary"]:
 print("Winter")
elif month in ["March" , "April" , "May "]:
  print("Spring")
elif month in ["June","July","August"]:
  print("summer")
elif month in ["September","October","November"]:
  print("Fall")
else:
  print("You have entered a wrong month!!!")

#Electricity Bill calculation

a = int(input("Enter the Electricity Units:"))
Bill = 0
if a <= 100:
  Bill = a*0.50
elif  a <= 200:
  Bill = 100*0.50+(a-100)*0.75
elif  a <= 300:
  Bill = 100*0.50+100*0.75+(a-200)*1.20
elif a > 300:
  Bill = 100*0.50+100*0.75+100*1.20+(a-300)*1.50

print(f"Electricity Bill: ${Bill:.3f}")

#Vowel or consunant

a = input("enter a character:")
if a in ["a", "e" , "i" , "o","u"]:
  print("vowel")
else:
  print("Consonants")

#Traffic light system

a = input("enter the color:")
if a in ["red"]:
  print("Stop")
elif a in ["Yellow"]:
  print("Caution")
elif a in ["Green"]:
  print("Go")
else:
  print("Invalid color")
