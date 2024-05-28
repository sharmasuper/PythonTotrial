a = "!!!! harry!!!!"
# string method
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.split(" "))
print(a.split(" "))
b = "hello"
print(a.capitalize())
print(len(b.center(50)))
b = "moht mohit  mohit mohit"
print(b.count("mohit"))

str1 = "welcome to the Console, !!!"
print(str1.endswith("!!!"))
a = str1.find("to")
print(a)
a = str1.index("to")  
print(a)

# if he element does not match it give error
# a = str1.index("hel")
# print(a)

st1 = "WelcomeToHome12"
print(st1.isalnum())

st1 = "Welcomehrllo" 
print(st1.isalpha())
# isalpha method does not take number is string

print(st1.islower())
print(str1.isprintable())
# but we use /n it give false
str1 = "    "
print(str1.isspace())
str1 = "To Kill A Mocking Bird"
print(str1.istitle())
print(str1.startswith('To'))
print(str1.swapcase())

print(str1.title())





