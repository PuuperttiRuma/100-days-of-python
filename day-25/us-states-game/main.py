import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Screenwriter
screen_writer = turtle.Turtle()
screen_writer.penup()
screen_writer.hideturtle()
FONT = ("Arial", 8, "normal")

def write_state_name(state_name, x, y):
    screen_writer.goto(x, y)
    screen_writer.write(state_name, False, "Center", FONT)


answer = screen.textinput(title="Guess a State", prompt="Type a name of a state name.").capitalize()

# Data
states_data = pandas.read_csv("50_states.csv")

state_df = states_data[states_data["state"] == answer]
if state_df.empty:
    print("Wrong answer")
else:
    state_dict = state_df.to_dict('list')
    print(state_dict)

screen.exitonclick()
