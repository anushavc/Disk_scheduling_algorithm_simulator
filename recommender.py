from future.moves import tkinter as tk
import numpy as np
from tkinter import filedialog, Text
import tkinter.font as tkFont
from tkinter import ttk
import matplotlib.pyplot as plt
import os
import sys
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot

root = tk.Tk()
root.title("Disk simulator")
root.configure(bg="#ffeeec")

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


# disk simulator heading
a = tk.Label(root, text="Disk Scheduling Simulator", fg="black", bg="#ffeeec", font=('Helvetica', 15), wraplength=1300)
a.pack(pady=30)

# enter the disk sequence heading
b = tk.Label(root, text="Enter the disk sequence:\n (make sure that the integers are comma seperated ex:12,13,14)",
             fg="black", bg="#ffeeec", font=('Helvetica', 11))
b.pack()

# variables
name_var = tk.StringVar()
name_var1 = tk.IntVar()
randarr = tk.StringVar()
r = tk.IntVar()


# a function to compare the three algorithms
def compare(head, req,given_direction):
    requests = list(req)
    current = head
    direction = given_direction
    seekOperations = 0
    final = []
    final.append(head)
    while requests:
        if current in requests:
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
            final.append(0)
            direction = "right"
        if current == 199:
            final.append(199)
            direction = "left"
    y = []
    for i in range(len(final), 0, -1):
        y.append(i)
    fig=simulate(final, y)
    fig.update_layout(title_text="Disk sequence chart using SCAN algorithm")
    plot(fig)
    tk.Label(text="Total seek operations for SCAN:  " + str(seekOperations), width=40, fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()

    requests1 = list(req)
    current1 = head
    seekOperations1 = 0
    final1 = []
    final1.append(head)
    while requests1:
        closestReq = abs(current1 - requests1[0])
        closestIndex = 0
        for x in range(1, len(requests1)):
            if abs(current1 - requests1[x]) < closestReq:
                closestReq = abs(current1 - requests1[x])
                closestIndex = x
        seekOperations1 += abs(current1 - requests1[closestIndex])
        current1 = requests1[closestIndex]
        final1.append(current1)
        requests1.remove(current1)
    y1 = []
    for i in range(len(final1), 0, -1):
        y1.append(i)
    fig1=simulate(final1, y1)
    fig1.update_layout(title_text="Disk sequence chart using SSTF algorithm")
    plot(fig1)
    tk.Label(text="Total seek operations for SSTF are :  " + str(seekOperations1), width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()

    current2 = head
    requests2 = list(req)
    seekOperations2 = 0
    final2 = []
    final2.append(head)
    for x in range(len(requests2)):
        seekOperations2 += abs(current2 - requests2[x])
        current2 = requests2[x]
        final2.append(current2)
    y2 = []
    for i in range(len(final2), 0, -1):
        y2.append(i)
    fig2=simulate(final2,y2)
    fig2.update_layout(title_text="Disk sequence chart using FCFS algorithm")
    plot(fig2)
    tk.Label(text="Total seek operations for FCFS:  " + str(seekOperations2), width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()

    # comparing the seek operations
    if (seekOperations > seekOperations1):
        if (seekOperations1 > seekOperations2):
            tk.Label(text="FFCS has the shortest seek time", width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()
        elif(seekOperations1==seekOperations2):
            tk.Label(text="FFCS and SSTF have the shortest seek time", width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()
        else:
            tk.Label(text="SSTF has the shortest seek time", width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()
    elif(seekOperations==seekOperations1):
         tk.Label(text="SCAN and SSTF have the shortest seek time", width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()
    else:
        if (seekOperations > seekOperations2):
            tk.Label(text="FFCS has the shortest seek time", width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()
        elif(seekOperations==seekOperations2):
            tk.Label(text="FFCS and SCAN have the shortest seek time", width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()
        else:
            tk.Label(text="SCAN has the shortest seek time", width=40,fg="black", bg="#ffeeec", font=(' Helvetica', 10)).pack()

    tk.Button(root, text="Reset", bg="#EAC2B0", fg="black", command=reset, font=(' Helvetica', 11)).pack()

# to get a random array
def randomize():
    global randarr
    randarr = list(np.random.randint(1, 200, 5))
    converted_list = [str(element) for element in randarr]
    e.insert(0, ",".join(converted_list))
    return True


# to get the input from the user for disk sequence
def submit():
    global set1
    global head_pos
    name = e.get()
    head_pos = int(f.get())
    parts = name.split(",")
    list = [int(i) for i in parts]
    set1 = list
    print(set1)
    print(head_pos)
    name_var.set("")
    e.insert(0, name)
    compare(head_pos,set1,variable.get())

#to clear the random array
def clear():
    e.delete(0, "end")
    return


def reset():
    os.execv(sys.executable, ['python'] + sys.argv)
    return

# randomize button
e = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'), width=50)
e.pack()
c = tk.Radiobutton(root, text="Randomize", fg="black", bg="#ffeeec", command=randomize).pack(pady=2)
clr = tk.Button(root, text = 'clear', command=clear,font = (' Helvetica', 10),bg="#EAC2B0").pack()

# head pos button
tk.Label(root, text="Enter the intial head position:", fg="black", bg="#ffeeec", font=('Helvetica', 11)).pack(padx=3)
f = tk.Entry(root, textvariable=name_var1, font=('calibre', 10, 'normal'), width=50)
f.pack()

# a dropdown menu to choose the direction of the track
DIRECTIONS_ARRAY = ["left", "right"]
variable = tk.StringVar(root)
variable.set(DIRECTIONS_ARRAY[0])


tk.Label(root,text="Choose the direction of SCAN algorithm:",fg="black", bg="#ffeeec",font=(' Helvetica', 11)).pack()
w = tk.OptionMenu(root, variable, *DIRECTIONS_ARRAY)
w.config(bg="#EAC2B0", fg="black")
w.pack()
sub_btn = tk.Button(root, bg="#EAC2B0", fg="black", text='Submit', command=submit, font=(' Helvetica', 11))
sub_btn.pack(pady=10)

root.mainloop()