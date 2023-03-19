#Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter their surname and display their full name in upper case. If the length of the first name is five or more characters, display their name in lower case.

print("HELLO")
fname=input("\nPlease enter your first name: ")
print("\nLength of the first name: ",len(fname))

if (len(fname))<=5: #checking the length of the first name if under five characters, 
  sname=input("\nEnter your Surname: ")#ask them to enter their surname  
  print("\n Your full name is: ",fname.upper(),sname.upper())#display their full name in upper case. 
else:
  print("\n ",fname.lower()) #If the length of the first name is five or more characters, display their name in lower case.