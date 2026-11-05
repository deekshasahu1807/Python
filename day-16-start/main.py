# import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.color("Coral")
# timmy.shape("turtle")
# turtle.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

pt = PrettyTable()
pt.field_names = ["Name", "Age", "Gender"]
pt.add_rows([
    ['Bhavesh', 35, 'Male'],
    ['Diksha', 33, 'Female'],
    ['Manvik', 2, 'Male']
])
pt.align = 'l'
print(pt)
ptt = PrettyTable()
ptt.add_column('Pokemon Name', ["Pikachu", "Squirtle", "Charmendar"])
ptt.add_column('Type', ["Electric", "Water", "Fire"])
ptt.align['Pokemon Name'] = "l"
ptt.align['Type'] = "c"
print(ptt)
