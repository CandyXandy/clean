# Clean.py

## Developed by Alexander Robertson
## Date: 21/05/2022
## Programming Assignment 3 - COSC110  
## Preface:
This program was built for the Mayor of CodeTown for the express purpose of obtaining information on the cleanliness
of the city's busses. This does this by asking the customers of the busses if they are clean or not. It grabs each input and displays an average of all inputs received.  
This information can then be stored externally, and used to determine the cleanliness of the city's busses on each individual bus route.

## Contents:
- Pre-Requesites
- How to run
- How to use
- How it works

## Pre-Requesites:
- Python 3  
You will need Python 3 installed on the computer this program will be running on.  
This program will support a touch screen, as well as a mouse interface.  
No keyboard functionality is included.  
You can obtain Python 3 by clicking [here](http://python.org/downloads/).  
Make sure you install the correct version for your operating system.  

## How to run:
In your terminal, navigate to the directory where you have Clean saved.  
Then, type python3 clean.py into the terminal. 
The program should begin to run.

## How to use:
This program is very simple from the user perspective.  
The user will be asked to input whether or not the bus is clean or not.  
This is done via a slider on the included Graphic User Interface(GUI), and then pressing or clicking on the "Submit" button.  
The program will then display the average of all inputs received.  
That's it! The driver can then record the average information received and either write it down or store it in a seperate file.  
There shouldn't be any way for the user to generate an error, as the program is self-contained in the GUI environment.

## How it works:
This program is heavily dependant on the tkinter library for Python.
The GUI is built using the tkinter library.  
There are 3 functions to handle the user input, and some variables which store the information.
This information is used by the functions and some of the widgets of the GUI to display the average of the inputs.

These variables are:

```Python
ratings = []   # List of ratings
count = len(ratings)   # Number of ratings

rating = tk.StringVar()  # Creates the StringVar that the slider will use
avg_display = tk.StringVar()  # Creates the StringVar that the average label will use
```

The first two are python variables to store the information.  
The last 2 are tkinter variables to display the information on the GUI.  


The first function we will talk about is the show_average function, displayed below.
```python
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
```

This is initially called when the submit button is pressed or clicked. It is responsible for displayed the average of the ratings. Conceptually simple, but this ties in to and calls the next function we will go over, the add_rating function.

```python
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
```
This function converts the slider value to a float, and then appends the rating to the ratings list.
It then uses the global variables to update the count and the average.   
It calls the cal_average function which we will go over in a moment. Once it has received a return value from that function, it converts the return value to a string formatted to 2 decimal places and sets the text of the average label to the string.

Now we'll go over the cal_average function.
```python
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
```
This function is responsible for calculating the average of the ratings. It iterates over every rating in the ratings list, and adds it to a running total. It then divides the running total by the number of ratings. This is the average which is sent back to the add_rating function.  

The rest of the program is specific to the tkinter library, which you can find documentation for [here](https://docs.python.org/3/library/tkinter.html).

One thing to take note of is the value slider. This is done by the tkinter tk.Scake widget.
```python
rating_scale = tk.Scale(master=frame,  # Creates the slider
                        variable=rating,  # Sets the variable to the StringVar created above
                        resolution=1,   # Sets the slider to increment by 1 at a time.
                        from_=1, to=5,  # Sets the range of the slider
                        orient="horizontal",  # Sets the slider to be horizontal
                        length=200)  # Sets the length of the slider
```
We need to use the tk version of scale rather than ttk, as ttk doesn't support
resolution. Implementing it myself would take up more time than just using tk.

I'll now list the widgets we needed to create to build this program.

```python
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
```
All relevant information for the widgets' use is in the comment blocks inside the code block above.

We also had to set their grid positions.
```python
# Sets the grid of the widgets, with their column/row spanning if necessary and their sticky /padding
frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
title_label.grid(column=2, row=1, columnspan=2, sticky=(tk.N), padx=5)
info.grid(column=2, row=2, stick=(tk.N), padx=5, pady=5)
happy_face.grid(column=1, row=2, sticky=(tk.E))
sad_face.grid(column=3, row=2, sticky=(tk.W))
rating_scale.grid(column=2, row=2, rowspan=3, sticky=(tk.W, tk.E), padx=5, pady=5)
submit_btn.grid(column=2, row=3, sticky=(tk.S), padx=5)
avg_show.grid(column=2, row=5, sticky=(tk.N, tk.S), padx=5, pady=5)
```

And we had to set the resizing weights, to allow the program to work with many different kinds of screens.
```python
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
```

When using the tkinter library, you need to call the mainloop function to keep the window open.
```python
root.mainloop()  # Starts the main loop
```
This is important, as it allows the program to run.



Thank you for reading.  
Alexander Robertson.