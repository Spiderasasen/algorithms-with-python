import tkinter as tk
from tkinter import simpledialog

# main window
def main():
    root = tk.Tk()
    root.title("Algorithm Visualization")
    root.geometry("400x300")

    #for exit button
    def on_exit():
        print('Exit button has been clicked')
        root.destroy()

    #title label
    root_label = tk.Label(root, text="Algorithm Visualization", font=("Arial", 20))
    root_label.pack(pady=20)
    print('title load')

    # exit button
    exit_button = tk.Button(root, text="Exit", command=on_exit, width=20)
    exit_button.pack(pady=15)


    root.mainloop()

#console log for buttons
def on_clicked(name: str):
    print(name, 'has been clicked')

    #checking what items will be accessed
    match name:
        case 'Insertion Sort':
            print('Insertion Sort algorithm has been executed')

if __name__ == '__main__':
    main()