import turtle
from name_table import NameTable
import pandas

screen = turtle.Screen()
screen.title("USA States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_states = []
quiz_on = True
while quiz_on:
    user_answer = screen.textinput(title=f"{len(correct_states)}/{len(data)} Guess the State",
                                   prompt="What's another state name: ").title()

    states_names = data.state.to_list()
    if user_answer in states_names:
        state = data[data.state == user_answer]
        x_cor = int(state.x)
        y_cor = int(state.y)
        correct_states.append(user_answer)
        state_place = NameTable(user_answer)
        state_place.coordinates(x_cor, y_cor)
    elif user_answer == "Exit":
        unknown_states_names = []
        for name in states_names:
            if name not in correct_states:
                unknown_states_names.append(name)
        dict_of_states = {"name": unknown_states_names}
        dict_to_dataframe = pandas.DataFrame(dict_of_states)
        dict_to_dataframe.to_csv("states_must_learn")
        quiz_on = False

    if len(correct_states) == len(data):
        state_place.game_finished()
        quiz_on = False

screen.exitonclick()
