import pgzrun

WIDTH = 800
HEIGHT = 700
TITLE = "Quiz Game"

marquee_box = Rect(0,0, 800,60 ) #Rect(iniital_x,ini_y ,W,H)
question_box = Rect(20,80, 500,140)
timer_box = Rect(550,80, 140,140)
skip_box = Rect(600,270, 150,350)
ans_box1 = Rect(20,270, 230,150)
ans_box2 = Rect(270,270, 230,150)
ans_box3 = Rect(20,450, 230,150)
ans_box4 = Rect(270,450, 230,150)
answer_boxes = [ans_box1,ans_box2,ans_box3,ans_box4]
score = 0
time_left = 10
marquee_message = ""
is_game_over = False 

quesion_index = 0
question_count = 0
question_file_name = "game_dev\\Quiz_game\\questions.txt"

def draw():
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"brown")
    screen.draw.filled_rect(question_box,"light blue")
    screen.draw.filled_rect(timer_box,"light blue")
    screen.draw.filled_rect(skip_box,"green")
    #Answer boxes
    for answer in answer_boxes:
        screen.draw.filled_rect(answer,"light blue")
    

    #Marquee box message
    marquee_message = "Welcome to Quiz Master..." #msg
    marquee_message += f"Q:{quesion_index} of {question_count}"

    screen.draw.textbox(marquee_message, marquee_box, color="white")

    #Display timer box text
    screen.draw.textbox(
        str(time_left),timer_box,
        color="white",shadow=(0.5,0.5),
        scolor="dim grey"
    )

    #Skip box
    screen.draw.textbox(
        "Skip", skip_box,
        color="black",angle=-90
    )
    
    #Question box text
    screen.draw.textbox(
        question[0].strip(), question_box(),
        color="white",shadow=(0.5,0.5),
        scolor = "dim grey")

    #to display ans_box texts
    index = 1
    for answer_box in answer_boxes:
         screen.draw.textbox(question[index].strip(),answer_box,
         color="black")
    index = index + 1
    



pgzrun.go()