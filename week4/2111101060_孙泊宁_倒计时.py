
import tkinter as tk

# 数字对应的七段数码管显示
digit_segments = [
    (1, 1, 1, 0, 1, 1, 1),  # 0
    (0, 0, 1, 0, 0, 1, 0),  # 1
    (1, 0, 1, 1, 1, 0, 1),  # 2
    (1, 0, 1, 1, 0, 1, 1),  # 3
    (0, 1, 1, 1, 0, 1, 0),  # 4
    (1, 1, 0, 1, 0, 1, 1),  # 5
    (1, 1, 0, 1, 1, 1, 1),  # 6
    (1, 0, 1, 0, 0, 1, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1),  # 9
]

# 创建窗口
root = tk.Tk()
root.title("倒计时牌")

# 创建七段数码管
def create_digit(canvas, x, y):
    return [
        canvas.create_line(x+20, y, x+50, y),  # a
        canvas.create_line(x+50, y, x+60, y+10),  # b
        canvas.create_line(x+60, y+10, x+60, y+40),  # c
        canvas.create_line(x+50, y+40, x+60, y+50),  # d
        canvas.create_line(x+20, y+50, x+50, y+50),  # e
        canvas.create_line(x+20, y+50, x+10, y+40),  # f
        canvas.create_line(x+10, y+10, x+10, y+40),  # g
    ]

# 显示数字
def show_digit(canvas, segments, digit):
    if digit < 0 or digit > 9:
        print("Invalid digit:",digit)
        return
    for i,seg in enumerate(segments):
        if digit_segments[digit][i]:
            canvas.itemconfig(seg,fill="red")
        else:
            canvas.itemconfig(seg,fill="gray")
    # for i, seg in enumerate(segments):
    #     if digit_segments[digit][i]:
    #         canvas.itemconfig(seg, fill="red")
    #     else:
    #         canvas.itemconfig(seg, fill="gray")

# 创建画布和数字
canvas = tk.Canvas(root, width=240, height=60)
canvas.pack()
digits = [create_digit(canvas, i*40, 10) for i in range(3)]

# 倒计时
countdown = 9
def update_countdown():
    global countdown
    show_digit(canvas, digits[0], countdown // 10)
    show_digit(canvas, digits[1], countdown % 10)
    if countdown == 0:
        show_digit(canvas, digits[2], 0)
    else:
        show_digit(canvas, digits[2], 10)  # 冒号
    countdown -= 1
    if countdown < 0:
        countdown = 9
    canvas.after(500, update_countdown)

update_countdown()

# 运行窗口
root.mainloop()
