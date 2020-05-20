#Strong Password Detection

#Password requirements:
minLength = 8 #Must be at least 8 characters
minUpper = 1 #Must contain at least 1 uppercase character
minLower = 1 #Must contain at least 1 lowercase character
minDigits = 1 #Must contain at least 1 digit

print("Password must be at least 8 characters long, upper and lower case characters, and at least one digit.")
password = input("Enter password:\n")
#print(password)

#Determine if password is at least 8 characters long
long = False
# print(len(password))
if len(password) >= minLength:
    long = True
    #print("Password is at least 8 characters long.")
else:
    print("Password is too short. Password must be at least 8 characters long.")

#Determine if password contains uppercase characters:
upper = False
uppercase = 0
for i in range(len(password)):
   if password[i].isupper():
       uppercase = uppercase + 1
#print(uppercase) #Prints how many uppercase characters in password
if uppercase >= minUpper:
    #print(f"Password contains {uppercase} uppercase character(s).")
    upper = True
else:
    print(f"Password does not contain any uppercase characters.")

#Determine if password contains lowercase characters:
lower = False
lowercase = 0
for i in range(len(password)):
   if password[i].islower():
       lowercase = lowercase + 1
#print(lowercase) #Prints how many lowercase characters in password
if lowercase >= minLower:
    lower = True
    #print(f"Password contains {lowercase} lowercase character(s).")
else:
    print(f"Password does not contain any lowercase characters.")

#Determine if password contains digit(s):
digit = False
digits = 0
for i in range(len(password)):
   if password[i].isdigit():
       digits = digits + 1
#print(lowercase) #Prints how many digit(s) in password
if digits >= minDigits:
    digit = True
    #print(f"Password contains {digits} digit(s).")
else:
    print(f"Password does not contain any digits.")

#Determine if meets password requirements
if long == True and upper == True and lower == True and digit == True:
    print("Password meets password requirements.")
