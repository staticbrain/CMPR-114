# Exercise 1

'''

import tkinter

class MyGUI:

    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Set the width of the main window
        self.main_window.geometry('400x200')  # Increase the width to 400 pixels

        # Display a title
        self.main_window.title('My First GUI')

        # Enter the tkinter main loop
        tkinter.mainloop()

# Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()

    '''

# Exercise 2

'''
import tkinter

class MyGUI:

    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create a label widget for last name
        self.last_name_label = tkinter.Label(self.main_window, text='Last Name:')
        self.last_name_label.pack()

        # Create a label widget for first name
        self.first_name_label = tkinter.Label(self.main_window, text='First Name:')
        self.first_name_label.pack()

        # Create a label widget for age
        self.age_label = tkinter.Label(self.main_window, text='Age:')
        self.age_label.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

# Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
'''

# Exercise 3

'''
# This program demonstrates internal padding
import tkinter

class MyGUI:

    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create two label widgets with solid borders
        self.label1 = tkinter.Label(self.main_window, text='Hello World!', borderwidth=1, relief='solid')
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program', borderwidth=1, relief='solid')
        
        # Create two additional labels with positive quotes
        self.label3 = tkinter.Label(self.main_window, text='You can do anything!', borderwidth=1, relief='solid')
        self.label4 = tkinter.Label(self.main_window, text='You\'re a wonderful person!', borderwidth=1, relief='solid')

        # Display the labels with 20 pixels of horizontal and vertical internal padding
        self.label1.pack(ipadx=20, ipady=20)
        self.label2.pack(ipadx=20, ipady=20)
        
        # Add padding to the additional labels for a neat display
        self.label3.pack(ipadx=20, ipady=20)
        self.label4.pack(ipadx=20, ipady=20)

        # Enter the tkinter main loop
        tkinter.mainloop()

# Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
 '''

# Exercise 4
'''
import tkinter
import tkinter.messagebox

class MyGUI:

    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create a button widget. The text 'Click Me!' should appear on the face of the button.
        # The do_something method should be executed when the user clicks the button.
        self.my_button = tkinter.Button(self.main_window, text='Click Me!', command=self.do_something)

        # Create three additional buttons with different positive quotes.
        self.button1 = tkinter.Button(self.main_window, text='Quote 1', command=self.display_quote1)
        self.button2 = tkinter.Button(self.main_window, text='Quote 2', command=self.display_quote2)
        self.button3 = tkinter.Button(self.main_window, text='Quote 3', command=self.display_quote3)

        # Create a Quit button. When this button is clicked, the root widget's destroy method is called
        # The main_window variable references the root widget so the callback function is self.main_window.destroy
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        # Pack the buttons.
        self.my_button.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.quit_button.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The do_something method is a callback function for the button widget
    def do_something(self):
        # Display an info dialog box
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the "Click Me!" button.')

    # Display positive quotes when the respective buttons are clicked
    def display_quote1(self):
        tkinter.messagebox.showinfo('Positive Quote', 'Quote 1: "You\'re doing great! Keep it up!"')

    def display_quote2(self):
        tkinter.messagebox.showinfo('Positive Quote', 'Quote 2: "You can do anything you set your mind to!"')

    def display_quote3(self):
        tkinter.messagebox.showinfo('Positive Quote', 'Quote 3: "You\'ve got this!"')

# Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
'''

# Exercise 5
'''
import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text = 'Enter a distance in kilometers: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        # Pack the top frame's widgets
        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')

        # Create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Convert', command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        # Pack the buttons
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The convert method is a callback function for the calculate button
    def convert(self):
        # Get the value entered by the user into the kilo_entry widget
        kilo = float(self.kilo_entry.get())

        # Convert km to miles
        miles = kilo * .6214

        # Display the results in an info dialog box
        tkinter.messagebox.showinfo('Results', str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles.')

# Create an instance of the KiloConverterGUI class
if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()
'''

# Exercise 6

import tkinter

class KiloConverterGUI:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text = 'Enter a distance in kilometers: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        # Pack the top frame's widgets
        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')

         # Create the widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame, text = 'Converted to miles: ')

        # We need a StringVar object to associate with an output label. Use the object's set method to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create a label and associate it with StringVar. Any value stored in this object will automatically be displayed in the label
        self.miles_label = tkinter.Label(self.mid_frame, textvariable = self.value)

        # Pack the middle frame's widgets
        self.descr_label.pack(side = 'left')
        self.miles_label.pack(side = 'left')

        # Create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Convert', command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        # Pack the buttons
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The convert method is a callback function for the calculate button
    def convert(self):
        # Get the value entered by the user into the kilo_entry widget
        kilo = float(self.kilo_entry.get())

        # Convert km to miles
        miles = kilo * .6214

        # Convert miles to string and store it in the StringVar object. This will automatically update the miles_label widget
        self.value.set(miles)

# Create an instance of the KiloConverterGUI class
if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()

