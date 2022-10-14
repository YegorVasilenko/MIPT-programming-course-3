from complex_vasilenko import ComplexNumber


# set 1
z = ComplexNumber(2, 2)
print(z.get_exponential_form())
print(z.get_algebraic_form())
z.set_r(3)
print(z.get_exponential_form())
print(z.get_algebraic_form())
s = z.substract(ComplexNumber(1, 1))
print(s.get_algebraic_form())


# set 2
a = ComplexNumber(3, -1)
b = ComplexNumber(1, 2)
sum_1 = a.sum(b)
sum_2 = b.sum(a)
diff_1 = a.substract(b)
diff_2 = b.substract(a)
prod_1 = a.product(b)
prod_2 = b.product(a)
ratio_1 = a.divide(b)
ratio_2 = b.divide(a)
print(sum_1.get_algebraic_form())
print(sum_2.get_algebraic_form())
print(diff_1.get_algebraic_form())
print(diff_2.get_algebraic_form())
print(prod_1.get_algebraic_form())
print(prod_2.get_algebraic_form())
print(ratio_1.get_algebraic_form())
print(ratio_2.get_algebraic_form())


# set 3
a = ComplexNumber(1, 0)
b = ComplexNumber(0, 1)
c = ComplexNumber(-1, 0)
d = ComplexNumber(0, -1)
print(a.get_exponential_form())
print(b.get_exponential_form())
print(c.get_exponential_form())
print(d.get_exponential_form())
