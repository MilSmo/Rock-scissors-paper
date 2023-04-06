from tkinter import *
from tkinter import ttk
from random import randint
from PIL import Image,ImageTk

root = Tk()
root.title("Rock, paper, scissors")
root.geometry("500x500")
root.config(bg="white")
rock =(Image.open("rock.png"))
re_rock = rock.resize((200, 200), Image.ANTIALIAS)
n_rock = ImageTk.PhotoImage(re_rock)
paper = (Image.open("img_1.png"))
re_paper = paper.resize((200, 200), Image.ANTIALIAS)
n_paper = ImageTk.PhotoImage(re_paper)
scissors =(Image.open("scissors.png"))
re_scissors = scissors.resize((200, 200), Image.ANTIALIAS)
n_scissors = ImageTk.PhotoImage(re_scissors)

image_list = [n_rock, n_paper, n_scissors]
computer_choice = randint(0, 2)
image_label = Label(root, image=image_list[computer_choice], bd=0)
image_label.pack(pady=20)
def spin():
    computer_choice = randint(0, 2)
    image_label.config(image=image_list[computer_choice])


    # 0 = rock, 1 = paper, 2 = scissors


    if user_choice.get() == "rock":
        user_choice_value = 0
    elif user_choice.get() == "paper":
        user_choice_value = 1
    elif user_choice.get() == "scissors":
        user_choice_value = 2

    if user_choice_value == computer_choice:
        win_loss_label.config(text="Tie!")
    elif user_choice_value == 0:
        if computer_choice == 1:
            win_loss_label.config(text="You lose!")
        else:
            win_loss_label.config(text="You win!")
    elif user_choice_value == 1:
        if computer_choice == 2:
            win_loss_label.config(text="You lose!")
        else:
            win_loss_label.config(text="You win!")
    elif user_choice_value == 2:
        if computer_choice == 0:
            win_loss_label.config(text="You lose!")
        else:
            win_loss_label.config(text="You win!")



user_choice = ttk.Combobox(root, values=["rock", "paper", "scissors"])
user_choice.current(0)
user_choice.pack(pady=20)


win_loss_label = Label(root, text="", font=("Helvetica", 20))
win_loss_label.pack(pady=50)

spin_button = Button(root, text="Try again", command=spin)
spin_button.pack(pady=20)

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)



root.mainloop()
