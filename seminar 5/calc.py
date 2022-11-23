from complex_number import ComplexNumber

print("What do You want to calculate?")
print("+ - * /")
s = input()
if s not in ["+", "-", "*", "/"]:
    raise ValueError
print("Enter real part of the first number:")
Re_1 = float(input())
print("Enter imaginary part of the first number:")
Im_1 = float(input())
print("Enter real part of the second number:")
Re_2 = float(input())
print("Enter imaginary part of the second number:")
Im_2 = float(input())
z_1 = ComplexNumber(Re_1, Im_1)
z_2 = ComplexNumber(Re_2, Im_2)
if s == "+":
    res = z_1 + z_2
elif s == "-":
    res = z_1 - z_2
elif s == "*":
    res = z_1 * z_2
else:
    res = z_1 / z_2
print(res)
