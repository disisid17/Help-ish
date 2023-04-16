import tkinter as tk
import tkinter.font as tkFont

from Chatbot import Chatbot # This import statement WORKS

# We were unable to finish the UI, but the Chatbot class from Chatbot.py successfully implements 
# the ChatGPT API to respond in various degrees of helpfulness.

class App:
    def __init__(self, root):
        #setting title
        root.title("Unhelpful Chatbot")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Message entry box
        GLineEdit_287=tk.Entry(root)
        GLineEdit_287["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_287["font"] = ft
        GLineEdit_287["fg"] = "#000000"
        GLineEdit_287["justify"] = "left"
        GLineEdit_287["text"] = "Enter message here"
        GLineEdit_287.place(x=20,y=450,width=460,height=30)

        # Big Message Box
        GMessage_350=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_350["font"] = ft
        GMessage_350["fg"] = "#000000"
        GMessage_350["justify"] = "left"
        GMessage_350["text"] = " "
        GMessage_350.place(x=20,y=30,width=540,height=408)

        # Enter Button
        GButton_268=tk.Button(root)
        GButton_268["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_268["font"] = ft
        GButton_268["fg"] = "#000000"
        GButton_268["justify"] = "center"
        GButton_268["text"] = "Enter"
        GButton_268.place(x=490,y=450,width=66,height=30)
        GButton_268["command"] = self.GButton_268_command

    def GButton_268_command(self): # when the button is pressed
        #Chatbot.question = self.GLineEdit_287["text"] # get the text from the entry box
    #    print(Chatbot.question)
        #entry = GLineEdit_287.get()
        #print(entry)
        
        print("command")
        #self.GMessage_350["text"] = "command"
        #GMessage_350["text"] = "command"

        label = tk.Label(root, text= "Message recieved", anchor="s", justify="left")
        #label = tk.Entry(GMessage_350, text= "Message recieved", anchor="s", justify="left")
        #this creates a new label to the GUI
        label.pack() 


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
