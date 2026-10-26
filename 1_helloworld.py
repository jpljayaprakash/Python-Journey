#print("Hello world")

x = input("Enter your name:")

#stiching strings
#print("Hello "+x)

#input function inside print function
#print("Hello",input("Enter your name:"))

#whitespace removal
x=x.strip()

#captialize first letter
#x=x.capitalize()

#title case
x=x.title()

#split string
#first,last=x.split(" ")

#Format string
#rint(f"Hello {x.split(' ')[1]}") 

#chain methods
print("Hello",input("Enter your name:").strip().title().split(" ")[1])


