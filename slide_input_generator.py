# Anosua Roy March 2021 (anosuaa.roy@gmail.com)
# Converts inputs in visual grid into '1511 slide (assignment1 21T1)' compatible inputs
# https://stackoverflow.com/questions/48964879/getting-values-from-multiple-textboxes-in-tkinter

from tkinter import  *
from tkinter import messagebox

SIZE = 15       # SIZE x SIZE grid
root = Tk()
root.minsize(700, 500)
n_array = []    #will be used as 2d array



def add_15_rows():
    global root, n_array

    row_array=[]    #array used to store a row
    n_array.append(row_array)
    y=len(n_array)           

    for x in range(SIZE):
        mainFrame = Frame(root)
        mainFrame.place(width=30, height=30, relx=0.05*x+0.01, rely=0.05*y+0.01)
        mainFrame.grid_propagate(False)

        row_array.append(Entry(mainFrame))
        row_array[x].grid(row=y, column=x, stick="nesw", padx=2,pady=2)
        row_array[x].columnconfigure(0, weight=10) 
        

def getVal():
    final_string = ""
    total_stones = 0

    for row in range(len(n_array)):

        for col in range(SIZE):
            if len(n_array[row][col].get()) != 0:
                total_stones += 1
                final_string = final_string + "\n" +f"{row} {col} {n_array[row][col].get()}"



    print("------Start of input------")
    print(total_stones)
    print(final_string)
    print("------End of input------\n\n")

for i in range(SIZE):
    add_15_rows()

Button(root, text="Print input", command=getVal, activebackground='#FFF0F5').grid(row=0, column=0)
mainloop()