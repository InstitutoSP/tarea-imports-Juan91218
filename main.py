import funciones as fn
while True:
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("5. SALIR")

    opcion = input("Ingrese el número de la opción que desea realizar: ")
    
    x1=int(input("ingrese el primer numero:"))
    x2=int(input("ingrese el segundo numero:"))
    if opcion == "1":
      fn.sumar(x1,x2)
    elif opcion == "2":
       fn.resta(x1,x2)
    elif opcion == "3":
       fn.multiplicar(x1,x2)
    elif opcion == "4":
       fn.division(x1,x2)
    elif opcion == "5":
        print("¡Chau!")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 5.")