#Equipo:Yo
#Trabajaron: Pensado Paredes Fredy Emanuel(TablosAF00)
# 2025/03/03 	V.1.0.1

#La finalidad de este codigo es mistrar en forma de bucle una lista de frutas la que inicialmente tendra tres elementos y luego se añadira un cuarto 
frutas = ["manzana", "plátano", "naranja"] #Creamos una lista de frutas que contiene tres elementos que deben estar entre los corchetes [] para que sea correcto 


frutas.append("pera") #El comando append() lo usamos para agregar un elemento adicional al final de la lista 
                      #En este caso es pera que se coloca dentro de los parentesis () y entre comillas ""


print("Lista de frutas:", frutas) #En edta linea con el comando print Mostramos en pantalla el texto "lista de frutas" mas la variable frutas donde estan alamcenados los enlementos anteriores 
                                  #Para que funcione debemos separar el texto de la variable con una coma ,

for fruta in frutas: #Aqui se crea un bucle For con la instruccion de recorrer cada elemento dentro de la lista frutas 
    print("Tengo una", fruta) #Junto al bucle se usa el comando print imprimimos en cadena el texto "tengo una" seguido de la variable donde esta guardada la lista de frutas 
  #Gracias al bucle el texto se imprime tantas veces como elementos haya en la lista
