import turtle
import pandas
from questions import question_data

# set the turtle screen
screen = turtle.Screen()

# set the title of turtle screen
screen.title("Europe Trivia Questions")

# method to set the background image of the screen
def screen_method(img_name):
    image = img_name
    screen.addshape(image)
    turtle.shape(image)
    image = img_name
    screen.addshape(image)
    turtle.shape(image)

# call the method to set the bg of the screen
screen_method("bg.gif")

# reading the csv file in pandas
data = pandas.read_csv("european_countries.csv")

# start of the trivia quiz
continue_trivia = True
while continue_trivia:
    text_input = screen.textinput(title="So you think you know europe?", prompt="Type 'Yes' to start your Trivia "
                                                                                " or 'No' to end Trivia.").title()
    answer = 0
    # start trivia quiz
    if text_input == "Yes":
        # set new screen image
        screen_method("europe.gif")

        # loop through the question_data
        for index in range(len(question_data)):
            # quiz questions
            question_txt = question_data[index]["question"]
            # quiz answers
            question_ans = question_data[index]["correct_answer"]
            # variable to store quiz questions
            txt = screen.textinput(title=f"Question {index + 1} || Your current Score: {answer}", prompt=question_txt)

            # check if quiz question is equal to quiz answer, set turtle and position turtle coordinate
            if txt == question_ans:
                answer += 1
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                ans_cor = data[data.country == txt]
                t.goto(int(ans_cor.x), int(ans_cor.y))
                t.color("white")
                t.write(txt, align='center', font=('Arial', 11, 'normal'))

        # check if the length of question_data is less than 15
        if len(question_data) < 15:
            continue_trivia = False
            turtle.clearscreen()
            turtle.hideturtle()
            screen.title("End of Trivia")
            turtle.write(f"Your current Score: {answer}. Thanks for taking part in this Trivia.",
                         align='center', font=('Arial', 20, 'normal'))

    # end trivia quiz
    else:
        continue_trivia = False
        screen.title("Learn More About Europe and Come Back for your Trivia Questions. Happy Learning🚼")
        screen_method("body_bg.gif")
        turtle.write("⬆️", align='center', font=('Arial', 22, 'normal'))

# check on turtle screen to exit program
screen.exitonclick()
