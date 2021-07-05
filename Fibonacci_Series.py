from tkinter import*

root = Tk()
root.title("Fibonacci Series")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series: ")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        label_flower["text"] = "Flower is fooly bloomd"
        label_spiral["text"] = "Spirals in right directions are"+str(first_no)+" and Spirals in right directions are"+str(second_no)+". Total Spirals are" + str(sum)
btn=Button(root,text="Show Fibonacci Series",command=fibonacci)
        
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()      