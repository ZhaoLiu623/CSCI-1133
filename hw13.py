import math,turtle,random
class Lander(turtle.Turtle):
    '''
    Purpose: Represents an object falling towards the moon’s surface
    Instance variables: self.vx represents the x velocity
                        self.vy represents the y velocity
                        self.remain represents the number of remain fuel
                        see turtle.Turtle
    Methods: self.move() runs the process of lander move
             self.thrust() runs the process of push lander up with a change velocity 
             self.left1() runs the process of lander turn left
             self.right1() runs the process of lander turn right
    '''
    def __init__ (self,xp,yp,vx,vy):
        turtle.Turtle.__init__(self)
        self.vx=vx
        self.vy=vy
        self.remain=50
        self.left(90)
        self.penup()
        self.speed(0)
        self.setpos(xp,yp)
    def move(self):
        self.vy-=0.0486
        new_x=self.xcor()+self.vx
        new_y=self.ycor()+self.vy
        self.setpos(new_x,new_y)
    def thrust(self):
        if self.remain>0:
            self.remain-=1
            angle=math.radians(self.heading())
            self.vx+=math.cos(angle)
            self.vy+=math.sin(angle)
            print(self.remain)
        else:
            print('Out of fuel')
    def right1(self):
        if self.remain>0:
            self.remain-=1
            self.right(10)
            print(self.remain)
        else:
            print('Out of fuel')
    def left1(self):
        if self.remain>0:
            self.remain-=1
            self.left(10)
            print(self.remain)
        else:
            print('Out of fuel')
class Meteors(turtle.Turtle):
    '''
    Purpose: The object that represents meteor in the game
    Instance variables: self.vx represents the x velocity
                        self.vy represents the y velocity
                        self.x represents the x position
                        see turtle.Turtle
    Methods: self.move() runs the process of meteor move 
    '''
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.vx=0
        self.vy=0
        self.right(90)
        self.color('red')
        self.penup()
        self.speed(0)
        self.x=random.uniform(100,900)
        self.setpos(self.x,1000)
    def move(self):
        self.vy-=0.0486
        new_y=self.ycor()+self.vy
        self.setpos(self.x,new_y)
class Game:
    '''
    Purpose: The object that represents keep the game running, keep track of the meteors, and so on
    Instance variables:self.player represent a Lander
                       self.list1 contains 10 Meteors
    Methods: self.gameloop() represents run the game in a condiontional loop 
    '''
    def __init__(self):
        turtle.setworldcoordinates(0, 0, 1000, 1000)
        turtle.delay(0)
        self.player=Lander(random.uniform(100,900),random.uniform(500,900),random.uniform(-5,5),random.uniform(-5,0))
        self.list1=[]
        for i in range(10):
            self.list1.append(Meteors())
        self.player.turtlesize(2)
        self.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.right1, 'Right')
        turtle.onkeypress(self.player.left1, 'Left')
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        self.player.move()
        for ele in self.list1:
            if ele.ycor()>1:
                ele.move()
        if abs(ele.ycor()-self.player.ycor())<15 and abs(ele.xcor()-self.player.xcor())<15:
            turtle.write('You crashed!', move=False, align='center', font=('宋体', 24,'normal'))
        elif self.player.ycor()>10:
            turtle.Screen().ontimer(self.gameloop, 30)
        else:
            if self.player.vx>=-3 and self.player.vx<=3 and self.player.vy>=-3 and self.player.vy<=3:
                turtle.write('Successful landing!', move=False, align='center', font=('宋体', 8, 'normal'))
            else:
                turtle.write('You crashed!', move=False, align='center', font=('宋体', 24,'normal'))    
       
