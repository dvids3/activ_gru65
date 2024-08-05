def fa_a_ce(g_fa):
    g_ce = (g_fa - 32) * 5/9
    return g_ce

g_fa = float(input("Ingrese la temperatura en grados Fahrenheit"))
g_ce = fa_a_ce(g_fa)
print(g_fa,"grados Fahrenheit son", g_ce, "grados Celsius")