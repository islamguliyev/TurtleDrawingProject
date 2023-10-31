import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Python Turtle")


'''
#beginner turtle drawing:

turtle_instance = turtle.Turtle()
turtle_instance.forward(50)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(180)
turtle_instance_2.forward((100))
turtle.done()
'''



##############################



'''
#square:

turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle.done()
'''


'''
#square with loop:

turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.right(90)
    
turtle.done()
'''



##############################



'''
#star:

turtle_instance = turtle.Turtle()

turtle_instance.left(60)
turtle_instance.forward(200)
turtle_instance.right(120)
turtle_instance.forward(200)
turtle_instance.left(50)
turtle_instance.forward(200)
turtle_instance.right(120)
turtle_instance.forward(200)
turtle_instance.left(50)
turtle_instance.forward(200)
turtle_instance.right(120)
turtle_instance.forward(200)
turtle_instance.left(40)
turtle_instance.forward(200)
turtle_instance.right(120)
turtle_instance.forward(200)
turtle_instance.left(60)
turtle_instance.forward(200)
turtle_instance.right(123)
turtle_instance.forward(200)
turtle.done()
'''


'''
#star2 with loop:

turtle_instance = turtle.Turtle()

for i in range(5):
    turtle_instance.left(144)  #right=left
    turtle_instance.forward(150)

turtle.done()
'''


'''
#polygon, for example, lets's draw a hexagon:

turtle_instance = turtle.Turtle()

num_sides = 8
angle = 360.0 / num_sides
side_length = 200

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()
'''


'''
#star2 with polygon code:

turtle_instance = turtle.Turtle()

num_sides = 5  #change
angle = 360.0 / num_sides * 2  #change
side_length = 200

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()
'''


#square with polygon code:

turtle_instance = turtle.Turtle()

num_sides = 8
angle = 360.0 / num_sides * 2
side_length = 200

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()