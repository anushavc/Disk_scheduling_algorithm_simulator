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

root = tk.Tk()
root.title("Disk simulator")

def graph():
    os.system('maingui.py')

def recomm():
    os.system('recommender.py')

root.configure(bg="#ffeeec")
#disk simulator heading
a = tk.Label(root, text="Disk Scheduling Simulator", fg="black",bg="#ffeeec",font = ('Helvetica', 30), wraplength = 1300).pack(pady=15,padx=30)
tk.Label(root,text="This is a simulator that demonstrates the three common disk scheduling algorithms which are SCAN,SSTF and FCFS",fg="black",bg="#ffeeec",font = (' Helvetica', 11)).pack()
tk.Label(root,text="Choose any of the options below",fg="black",bg="#ffeeec",font = (' Helvetica', 12)).pack()
sub_btn = tk.Button(root,  wraplength=100,text='To generate a chart showing the sequence in which the requests have been serviced',command=graph,height=10,width=20,bg="#EAC2B0",fg="black",font = (' Helvetica', 12)).pack(padx=10,pady=10)
sub_btn = tk.Button(root,  wraplength=100,text='To find the best algorithm for a given disk sequence',command=recomm,height=7,width=20,fg="black",bg="#EAC2B0",font = (' Helvetica', 12)).pack(padx=10,pady=10)
root.mainloop()