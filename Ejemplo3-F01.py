#Equipo: 
#Trabajaron: Fredy Emanuel Pensado Paredes(TablosAF00)
# 2025/03/03 	V.1.0.2
#Este codigo tiene como finalidad pedir a un usuario que ingrese un numero cualquiera; entonces se determinara si dicho numero es impar o par.


numero = int(input("Ingrese un número: ")) #Primeramente se crea una variable donde se guardaran el numero.
#Se usa la sintaxis donde determinamos con Int para que se almacene un numero entero seguido de la funcion input que se usa para recoger datos que se introduscan con el teclado.
#Tambien entre comillas colocamos el texpt de "ingrese un numero"

if numero % 2 == 0: #Con una funcion IF determinamos los dos posibles resultados donde primero es el caso donde el numero si es par.
  #Con la expresion numero % 2 == 0 usamos el operador % que nos devuelve el residuo de la division del numero que se ingreso entre 2 por lo que si el residuo es 0 sera un numero par.
    print("El número es par")#Si la condicion es 0 imprimira ese mensaje 
else:
    print("El número es impar") #Si la cpndicion no se cumple mostrara este texto en pantalla indicando que el numero no es par.
