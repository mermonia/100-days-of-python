import tkinter as tk

# ---------------------------- CONSTANTS -------------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Nunito"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
is_timer_on = False

# ---------------------------- TIMER RESET -----------------------------#


def restart_timer():
    global is_timer_on, reps
    is_timer_on = False
    reps = 0
    canvas.itemconfigure(timer_text, text="00:00")
    label_header.configure(text="Timer", fg=GREEN)
    label_checkmark.configure(text="")

# ---------------------------- TIMER MECHANISM -------------------------#


def start_timer():
    global is_timer_on, reps

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if is_timer_on:
        return

    is_timer_on = True

    match reps:
        case 0 | 2 | 4 | 6:
            count_down(work_secs, True)
            label_header.configure(text="Work", fg=RED)
            reps += 1
        case 1 | 3 | 5:
            count_down(short_break_secs, False)
            label_header.configure(text="Break", fg=PINK)
            reps += 1
        case 7:
            count_down(long_break_secs, False)
            label_header.configure(text="Break", fg=PINK)
            reps = 0


# ---------------------------- COUNTDOWN MECHANISM ---------------------#


def count_down(seconds, is_work_session):
    global is_timer_on

    if not is_timer_on:
        return

    if seconds >= 0:
        mins = seconds // 60
        secs = seconds % 60
        canvas.itemconfigure(timer_text, text=f"{mins:02d}:{secs:02d}")
        window.after(1000, count_down, seconds-1, is_work_session)
    else:
        if is_work_session:
            label_checkmark.configure(text=label_checkmark.cget("text") + "✓")
        is_timer_on = False
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, background=YELLOW)


label_header = tk.Label(text="Timer", fg=GREEN, bg=YELLOW,
                        font=(FONT_NAME, 30, "bold"))
label_header.grid(column=1, row=0)


tomato_image = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 30, "bold"))
canvas.configure(background=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)


def on_start_button_clicked():
    start_timer()


def on_reset_button_clicked():
    restart_timer()


button_start = tk.Button(text="Start", command=on_start_button_clicked)
button_start.grid(column=0, row=2)

button_reset = tk.Button(text="Reset", command=on_reset_button_clicked)
button_reset.grid(column=2, row=2)


label_checkmark = tk.Label(text="", bg=YELLOW, fg=GREEN,
                           font=(FONT_NAME, 30, "bold"))
label_checkmark.grid(column=1, row=3)


window.mainloop()
