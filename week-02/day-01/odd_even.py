# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.

number = input('Give me a number: ')
if int(number)%2 == 0:
    print("The number is even")
else:
    print("The number is odd")

    