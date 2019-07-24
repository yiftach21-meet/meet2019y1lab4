import turtle
turtle.shape('turtle')
finn = turtle.clone()
finn.shape('square')
finn.penup()
finn.goto(100,100)
finn.pendown()
finn.goto(100,0)
finn.goto(0,0)
finn.goto(0,100)
finn.goto(100,100)
cat = finn.clone()
cat.shape('circle')
finn.goto(50,150)
finn.goto(0,100)
turtle.mainloop

