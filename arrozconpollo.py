print("Bienvenido al simulador de arroz con pollo creado por yll.")
input("Presiona enter para continuar: ")

print("*Voy a la cocina*")
print("*Reviso todo*")

hay_pollo = input("Hay pollo? S/N ")
hay_arroz = input("Hay arroz? S/N ")

if hay_pollo != "S" or hay_arroz != "S":
    print("Voy al almacén po culiao")
    if hay_pollo != "S":
        print("*Compro pollo*")
    if hay_arroz != "S":
        print("*Compro el arroz*")

elif hay_pollo or hay_arroz == "S":
    print("Continuamos")

hay_aceite = input("Hay aceite? S/N ")

if hay_aceite != "S":
    print("Entonces cagamos.")
    exit()

input("Presione enter para freir el pollo: ")
print("*Se fríe el pollo*")

input("Presione enter para hacer el arroz: ")
print("*Se hace el arroz...*")
input("Presione enter para juntar el arroz y el pollo: ")

print("*Juntamos el arroz y el pollo*")
input("Presione enter para echarle ketchup: ")
print("*Le echamos ketchup*")
input("Pulse enter para continuar: ")

print("Comiendo... 1%")
print("Comiendo... 35%")
print("Comiendo... 57%")
print("Comiendo... 75%")
print("Comiendo... 99%")
input("Pulse una tecla para continuar... ")

print("Gracias por comerte tu arroz con pollo computarizado en Python.")
print("Sígueme en Twitter: @emlxya y chupame el pico.")
    exit()
