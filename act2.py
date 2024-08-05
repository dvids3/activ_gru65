def cal_area_cir(rad):
    pi = 3.14 
    area = pi * (rad ** 2)  
    return area


rad = float(input("Introduce el radio del círculo"))
cal_area_cir = cal_area_cir(rad)
print("El área del círculo es", cal_area_cir)