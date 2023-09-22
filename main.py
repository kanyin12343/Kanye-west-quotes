from tkinter import *
import requests


#Function to display Knaye west quote
def get_quote():
    pass
    response = requests.get(url="https://api.kanye.rest") # Make a GET call to the quotation API for Kanye West.
    response.raise_for_status() #Raise an exception if the request is accompanied by one.
    data = response.json() # Parse the JSON data that was returned.
    quotes  = data["quote"] # Take the Kanye West quotation out of the JSON information.
    canvas.itemconfig(quote_text, text = quotes) #Update the quote with # the new quote # on the canvas.


# Creates the main application window.
window = Tk()
window.title("Kanye Says...") #window title
window.config(padx=50, pady=50) # padding to the window

#Creating canvas
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")# loads background image
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0) #displays the canvas

kanye_img = PhotoImage(file="kanye.png") #Displays the Kanye west image
# Make a button with Kanye's picture that, when clicked, calls the get_quote function.
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0) #displays the button in the window.



window.mainloop()
