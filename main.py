import tkinter as tk
from tkinter import ttk

#-----root window generation-----

root_window = tk.Tk()
root_window.title('Graph Generator')
root_window.resizable(False, False)
root_window.tk.call('tk', 'scaling', 1.0)

Frame = tk.Frame(root_window, width=800, height=800)
Frame.pack()

root_canvas = tk.Canvas(Frame, width=800, height=800)
root_canvas.pack()

#-----root window widget generation-----

exit_button = tk.Button(Frame, text='Exit', command=root_window.destroy)
exit_button.place(x=10, y=770)

title_label = tk.Label(Frame, text='Welcome to the Graph Generator!',font=('Arial', 15))
title_label.place(x=290,y=10)

graph_type_label = tk.Label(root_window, text='Graph Type:', font=('Arial', 13))
graph_type_label.place(x=15,y=70)

root_canvas.create_rectangle(10, 60, 95, 190, outline='black')

#---graph selection radio widget---
graph_type_value = tk.StringVar(value='1')

pie_radio = ttk.Radiobutton(root_window,text='pie chart',variable=graph_type_value,value='1',command=root_window.update)
pie_radio.place(x=15,y=100)
line_radio = ttk.Radiobutton(root_window,text='line chart',variable=graph_type_value,value='2',command=root_window.update)
line_radio.place(x=15,y=120)
bar_radio = ttk.Radiobutton(root_window,text='bar chart',variable=graph_type_value,value='3',command=root_window.update)
bar_radio.place(x=15,y=140)
scatter_radio = ttk.Radiobutton(root_window,text='scatter chart',variable=graph_type_value,value='4',command=root_window.update)
scatter_radio.place(x=15,y=160)

#-----radio widget outputs-----

if graph_type_value.get()=='1':
    pie_table = ttk.Treeview(root_window, columns=['Name', 'Value'], show='headings')



root_window.mainloop()