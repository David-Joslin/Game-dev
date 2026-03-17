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

question_index = 0
question_count = 0
#question_file_name = "C:\Users\josli\OneDrive\Desktop\Jetlearn\game_dev\Quiz_game\questions.txt"
question_file_name = "questions.txt"
questions = []
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
    marquee_message += f"Q:{question_index} of {question_count}"

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
        question[0].strip(), question_box,
        color="white",shadow=(0.5,0.5),
        scolor = "dim grey")

    #to display ans_box texts
    index = 1
    for answer_box in answer_boxes:
         screen.draw.textbox(question[index].strip(),answer_box,
         color="black")
    index = index + 1
    
def update():
    move_marquee()

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_question_file():
    global question_count
    global question_file_name

    q_file = open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()


def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split("|")
    

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == int(question[5]):
                correct_answer()
            else:
                game_over()
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()
  

def correct_answer():
    global score
    global time_left
    global question
    global questions

    score += 1
    if questions:
        question = read_next_question
        time_left = 10
    else:
        game_over()

def game_over():
    global question
    global time_left
    global is_game_over
    message = f"Game over!\nYou got {score} questions correct"
    question = [message,"-","-","-","-",5]
    time_left == 0
    is_game_over = True

def skip_question():
    global question
    global time_left
    if question and not is_game_over:
        question = read_next_question()
        time_left = 10
    else:
        game_over()
    

def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()

read_question_file()
question = read_next_question()

clock.schedule_interval(update_time_left,1)







pgzrun.go()