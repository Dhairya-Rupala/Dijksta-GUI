from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import sys

global LABELS
global ENTRIES
global BUTTONS
global SOURCE
global DESTINATION
global NUMBER_NODES
global row_num
global count_next
global col_num
global count_press
global Short_Path
global count_res


#################################################################################################################
def clearNODE():
    NODE_ENTRY.delete(0, END)

def clearall():
    for i in ENTRIES:
        i.delete(0, END)

def clearsourcedest():
    for i in SOURCE:
        i.delete(0, END)
    for i in DESTINATION:
        i.delete(0, END)

def check_entries():
    for i in ENTRIES:
        string = i.get()
        num_node = NUMBER_NODES
        temp_list = string.split()
        if len(temp_list) != num_node:
            return -1
        for i in range(num_node):
            temp_string = temp_list[i]
            if temp_string.isalpha() or temp_string.isspace():
                return -1
    return 1

def clearAll():
    NODE_ENTRY.delete(END,0)
    global row_num
    global col_num
    global count_press
    global count_next
    global count_res
    global BUTTONS
    global LABELS
    global NUMBER_NODES
    global SOURCE
    global DESTINATION
    global Short_Path
    global ENTRIES
    clearNODE()
    for i in LABELS:
        i.destroy()
    for i in BUTTONS:
        i.destroy()

    for i in ENTRIES:
        i.destroy()
    for i in SOURCE:
        i.destroy()
    for i in DESTINATION:
        i.destroy()

    LABELS = []
    ENTRIES = []
    BUTTONS = []
    SOURCE = []
    DESTINATION = []
    NUMBER_NODES = 0
    count_next = 0
    count_press = 0
    col_num = 1
    Short_Path = []
    count_res = 0
    row_num = 8





def check_src_dest():
    num_node = 1
    for i in SOURCE:
        string = i.get()
        temp_list = string.split()
        if len(temp_list) != num_node or string.isspace():
            return -1
        d = temp_list[0]
        if not d.isdigit():
            return -1
        nUMBER = int(string)
        if nUMBER<0 or nUMBER>=NUMBER_NODES:
            return -1
    for i in DESTINATION:
        string = i.get()
        temp_list = string.split()
        if len(temp_list) != num_node:
            return -1
        d = temp_list[0]
        if not d.isdigit():
            return -1
        nUMBER =int(string)
        if nUMBER<0 or nUMBER>=NUMBER_NODES:
            return -1
    return 1





def check_nodes():
    global NUMBER_NODES

    string = NODE_ENTRY.get()
    temp_list = string.split()
    if len(temp_list) != 1:
        return -1
    string1 = temp_list[0]
    if not string1.isdigit():
        return -1
    if not (int(string1) <= 17) or not (int(string1) > 1):
        return -1

    NUMBER_NODES = int(string1)
    return 1

def close():
    root.destroy()

#################################################################################################################

def printPath(parent, ver):
    if parent[ver] == -1:
        return
    printPath(parent, parent[ver])
    txt = str(ver)
    t1 = "->"
    Short_Path.append(t1 + txt)


def printSolution(dist, parent, src, desti, Vertex):
    for i in range(Vertex):
        if i == desti:
            printPath(parent, i)
    txt = "".join(Short_Path)
    Lab = Label(root, text=str(src) + txt)
    Lab.grid(row=row_num, column=2)
    LABELS.append(Lab)

    DIST_LABEL = Label(root, font=myfont, text="Minimum Distance is", bg="light green", fg="black")
    DIST_LABEL.grid(row=row_num + 2, column=1)
    DIST_LABEL.config(height=1)
    LABELS.append(DIST_LABEL)

    distance = str(DISTANCE)
    MIN_DIST = Label(root, text=distance)
    MIN_DIST.grid(row=row_num + 2, column=2)
    MIN_DIST.config(height=1)
    LABELS.append(MIN_DIST)


def minDistance(dist, sptSet, Vertex):
    minimum = sys.maxsize
    min_index = 0

    for i in range(Vertex):
        if sptSet[i] == False and dist[i] <= minimum:
            minimum = dist[i]
            min_index = i
    return min_index



def DIJKSTRA(graph, source, desti, Vertex):
    # This data structures for storing the distance and parent information
    DIST = []
    Parent = []
    isIncluded = []
    Number = sys.maxsize

    for i in range(Vertex):
        DIST.append(Number)
        isIncluded.append(False)
        Parent.append(-1)

    DIST[source] = 0

    for temp in range(Vertex):

        min_ = minDistance(DIST, isIncluded, Vertex)
        isIncluded[min_] = True

        for i in range(Vertex):
            if isIncluded[i] == False and graph[min_][i] != 0 and (DIST[min_] + graph[min_][i] <= DIST[i]):
                DIST[i] = DIST[min_] + graph[min_][i]
                Parent[i] = min_
    global DISTANCE
    DISTANCE = DIST[desti]
    printSolution(DIST, Parent, source, desti, Vertex)

def MakeGraph():
    global count_res

    if count_res == 0:
        count_res = 1
        val = check_src_dest()

        if val == 1:
            GRAPH = []
            temp_list = []
            for i in ENTRIES:
                string = i.get()
                temparr = string.split()
                for d in range(len(temparr)):
                    temp_list.append(float(temparr[d]))
                GRAPH.append(temp_list)
                temp_list = []

            Source = 0
            DESTI = 0

            for i in SOURCE:
                Temp = i.get()
                string = Temp.split()
                Source = int(string[0])

            for i in DESTINATION:
                Temp = i.get()
                string = Temp.split()
                DESTI = int(string[0])

            Blextra = Label(root, font=myfont, text="The shortest path is", bg='light green', fg="black")
            Blextra.grid(row=row_num, column=1)
            Blextra.config(height=1)
            LABELS.append(Blextra)

            DIJKSTRA(GRAPH, Source, DESTI, NUMBER_NODES)
        else:
            messagebox._show(message='Invalid source or destination entries.Source and destination should be within the node range')
            clearsourcedest()
            count_res = 0

def AfterEntry():
    global count_press
    global row_num
    if count_press == 0:

        count_press = 1
        val = check_entries()

        if val == 1:
            BL2 = Label(root, bg="sky blue")
            BL2.grid(row=row_num, column=0)
            BL2.config(height=1)
            LABELS.append(BL2)

            SOURCE_LABEL = Label(root, font=myfont, text="    Enter the source node     ", bg="light green", fg="black")
            SOURCE_LABEL.grid(row=row_num + 1, column=0)
            SOURCE_LABEL.config(height=1)
            LABELS.append(SOURCE_LABEL)

            SOURCE_ENTRY = Entry(root)
            SOURCE_ENTRY.grid(row=row_num + 1, column=1)
            SOURCE.append(SOURCE_ENTRY)
            row_num += 2

            DEST_LABEL = Label(root, font=myfont, text="Enter the  destination node", bg="light green", fg="black")
            DEST_LABEL.grid(row=row_num, column=0)
            LABELS.append(DEST_LABEL)

            DEST_ENTRY = Entry(root)
            DEST_ENTRY.grid(row=row_num, column=1)
            DESTINATION.append(DEST_ENTRY)

            BL4 = Label(root, bg="sky blue")
            BL4.grid(row=row_num + 1, column=0)
            BL4.config(height=1)
            LABELS.append(BL4)
            row_num += 2

            BUTTON_FINAL = Button(root, text="Result", bg="yellow", fg="black", command=MakeGraph)
            BUTTON_FINAL.grid(row=row_num, column=0)
            BUTTONS.append(BUTTON_FINAL)

        else:
            messagebox._show(message="Enter the valid matrix,costs should be numbers it can not be alphabets.")
            count_press = 0
            clearall()


def Node_Entry():

    val = check_nodes()
    global count_next
    global row_num
    global col_num

    if count_next == 0:

        count_next = 1
        if val == 1:

            num_nodes = NUMBER_NODES
            for i in range(num_nodes):
                row_string = str(i)

                temp_entry = Entry(root)
                temp_label = Label(root, font=myfont, text="Enter " + row_string + "th row", bg="light green",
                                   fg="black")
                temp_label.grid(row=row_num, column=0)
                temp_label.config(height=1)
                ENTRIES.append(temp_entry)
                LABELS.append(temp_label)

                temp_entry.grid(row=row_num, column=col_num)
                row_num += 1

            Button_after_entry = Button(root, text="Press it", bg="yellow", fg="black", command=AfterEntry)
            Button_after_entry.grid(row=row_num - 1, column=2)
            Button_after_entry.config(height=1)
            BUTTONS.append(Button_after_entry)

        else:
            messagebox._show(message="The number of nodes should be grater than 1 and less than or equal to 17 also it can not be alphabets or float numbers")
            count_next = 0
            clearNODE()



if __name__ == "__main__":

    root = Tk()
    root.title("Dijkstra Algorithm By Dhairya")
    root.geometry("2000x2000")
    root.configure(bg="sky blue")

    LABELS = []
    ENTRIES = []
    BUTTONS = []
    SOURCE = []
    DESTINATION = []
    NUMBER_NODES = 0
    count_next = 0
    count_press = 0
    col_num = 0
    Short_Path =[]
    count_res = 0


    for i in range(3):
        temp_label = Label(root, bg="sky blue")
        temp_label.grid(row=0, column=i)
        temp_label.config(padx=30)
        myfont = font.Font(family="Halvetica")

    temp_label = Label(root, bg="sky blue")
    temp_label.grid(row=1, column=0)
    temp_label.config(padx=270)

    TITLE_LABEL = Label(root, text="DIJKSTRA ALGORITHM DEMO BY DHAIRYA", font=myfont, bg="sky blue", fg="black")
    TITLE_LABEL.grid(row=1, column=1)

    blank_label = Label(root, bg="sky blue")
    blank_label.grid(row=2, column=0)
    blank_label.config(height=1)

    Rule_label = Label(root, text="NOTE-You have to enter the graph in adjacency matrix form.                                                                                  ", bg="sky blue",
                       fg="black")
    Rule_label.grid(row=3,column=0)
    blank_label2 = Label(root,text="Every element should be space separated                                                                                                                   ",bg="sky blue",fg="black")
    blank_label2.grid(row=4, column=0)
    blank_label2.config(height=1)

    v = Label(root,bg="sky blue")
    v.grid(row=5,column=0)


    NODE_LABEL = Label(root, text="Enter the number of nodes", font=myfont, bg="light green", fg="black")
    NODE_LABEL.grid(row=6, column=0)
    NODE_LABEL.config(height=1)

    NODE_ENTRY = Entry(root)
    NODE_ENTRY.grid(row=6, column=1)

    NEXT_BUTTON = Button(root, text="Next", bg="yellow", fg="black", command=Node_Entry)
    NEXT_BUTTON.grid(row=6, column=2)

    Reset_Button = Button(root, text="Reset", bg="yellow", fg="black", command=clearAll)
    Reset_Button.grid(row=6, column=3)

    CLOSE_BUTTON=Button(root,text=" exit",bg="yellow",fg="black",command=close)
    CLOSE_BUTTON.grid(row=6,column=4)

    BLANK=Label(root,bg="sky blue")
    BLANK.grid(row=7,column=0)
    row_num =8
    col_num=1

    root.mainloop()
