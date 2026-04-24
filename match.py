
op
total
while op 
print("1.-opcion1")
print("2.-opcion2")
print("3.-opcion3")
op=int(input("seleccione una opcion: "))
match op:
    case 1:
        print("seelecciono la opcion:")
        total+=25000
    case 2:
        print("el valo a pagar", 500000*1.19)