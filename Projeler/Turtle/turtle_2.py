#----------------------------------------------------------------------------------------------------------------------------#

# Kare çizelim:
import turtle

tospik = turtle.Turtle()

# kenar 1
tospik.fd(100)
tospik.lt(90)

# kenar 2
tospik.fd(100)
tospik.lt(90)

# kenar 3
tospik.fd(100)
tospik.lt(90)

# kenar 4
tospik.fd(100)
tospik.lt(90)


for i in range(4):
    tospik.fd(100)
    tospik.lt(90)

turtle.mainloop()



#----------------------------------------------------------------------------------------------------------------------------#

# kare çizmek döngü ile 
import turtle
tospik = turtle.Turtle()

for i in range(4):
    tospik.fd(100)
    tospik.lt(90)

turtle.mainloop()

# mainloop
# son satır olmalı -> mainloop
turtle.mainloop()