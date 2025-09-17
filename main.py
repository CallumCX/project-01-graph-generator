import tkinter as tk
from tkinter import ttk

#-----functions needed for different parts of the program-----

def update_window():

    for widget in radio_canvas.winfo_children():
        widget.destroy()

    if graph_type_value.get() == '1':

        values = ['Name', 'Value']
        pie_table = ttk.Treeview(radio_canvas, columns=values, show='headings')

        for i in values:
            pie_table.heading(i, text=i)
            pie_table.column(i, width=70)

        pie_table.place(x=400, y=85)

        title_input_pie = ttk.Entry(radio_canvas)
        title_input_pie.place(x=600, y=100)
        value_input_pie = ttk.Entry(radio_canvas)
        value_input_pie.place(x=600, y=150)

        title_label = ttk.Label(radio_canvas, text='Title:', font=('Arial', 13))
        title_label.place(x=600, y=80)
        value_label = ttk.Label(radio_canvas, text='Value:', font=('Arial', 13))
        value_label.place(x=600, y=130)
    elif graph_type_value.get() == '2':

        values = ['Value']
        line_table = ttk.Treeview(radio_canvas, columns=values, show='headings')

        for i in values:
            line_table.heading(i, text=i)
            line_table.column(i, width=70)

        line_table.place(x=470, y=85)

        value_input_pie = ttk.Entry(radio_canvas)
        value_input_pie.place(x=600, y=100)

        value_label = ttk.Label(radio_canvas, text='Value:', font=('Arial', 13))
        value_label.place(x=600, y=80)

    root_window.update()

def add_to_table_with_two_column(table,title,value):
    table.insert("",tk.END,values=(title,value))



#-----root window generation-----

root_window = tk.Tk()
root_window.title('Graph Generator')
root_window.resizable(False, False)
root_window.tk.call('tk', 'scaling', 1.0)

Frame = tk.Frame(root_window, width=800, height=800)
Frame.pack()

root_canvas = tk.Canvas(Frame, width=800, height=800)
root_canvas.pack()

radio_canvas = tk.Canvas(root_canvas, width=800, height=800)
radio_canvas.pack()

#-----root window widget generation-----

exit_button = tk.Button(Frame, text='Exit', command=root_window.destroy)
exit_button.place(x=10, y=770)

title_label = tk.Label(Frame, text='Welcome to the Graph Generator!',font=('Arial', 15))
title_label.place(x=290,y=10)

graph_type_label = tk.Label(root_window, text='Graph Type:', font=('Arial', 13))
graph_type_label.place(x=15,y=70)

root_canvas.create_rectangle(10, 60, 95, 190, outline='black')

#---graph selection radio widget---

graph_type_value = tk.StringVar(value='0')

pie_radio = ttk.Radiobutton(root_window,text='pie chart',variable=graph_type_value,value='1',command=update_window)
pie_radio.place(x=15,y=100)
line_radio = ttk.Radiobutton(root_window,text='line chart',variable=graph_type_value,value='2',command=update_window)
line_radio.place(x=15,y=120)
bar_radio = ttk.Radiobutton(root_window,text='bar chart',variable=graph_type_value,value='3',command=update_window)
bar_radio.place(x=15,y=140)
scatter_radio = ttk.Radiobutton(root_window,text='scatter chart',variable=graph_type_value,value='4',command=update_window)
scatter_radio.place(x=15,y=160)

#-----radio widget outputs-----


root_window.mainloop()