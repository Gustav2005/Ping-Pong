#Ping pong spil

import turtle as t
playerAscore=0
playerBscore=0
  
#Opretelse af et vindue og erklæring en variabel kaldet window
window=t.Screen()
window.title("Ping pong spil")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)


#Definering af venstre spiller
venstre_spiller=t.Turtle()
venstre_spiller.speed(0)
venstre_spiller.shape("square")
venstre_spiller.color("white")
venstre_spiller.shapesize(stretch_wid=5,stretch_len=1)
venstre_spiller.penup()
venstre_spiller.goto(-350,0)

#Definering af højre spiller
højre_spiller=t.Turtle()
højre_spiller.speed(0)
højre_spiller.shape("square")
højre_spiller.color("white")
højre_spiller.shapesize(stretch_wid=5,stretch_len=1)
højre_spiller.penup()
højre_spiller.goto(350,0)


#Kode for bolden
bold=t.Turtle()
bold.speed(0)
bold.shape("circle")
bold.color("red")
bold.penup()
bold.goto(5,5)
boldxretning=0.2
boldyretning=0.2

#Kode for bevægelse af den venstre spillers bat
def venstre_spiller_op():
    y=venstre_spiller.ycor()
    y=y+45
    venstre_spiller.sety(y)
  
def  venstre_spiller_ned():
    y=venstre_spiller.ycor()
    y=y-45
    venstre_spiller.sety(y)


#Kode for bevægelse af den venstre spillerts bat
def højre_spiller_op():
    y=højre_spiller.ycor()
    y=y+45
    højre_spiller.sety(y)
  
def højre_spiller_ned():
    y=højre_spiller.ycor()
    y=y-45
    højre_spiller.sety(y)


#Taster til at spille
window.listen()
window.onkeypress(venstre_spiller_op,'w')
window.onkeypress(venstre_spiller_ned,'s')
window.onkeypress(højre_spiller_op,'Up')
window.onkeypress(højre_spiller_ned,'Down')

while True:
    window.update()


    bold.setx(bold.xcor()+boldxretning)
    bold.sety(bold.ycor()+boldyretning)

    if bold.ycor()>290:
        bold.sety(290)
        boldyretning=boldyretning*-1
    if bold.ycor()<-290:
        bold.sety(-290)
        boldyretning=boldyretning*-1
          
    if bold.xcor() > 390:
        bold.goto(0,0)
        
        
        