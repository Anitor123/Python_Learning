from turtle import Turtle, Screen


zomp = Turtle()


zomp.shape("classic")
zomp.color("black")
for tri in range(3):
    zomp.right(120)
    zomp.forward(100)
for sqr in range(3):
    zomp.right(90)
    zomp.forward(100)
zomp.right(90)  
zomp.forward(100)
for pent in range(4):    
    zomp.right(72)
    zomp.forward(100)
zomp.right(72)
zomp.forward(100)
for hex in range(5):
    zomp.right(60)
    zomp.forward(100)    
zomp.right(60)
zomp.forward(100)    
for hept in range(6):
    zomp.right(51.42857142857143)
    zomp.forward(100)
zomp.right(51.42857142857143)
zomp.forward(100)
for oct in range(7):
    zomp.right(45)
    zomp.forward(100)
zomp.right(45)
zomp.forward(100)   
for non in range(8):
    zomp.right(40)
    zomp.forward(100)  
zomp.right(40)
zomp.forward(100) 
for dec in range(9):
    zomp.right(36)
    zomp.forward(100)  
zomp.right(36)
zomp.forward(100)        








screen = Screen()
screen.exitonclick()
