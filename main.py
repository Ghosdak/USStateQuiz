import pandas
import turtle

screen = turtle.Screen()
screen.title("US State Quiz")
screen.setup(width=700, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.ht()
writer.penup()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 Correct", "Name of a State: ").title()
    
    state = data[data['state'] == answer]
    if not state.empty:
        writer.goto(int(state.x), int(state.y))
        writer.write(answer)
        guessed_states.append(answer)
    if answer == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break
    
