from future.moves import tkinter as tk
import numpy as np
from tkinter import filedialog, Text
import tkinter.font as tkFont
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import sys
import plotly
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objects as go

# function to plot the graph
def simulate(x, y):
    x = x
    y = y
    x1=[]
    x1=x
    x1.append(0)
    x1.append(199)
    frames = []
    for i in range(0, len(x) + 1):
        x_axis_frame = x[:i]
        y_axis_frame = y[:i]
        curr_frame = go.Frame(data=[go.Scatter(x=x_axis_frame, y=y_axis_frame, line_color="black")])
        print(curr_frame)
        frames.append(curr_frame)

    fig = go.Figure(
        data=go.Scatter(x=x, y=y),
        layout={"xaxis": {"mirror": "allticks", 'side': 'top','tickvals':x1}, "yaxis": {"showticklabels": False},
                "title": "Disk scheduling algorithm chart",
                "updatemenus": [
                    {"type": "buttons", "buttons": [{"method": "animate", "label": "play again", "args": [None, {
                        "frame": {"duration": 500, "redraw": False}, }]}]}]
                },
        frames=frames
    )
    fig.layout.plot_bgcolor = '#ffeeec'
    fig.layout.paper_bgcolor = '#fff'
    fig.update_xaxes(range=[0, 200])
    fig.update_yaxes(range=[0, max(y) + 1])
    fig.update_layout(transition_duration=3000)
    return fig


root = tk.Tk()
root.title("Disk simulator")
root.configure(bg="#ffeeec")
# disk simulator heading
a = tk.Label(root, text="Disk Scheduling Simulator", fg="black", bg="#ffeeec", font=('Helvetica', 15),
             wraplength=1300).pack(pady=10, padx=20)
# enter the disk sequence heading
b = tk.Label(root, text="Enter the disk sequence:\n (make sure that the integers are comma seperated ex:12,13,14)",
             fg="black", bg="#ffeeec", font=(' Helvetica', 10))
b.pack()

# variables
name_var = tk.StringVar()
name_var1 = tk.IntVar()
randarr = tk.StringVar()
r = tk.IntVar()


# scan algorithm
def SCAN(head, req, given_direction):
    requests = list(req)
    current = head
    direction = given_direction
    seekOperations = 0
    final = []
    final.append(head)
    print(final)
    tk.Label(text="Execution order:   ", fg="black", bg="#ffeeec", font=(' Helvetica', 9)).pack()
    while requests:
        if current in requests:
            print(requests)
            tk.Label(text=(str(current)), fg="black", bg="#ffeeec", font=(' Helvetica', 9)).pack()
            final.append(current)
            requests.remove(current)
            if not requests:
                break
        if direction == "left" and current > 0:
            current -= 1
        if direction == "right" and current < 200:
            current += 1
        seekOperations += 1
        if current == 0:
            tk.Label(text='0', fg="black", bg="#ffeeec", font=(' Helvetica', 9)).pack()
            final.append(0)
            direction = "right"
        if current == 199:
            tk.Label(text='199', fg="black", bg="#ffeeec", font=(' Helvetica', 9)).pack()
            final.append(199)
            direction = "left"
    tk.Label(text="Total seek operations :  " + str(seekOperations), width=40, font=(' Helvetica', 9)).pack()
    y = []
    for i in range(len(final), 0, -1):
        y.append(i)
    fig=simulate(final, y)
    fig.update_layout(title_text="Disk sequence chart using SCAN algorithm")
    plot(fig)
    tk.Button(root, text="Reset", bg="#EAC2B0", fg="black", command=reset, font=(' Helvetica', 11)).pack()


def SSTF(head, req):
    requests = list(req)
    current = head
    seekOperations = 0
    final = []
    final.append(head)
    tk.Label(text="Execution order:   ", fg="black", bg="#ffeeec", font=(' Helvetica', 9)).pack()
    while requests:
        closestReq = abs(current - requests[0])
        closestIndex = 0
        for x in range(1, len(requests)):
            if abs(current - requests[x]) < closestReq:
                closestReq = abs(current - requests[x])
                closestIndex = x
        seekOperations += abs(current - requests[closestIndex])
        current = requests[closestIndex]
        tk.Label(text=(str(current)), fg="black", bg="#ffeeec", font=(' Helvetica', 9)).pack()
        final.append(current)
        requests.remove(current)
    y = []
    for i in range(len(final), 0, -1):
        y.append(i)
    fig=simulate(final, y)
    fig.update_layout(title_text="Disk sequence chart using SSTF algorithm")
    plot(fig)
    tk.Label(text="Total seek operations:  " + str(seekOperations), width=40, font=(' Helvetica', 9)).pack()
    tk.Button(root, text="Reset", bg="#EAC2B0", fg="black", command=reset, font=(' Helvetica', 11)).pack()
    return seekOperations


def FCFS(head, requests):
    current = head
    seekOperations = 0
    final = []
    final.append(head)
    tk.Label(text="Execution order:   ", fg="black", bg="#ffeeec", font=(' Helvetica', 9)).pack()
    for x in range(len(requests)):
        seekOperations += abs(current - requests[x])
        current = requests[x]
        tk.Label(text=(str(current)), fg="black", bg="#ffeeec", font=(' Helvetica', 9)).pack()
        final.append(current)
    y = []
    for i in range(len(final), 0, -1):
        y.append(i)
    fig=simulate(final, y)
    fig.update_layout(title_text="Disk sequence chart using FCFS algorithm")
    plot(fig)
    tk.Label(text="Total seek operations :  " + str(seekOperations), width=40, font=(' Helvetica', 9)).pack()
    tk.Button(root, text="Reset", bg="#EAC2B0", fg="black", command=reset, font=(' Helvetica', 11)).pack()


# to get random array
def randomize():
    global randarr
    randarr = list(np.random.randint(1, 200, 8))
    converted_list = [str(element) for element in randarr]
    e.insert(0, ",".join(converted_list))# need to figure out why 0 is there


# a dropdown menu to choose the direction of the track
OPTIONS = ["left", "right"]
variable = tk.StringVar(root)
variable.set(OPTIONS[0])

# input from the checkboxes
CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
CheckVar3 = tk.IntVar()
CheckVar1.set(0)
CheckVar2.set(0)
CheckVar3.set(0)


# to get the input from the user
def submit():
    global set1
    global head_pos
    name = e.get()
    head_pos = int(f.get())
    parts = name.split(",")
    list = [int(i) for i in parts]
    set1 = list
    name_var.set("")
    e.insert(0, name)
    if (CheckVar1.get() != 0):
        SCAN(head_pos, set(set1), variable.get())
    if (CheckVar2.get() != 0):
        FCFS(head_pos, set1)
    if (CheckVar3.get() != 0):
        SSTF(head_pos, set(set1))


def reset():
    os.execv(sys.executable, ['python'] + sys.argv)
    return


def clear():
    e.delete(0, "end")
    return


e = tk.Entry(root, textvariable=name_var, width=50)
e.pack()
c = tk.Radiobutton(root, text="Randomize", bg="#ffeeec", fg="black", command=randomize, font=(' Helvetica', 11)).pack()

clr = tk.Button(root, text='Clear', bg="#EAC2B0", fg="black", command=clear, font=(' Helvetica', 10)).pack()

tk.Label(root, text="Enter the intial head position:", fg="black", bg="#ffeeec", font=(' Helvetica', 11)).pack()
f = tk.Entry(root, textvariable=name_var1, font=('calibre', 10, 'normal'), width=50)
f.pack()

# to choose the algo
tk.Label(root, text="Choose one algorithm", fg="black", bg="#ffeeec", font=(' Helvetica', 11)).pack()

C2 = tk.Checkbutton(root, text="FCFS", variable=CheckVar2, bg="#EAC2B0", fg="black", onvalue=1, offvalue=0, height=1,
                    width=20).pack()

C3 = tk.Checkbutton(root, text="SSTF", variable=CheckVar3, onvalue=1, offvalue=0, height=1, bg="#EAC2B0", fg="black",
                    width=20).pack()

C1 = tk.Checkbutton(root, text="SCAN", variable=CheckVar1, bg="#EAC2B0", fg="black", onvalue=1, offvalue=0, height=1,
                    width=20).pack()

tk.Label(root, text="For the SCAN algorithm, choose the direction", fg="black", bg="#ffeeec",
         font=(' Helvetica', 11)).pack()

w = tk.OptionMenu(root, variable, *OPTIONS)
w.config(bg="#EAC2B0", fg="black")
w.pack()

sub_btn = tk.Button(root, bg="#EAC2B0", fg="black", text='Submit', command=submit, font=(' Helvetica', 10))
sub_btn.pack(pady=10)

root.mainloop()