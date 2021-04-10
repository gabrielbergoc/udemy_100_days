import turtle, pandas

FONT = ("Arial Black", 8, "normal")

screen = turtle.Screen()
screen.title("Estados do Brasil")
image = "mapa_brasil.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("estados_brasil.csv")
states = data.estados.to_list()

# def get_mouse_click_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coord)
#
# turtle.mainloop()

chiquinha = turtle.Turtle()
chiquinha.hideturtle()
chiquinha.penup()
chiquinha.color("black")
chiquinha.speed(0)

corrects = []

while True:
    answer = screen.textinput(title=f"{len(corrects)}/{len(data.estados)} estados", prompt='Escreva o nome de um estado ou "sair" para fechar:').lower()

    if answer == "sair":
        break

    if answer in states and answer not in corrects:
        corrects.append(answer)

        x = float(data.x[data.estados == answer])
        y = float(data.y[data.estados == answer])

        chiquinha.goto(x, y)
        chiquinha.write(answer.title(), font=FONT, align="center")

chiquinha.color("red")
for state in states:
    if state not in corrects:
        x = float(data.x[data.estados == state])
        y = float(data.y[data.estados == state])

        chiquinha.goto(x, y)
        chiquinha.write(state.title(), font=FONT, align="center")

screen.exitonclick()