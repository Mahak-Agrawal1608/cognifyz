def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return 5/9 * (fahrenheit - 32)

def convertor():
    print("Temperature Convertor : \n")
    print("\t1. Celsius → Fahrenheit")
    print("\t2. Fahrenheit → Celsius\n")

    opt = int(input("Enter your choice (1 or 2): "))

    if opt == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        temp = celsius_to_fahrenheit(celsius)
        print(f"{celsius} °C = {temp:.2f} °F.")
        
    elif opt == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        temp = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} °F = {temp:.2f} °C.")
        
    else:
        print("Invalid choice. Please enter 1 or 2.")

convertor()

#TIME COMPLEXITY OF CODE IS O(1)
#SPACE COMPLEXITY OF CODE IS O(1)