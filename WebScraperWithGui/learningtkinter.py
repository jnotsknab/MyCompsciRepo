##ts is a 18 hr tkinter course hoyl fuck
#mile to kilometer converter example

#basics
#need 3 componenets major componenets(widgets(text, button, menu), layout)
##layout(columns and rows etc), style(color, font, etc)

import tkinter as tk
##ttk has widgets
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    kilometer = mile_input * 1.61
    output_string.set(kilometer)

#window to put stuff on
window = ttk.Window(themename= 'solar')
#window title
window.title('dick')
#sets size
window.geometry('300x200')

#title(master is window because the label needs something to refer to ie the gui window)
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 20 bold')
#we need to pack the label to pack it onto the window
title_label.pack()

#input field/dropdown menu
#we now have a frame we can put widgets into

#we must now place the frame itself in the window once the entry and button are within the frame
input_frame = ttk.Frame(master = window)
#seperate variable that can store and update values for entry field
entry_int = tk.IntVar()
#master for entry and button are input frame since they will be inside the input frame
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
#we want to do something when the button is clicked so we must create a function for it
#only want to pass function button click itself will call the fucntion
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
#do it using pack, pack places widgets below each other
#pad adds spacing on 
entry.pack(side = 'left', padx = 5)
button.pack(side = 'left', padx= 5)
#we want entry widget and button next to eachother so pass side argument to pack
input_frame.pack(pady = 10)

#we need the output widget
#we need to create the output 
#stores string inside an integer
output_string = tk.StringVar()
output_label = ttk.Label(master = window,
                          text = 'Output',
                          font = 'Calibri 20 bold',
                          textvariable= output_string)
#text variable overides whatever text is inside the label, so we can update label dynamically
output_label.pack(pady = 5)






#create mainloop to see window
window.mainloop()
