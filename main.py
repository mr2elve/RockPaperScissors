import tkinter as tk
from random import *
import pygame.mixer

main_list = ["Rock", "Paper", "Scissors"]

window = tk.Tk()

window.geometry("800x400")
window.title("project_es_zhi")

user_score = 0
comp_score = 0
score_value = 0

pygame.mixer.init()


def play_background_music():
    pygame.mixer.music.load("mus/background_music.mp3")
    pygame.mixer.music.play(-1)


img = tk.PhotoImage(file="images/bg.png")


def start_page():
    def get_v():
        value = e.get()

        if value.isdigit():
            if int(value) > 0:
                frame.pack_forget()
                global score_value
                score_value = value
                main_game()
        else:
            e.delete(0, tk.END)
            warning = tk.Label(frame, text="Введите корректное целое число", font="normal 15", bg="red")
            warning.place(x=300, y=130)

    frame = tk.Frame(window)
    frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    bg_img = tk.Label(frame, image=img)
    bg_img.place(x=0, y=0)

    name = tk.Label(frame, text="Камень Ножницы Бумага 228", font="normal 31", borderwidth=2, relief="solid")
    name.place(x=175, y=10)

    lb = tk.Label(frame, text="Введите до скольки побед:", font="normal 27", borderwidth=2, relief="solid")
    lb.place(x=175, y=175)

    e = tk.Entry(frame, width=3, font="normal 20")
    e.place(x=525, y=175)

    b_confirm = tk.Button(frame, text="Подтвердить", font="normal 30", command=get_v)
    b_confirm.place(x=275, y=275)

    window.mainloop()


def main_game():
    play_background_music()
    frame = tk.Frame(window)
    frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    name = tk.Label(frame, text="Камень Ножницы Бумага - Player vs Computer", font="normal 20")
    name.place(x=175, y=10)

    label1 = tk.Label(frame, text="Player", font="normal 15")
    label2 = tk.Label(frame, text="VS", font="normal 15")
    label3 = tk.Label(frame, text="Computer", font="normal 15")

    label1.place(x=80, y=50, width=100)
    label2.place(x=350, y=50, width=100)
    label3.place(x=600, y=50, width=100)

    rock_png = tk.PhotoImage(file="images/rock.png")
    paper_png = tk.PhotoImage(file="images/paper.png")
    scissors_png = tk.PhotoImage(file="images/scissors.png")

    r_rock_png = rock_png.subsample(5, 5)
    r_paper_png = paper_png.subsample(5, 5)
    r_scissors_png = scissors_png.subsample(5, 5)

    user_image = tk.Label(frame, image="")
    user_image.place(x=80, y=100, width=100)

    comp_image = tk.Label(frame, image="")
    comp_image.place(x=600, y=100, width=100)

    label4 = tk.Label(frame, text="", font="normal 25", width=15, borderwidth=2, relief="solid")
    label4.place(x=275, y=250)

    user_count = tk.Label(frame, text="", font="normal 25", borderwidth=2, relief="solid", width=2)
    user_count.place(x=110, y=250)

    comp_count = tk.Label(frame, text="", font="normal 25", borderwidth=2, relief="solid", width=2)
    comp_count.place(x=630, y=250)

    def rock():  # rock fs
        user = "Rock"
        computer = choice(main_list)
        user_image.config(image=r_rock_png)

        global user_score
        global comp_score
        global score_value

        if user == computer:
            label4.config(text="Ничья")
            comp_image.config(image=r_rock_png)
        elif computer == "Paper":
            label4.config(text="Компьютер выиграл!")
            comp_image.config(image=r_paper_png)
            comp_score += 1
            comp_count.config(text=comp_score)
        else:
            label4.config(text="Вы выиграли!")
            comp_image.config(image=r_scissors_png)
            user_score += 1
            user_count.config(text=user_score)

        if int(user_score) >= int(score_value):
            frame.pack_forget()
            ending_page(True)
        elif int(comp_score) >= int(score_value):
            frame.pack_forget()
            ending_page(False)

    def paper():  # dsfs
        user = "Paper"
        computer = choice(main_list)
        user_image.config(image=r_paper_png)

        global user_score
        global comp_score
        global score_value

        if user == computer:
            label4.config(text="Ничья")
            comp_image.config(image=r_paper_png)
        elif computer == "Scissors":
            label4.config(text="Компьютер выиграл!")
            comp_image.config(image=r_scissors_png)
            comp_score += 1
            comp_count.config(text=comp_score)
        else:
            label4.config(text="Вы выиграли!")
            comp_image.config(image=r_rock_png)
            user_score += 1
            user_count.config(text=user_score)

        if int(user_score) >= int(score_value):
            frame.pack_forget()
            ending_page(True)
        elif int(comp_score) >= int(score_value):
            frame.pack_forget()
            ending_page(False)

    def scissors():  # sdfsf
        user = "Rock"
        computer = choice(main_list)
        user_image.config(image=r_scissors_png)

        global user_score
        global comp_score
        global score_value

        if user == computer:
            label4.config(text="Ничья")
            comp_image.config(image=r_scissors_png)
        elif computer == "Rock":
            label4.config(text="Компьютер выирал!")
            comp_image.config(image=r_rock_png)
            comp_score += 1
            comp_count.config(text=comp_score)
        else:
            label4.config(text="Вы выиграли!")
            comp_image.config(image=r_paper_png)
            user_score += 1
            user_count.config(text=user_score)

        if int(user_score) >= int(score_value):
            frame.pack_forget()
            ending_page(True)
        elif int(comp_score) >= int(score_value):
            frame.pack_forget()
            ending_page(False)

    b1 = tk.Button(frame, text="Rock", font="normal 12", width=20, height=2, command=rock)
    b1.place(x=100, y=300)

    b2 = tk.Button(frame, text="Paper", font="normal 12", width=20, height=2, command=paper)
    b2.place(x=300, y=300)

    b3 = tk.Button(frame, text="Scissors", font="normal 12", width=20, height=2, command=scissors)
    b3.place(x=500, y=300)

    window.mainloop()


def ending_page(flag):
    frame = tk.Frame(window)
    frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    canvas = tk.Canvas(frame, bg="black")
    canvas.pack(fill=tk.BOTH, expand=True)

    def create_sparkles_w():
        canvas.delete("sparkle")
        for _ in range(50):
            x = randint(0, frame.winfo_width())
            y = randint(0, frame.winfo_height())
            size = randint(1, 5)
            color = "#{:06x}".format(randint(0, 0xFFFFFF))
            canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline="", tags="sparkle")
        frame.after(100, create_sparkles_w)

    def create_sparkles_l():
        canvas.delete("sparkle")
        for _ in range(50):
            x = randint(0, frame.winfo_width())
            y = randint(0, frame.winfo_height())
            size = randint(1, 5)
            color = "red"
            canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline="", tags="sparkle")
        frame.after(100, create_sparkles_l)

    def yes():
        frame.pack_forget()
        global user_score
        global comp_score
        global score_value
        user_score = 0
        comp_score = 0
        score_value = 0
        start_page()

    def no():
        window.destroy()

    global user_score
    global comp_score

    if flag:
        pygame.mixer.music.load("mus/victory.mp3")
        pygame.mixer.music.play(1)
        create_sparkles_w()
        text = tk.Label(frame, text="Поздравляю, вы ВЫИГРАЛИ!!!", font="normal 40", borderwidth=2, relief="solid", bg="black", fg="white")
        text.place(x=100, y=100)

    else:
        pygame.mixer.music.load("mus/fail.mp3")
        pygame.mixer.music.play(1)
        create_sparkles_l()
        text = tk.Label(frame, text="К сожалению, вы проиграли :(", font="normal 40", borderwidth=2, relief="solid", bg="black", fg="white")
        text.place(x=100, y=100)

    text2 = tk.Label(frame, text=f"Со счетом: {user_score}:{comp_score}", font="normal 30", borderwidth=2, relief="solid", bg="black", fg="white")
    text2.place(x=290, y=165)

    text3 = tk.Label(frame, text="Хотите сыграть еще?", font="normal 30", borderwidth=2, relief="solid", bg="black", fg="white")
    text3.place(x=235, y=250)

    b_yes = tk.Button(frame, text="Да", font="normal 30", command=yes)
    b_yes.place(x=295, y=300)

    b_no = tk.Button(frame, text="Нет", font="normal 30", command=no)
    b_no.place(x=395, y=300)

start_page()