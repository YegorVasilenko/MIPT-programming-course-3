from complex_vasilenko_improved import ComplexNumber


a = ComplexNumber(1, 2)
b = ComplexNumber(3, -5)
c = a + b
d = a - b
e = a * b
f = ComplexNumber(2, 2) / ComplexNumber(2, 0)
print(c.get_Re(), c.get_Im())
print(d.get_Re(), d.get_Im())
print(e.get_Re(), e.get_Im())
print(f.get_Re(), f.get_Im())
print(e == f)
print(ComplexNumber(1, 1) == f)
