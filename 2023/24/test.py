import sympy

x, y = sympy.symbols("x,y")
print(sympy.solve([sympy.Eq(x + y, 1), sympy.Eq(x - y, 2)], [x, y]))
