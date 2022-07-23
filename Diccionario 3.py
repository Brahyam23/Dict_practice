d1 = {'Euro':'€',
      'Dolar':'$',
      'Yen':'¥'
}
while True:
    divisa=input("""Que divisa esta buscando?:
1°Euro
2°Dolar
3°Yen\n""")
    try:
        if divisa.lower()=="euro" or int(divisa)==1:
            print("El simbolo de su divisa es:", d1["Euro"])
        elif divisa.lower=="dolar" or int(divisa)==2:
            print("El simbolo de su divisa es:", d1["Dolar"])
        elif divisa.lower=="yen" or int(divisa)==3:
            print("El simbolo de su divisa es:", d1["Yen"])
        else:
            print("Ha ingresado una divisa no disponible, intentelo nuevamente\n")
            continue
        i=input("""\nDesea buscar otra divisa?:
    1° Si
    2° No\n""")
        if i.lower()=="no" or int(i)==2:
            break

    except(ValueError):
        print("Ha ingresado una opción inválida, intentelo nuevamente")

print("Hasta luego!");