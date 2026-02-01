print("Calculator")
number_1=int(input("Enter first number:"))
number_2=int(input("Enter second number:"))

operator=input("Enter operator(+,-,*,/,%,**,//):")

if operator=="+":
    print(number_1+number_2)
elif operator=="-":
    print(number_1-number_2)
elif operator=="*":
    print(number_1*number_2)
elif operator=="/":
    print(number_1/number_2)
elif operator=="%":
    print(number_1%number_2)
elif operator=="**":
    print(number_1**number_2)
elif operator=="//":
    print(number_1//number_2)
else:
    print("Invalid operator")