from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from heapsort import heap_sort
from insertionsort import insertion_sort
from selectionsort import selection_sort

root = Tk()
root.title('Sorting Visualizer')
root.geometry('900x600+200+80')
root.config(bg='#082A46')

isSorting = False
selected_algorithm = StringVar()
data = []

#code to generate the array
def Generate():
    global data
    print('Selected Algorithm: ' + selected_algorithm.get())
    min_value = int(minvalue.get())
    max_value = int(maxvalue.get())
    size_value = int(sizevalue.get())
   
    data = []
    for i in range(size_value):
        data.append(random.randrange(min_value, max_value + 1))
        drawData(data, ['#A90042' for x in range(len(data))])

#drawing array elements as rectangle bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400

        x1 = (i + 1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=("new roman", 15, "italic bold"), fill="orange")

        root.update_idletasks()

#code to start sorting
def StartAlgorithm():
    global isSorting
    isSorting = True
    if not isSorting:
        return

    global data
    if not data:
        return

    if algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedscale.get())

    elif algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawData, speedscale.get())

    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, drawData, speedscale.get())

    elif algo_menu.get() == "Heap Sort":
        heap_sort(data, drawData, speedscale.get())

    elif algo_menu.get() == "Insertion Sort":
        insertion_sort(data, drawData, speedscale.get())

    elif algo_menu.get() == "Selection Sort":
        selection_sort(data, drawData, speedscale.get())

    drawData(data, ['gray' for x in range(len(data))])

def StopAlgorithm():
    global isSorting
    isSorting = False
    

#GUI PART
mainlabel = Label(root, text="Select Algorithm :", font=("new roman", 13, "bold"), bg="black",
                  height=1, width=15, fg="white")
mainlabel.place(x=5, y=20)

algo_menu = ttk.Combobox(root, width=15, font=("new roman", 17, "bold"), textvariable=selected_algorithm,
                         values=['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Insertion Sort', 'Selection Sort'])
algo_menu.place(x=170, y=20)
algo_menu.current(0)

random_generate = Button(root, text="Generate", bg="yellow", fg="black", font=("arial", 12, "italic bold"), relief=GROOVE,
                         activebackground="orange", activeforeground="white", bd=5, width=10, command=Generate)
random_generate.place(x=750, y=80)

sizevaluelabel = Label(root, text="Array size :", font=("new roman", 12, "bold"), bg="black",
                       height=2, width=10, fg="white", bd=5, relief=SUNKEN)
sizevaluelabel.place(x=4,y=80)

sizevalue = Scale(root, from_ = 0 , to = 30, resolution = 1,orient = HORIZONTAL, font = ("arial",14,"italic bold"),
                      relief = GROOVE, bd = 2, width = 10)
sizevalue.place(x=120,y=80)


minvaluelabel = Label(root, text="Min Value :", font=("new roman",12,"bold"),bg="black",
                 height=2, width=10,fg="white", bd=5, relief= SUNKEN)
minvaluelabel.place(x=250,y=80)

minvalue = Scale(root, from_ = 0 , to = 10, resolution = 1,orient = HORIZONTAL, font = ("arial",14,"italic bold"),
                      relief = GROOVE, bd = 2, width = 10)
minvalue.place(x=370,y=80)


maxvaluelabel = Label(root, text="Max Value :", font=("new roman",12,"bold"),bg="black",
                 height=2, width=10,fg="white", bd=5, relief= SUNKEN)
maxvaluelabel.place(x=500,y=80)

maxvalue = Scale(root, from_ = 0 , to = 100, resolution = 1,orient = HORIZONTAL, font = ("arial",14,"italic bold"),
                      relief = GROOVE, bd = 2, width = 10)
maxvalue.place(x=620,y=80)

start = Button(root,text="Start", bg="green", fg="white",font = ("arial",12,"italic bold"),relief = GROOVE,
                         activebackground="#C45B09", activeforeground="black",bd=5,width=10,command=StartAlgorithm)
start.place(x=750,y=20)

speedlabel = Label(root, text = "Speed :", font = ("new roman",12,"bold"), bg = "black",
                   height=2,width=10, fg="white",relief=SUNKEN,bd=5)
speedlabel.place(x=400,y=20)

speedscale = Scale(root, from_ = 0.1 , to = 5.0, resolution = 0.2,length=200,digits=2,orient = HORIZONTAL, font = ("arial",14,"italic bold"),
                      relief = GROOVE, bd = 2, width = 10)
speedscale.place(x=520,y=20)

canvas = Canvas(root, width=870, height=450, bg="black")
canvas.place(x=10,y=140)

#stop_button = Button(root, text="Stop", bg="red", fg="white", font=("arial", 12, "italic bold"), relief=GROOVE,
#                    activebackground="orange", activeforeground="white", bd=5, width=10, command=StopAlgorithm)
#stop_button.place(x=750, y=50)

root.mainloop()