#Estas son las librerías que se utilizarán.

from turtle import * #Esto significa que se importan todas las funciones de la librería turtle.
from random import randrange #Esto significa que de la librería random solo se importa la función randrange.
from freegames import square, vector #Esto significa que de la librería freegames solo se importan las funciones "square" y "vector".

#Estas son las variables que se utilizarán para el programa

food = vector(0, 0) #Aquí la variable food indica la posción en la que se encuentra inicialmente de manera vectorial.
snake = [vector(10, 0)]  #Aquí la variable snake indica la posción inicial del cuadro que representa la serpiente, pero se encuentra dentro de una lista.
aim = vector(0, -10) #Aquí la variable aim nos indica la diracción inicial de la serpiente al generar el juego.


color = ['black','blue','green','pink','brown'] #Se creó esta lista para poder tener en una sola variable varias opciones.

p = color[randrange(0,5)] #La variable "p" será utilizada para definir el color del cuerpo de la serpiente.
#Lo que se hace es elegir de manera aleatoria uno de los colores de la lista en la variable "color".

p2 = color[randrange(0,5)] #La variable "p2" será utilizada para definir el color de la comida.
#Se elige de manera aleatoria un color de la lista de la variable colores.
#
#Este while se asegura de que los colores no se repitan y de ser así obliga a que la variable p2 tenga un color distinto.
while p2 == p:
    p2 = color[randrange(0,5)]

# Recibe un valor (x,y) y cambia el vector aim el cual
# indica la dirección a la que se dirige el snake
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head): #Esta función es llamada "inside" y toma como parámetro la variable "head".
    "Return True if head inside boundaries."
    #Lo que se busca es evaluar si la posición de la cabeza de la serpiente se encuentra dentro de los límites establecidos de la pantalla de juego.
    #De ser así regresa el valor booleano de True y no se así regresa False.
    return -200 < head.x < 190 and -200 < head.y < 190 #Return con la evaluación.


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        w = vector(randrange(-10,11,10),randrange(-10,11,10)) # Se creó un vector 'w' para definir un valor random entre -10, 0 y 10 tanto para x como para y
        food.move(w) # El vector creado cambia el valor de la posición de la comida
    clear()

    for body in snake:
        square(body.x, body.y, 9, p) #Construye el cuerpo de la serpiente

    square(food.x, food.y, 9, p2) #Construye el cuerpo de la comida
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
