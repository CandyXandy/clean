#####################################################################
# Alexander Robertson - COSC110     |       21/05/2022              #
# Assignment 4 - clean.py           |                               #
#####################################################################
# Developed for the mayor of CodeTown to help deal with the         #
# newly-found cleanliness problem of city's bus network.            #
# Presents a GUI for the user to rate the cleanliness of the bus    #
# from 1 to 5.                                                      #
# Gives an average of the ratings once input has been received.     #
#####################################################################

import tkinter as tk
from tkinter import ttk

ratings = []   # List of ratings
count = len(ratings)   # Number of ratings


def cal_average():
    """
    Calculates the average of the ratings.

            Takes no arguments.

    After making sure we're using the global variables ratings and count,
    we set a variable to 0 before iterating through the ratings list.
    Then, in every iteration of the loop, we add the current rating to the
    running total and divide the running total by the number of ratings.
    This is the average, which is returned.
    """
    global ratings, count  # We need to use the global variables
    sum = 0
    for num in ratings:
        sum = sum + num

    average = sum / count
    return average


def add_rating(*args):
    """
    Adds the rating to the ratings list.

    This function is called by the show_average function.
    When called, it takes the current value of the slider,
    and converts it to a float. We then make sure we're using
    the global variables ratings and count. The ratings list
    is appended by the current rating and the count is
    incremented by 1. Then, we call the cal_average function,
    converting the return value to a string formatted to 2 decimal
    places and setting the text of the average label to the string.
    """
    input = rating.get()  # Get the current value of the slider
    input = float(input)  # Convert to a float
    global ratings, count  # We need to use the global variables
    ratings.append(input)  # Add the rating to the list
    count = len(ratings)  # Increment the count
    avg = cal_average()  # Calculate the average
    avg = f'{avg:.2f}'  # Format the average to 2 decimal places
    avg_display.set(avg)  # Set the text of the average label to the average


def show_average(*args):
    """
    Displays the average of the ratings.

    Called when the user clicks the submit button.
    Shows the avg_label Label with the average of the ratings.
    """
    avg_label = tk.Label(frame,  # The label to show upon being called
                         text="This bus has an average cleanliness rating of:",
                         font=("Arial", 16))
    avg_label.grid(column=2, row=4, sticky=(tk.S), padx=5)
    add_rating()  # Add the rating to the ratings list


root = tk.Tk()  # Creates the main window
root.title("Bus Cleanliness Rater")  # Sets the title of the window
root.minsize(width=640, height=480)  # Sets the minimum size of the window


# Some widgets to be used.
frame = ttk.Frame(master=root,  # Creates the frame
                  padding=(3, 3, 12, 12))
title_label = ttk.Label(master=frame,  # The title text at the top of the GUI
                        text="Bus Cleanliness Rater",
                        font=("Arial", 25))  # Sets the font and size
info = ttk.Label(master=frame,         # Instruction to the user
                 text="Please rate the cleanliness of this bus from 1 to 5:",
                 font=("Arial", 16))
happy_face = ttk.Label(master=frame,    # Happy face for the end of the slider
                       text=":-)",
                       font=("Arial", 16))
sad_face = ttk.Label(master=frame,      # Sad face for the beginning of the slider
                     text=":-(",
                     font=("Arial", 16))


# Variables to be used by widgets
rating = tk.StringVar()  # Creates the StringVar that the slider will use
rating.set("1")          # Sets the default value of the slider
avg_display = tk.StringVar()  # Creates the StringVar that the average label will use


# Widgets that require the above variables
# We need to use the tk version of scale rather than ttk, as ttk doesn't support
# resolution. Implementing it myself would take up more time than just using tk.
rating_scale = tk.Scale(master=frame,  # Creates the slider | Used to obtain rating value
                        variable=rating,  # Sets the variable to the StringVar created above
                        resolution=1,   # Sets the slider to increment by 1 at a time.
                        from_=1, to=5,  # Sets the range of the slider
                        orient="horizontal",  # Sets the slider to be horizontal
                        length=200)
avg_show = ttk.Label(master=frame,  # The label to show upon being called
                     textvariable=avg_display,  # Sets the variable to the StringVar created above
                     font=("Arial", 16))
submit_btn = ttk.Button(master=frame,   # The button to be called upon being clicked
                        text="Submit",
                        command=show_average)  # Sets the command to the show_average function


# Sets the grid of the widgets, with their column/row spanning if necessary and their sticky /padding
frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
title_label.grid(column=2, row=1, columnspan=2, sticky=(tk.N), padx=5)
info.grid(column=2, row=2, stick=(tk.N), padx=5, pady=5)
happy_face.grid(column=1, row=2, sticky=(tk.E))
sad_face.grid(column=3, row=2, sticky=(tk.W))
rating_scale.grid(column=2, row=2, rowspan=3, sticky=(tk.W, tk.E), padx=5, pady=5)
submit_btn.grid(column=2, row=3, sticky=(tk.S), padx=5)
avg_show.grid(column=2, row=5, sticky=(tk.N, tk.S), padx=5, pady=5)


# Sets the columns/rows to be resizable, weight determing how much the widget should take up
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(2, weight=3)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=2)
frame.rowconfigure(2, weight=3)
frame.rowconfigure(3, weight=2)
frame.rowconfigure(4, weight=1)
frame.rowconfigure(5, weight=1)

root.mainloop()  # Starts the main loop
