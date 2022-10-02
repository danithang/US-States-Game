import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# loading image into screen
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
# calling turtle to get image from above to show up on screen
turtle.shape(image)

# reading csv file with pandas
states_data = pandas.read_csv("50_states.csv")
# putting all states in a list
all_states = states_data.state.to_list()
guessed_states = []

# while loop to say if length of list guessed_states is less than 50 then continue with the loop
while len(guessed_states) < 50:
    # changing the title to length of guessed_states whenever user answer puts in the right input so each correct guess
    # will be documented because guessed_states will append to user_answer....title() will accept upper or lower case
    # input
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What is another state name?").title()

    # if user input types exit(Has to be capitalized because of title())...end while loop
    if user_answer == "Exit":
        # creating a not guessed list to append to the states that were not guessed and creating new DataFrame to store
        # those un-guessed states each time someone plays
        not_guessed = []
        for state in all_states:
            if state not in guessed_states:
                not_guessed.append(state)
        states_left = pandas.DataFrame(not_guessed)
        states_left.to_csv("states_to_learn.csv")
        break
    # if statement to check if user answer is in all_states list
    if user_answer in all_states:
        guessed_states.append(user_answer)
        # creating a turtle and hiding it and pen up
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # checking if states_data.state equals user_answer and if it does go to right coordinates and write name of
        # each state
        state_info = states_data[states_data.state == user_answer]
        t.goto(int(state_info.x), int(state_info.y))
        # writing user answer in the right coordinates because we already did the checks to make sure user_answer
        # matches
        # all_states variable
        t.write(user_answer)






