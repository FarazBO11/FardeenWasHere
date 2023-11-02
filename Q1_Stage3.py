from tkinter import *


# Function to read data from the text file and store it in a nested list
def read_data_from_file():
    data = []
    with open("length_data.txt", "r") as file:
        next(file)  # Skip the first line
        for line in file:
            entry = line.strip().split()
            meters = float(entry[0])
            centimeters = meters * 100
            data.append([meters, centimeters])
    return data


# Function to display data in the GUI
def display_data():
    data = read_data_from_file()
    details = "Length Data from File:\n"
    for entry in data:
        details += f"{entry[0]} meters = {entry[1]} centimeters\n"
    details_label.config(text=details)


# Calculate centimeters
def calc_centimeters():
    meters = float(e1.get())
    centimeters = meters * 100
    e2.delete(0, END)
    e2.insert(0, centimeters)


# Calculate meters
def calc_meters():
    centimeters = float(e2.get())
    meters = centimeters / 100
    e1.delete(0, END)
    e1.insert(0, meters)


# Clear entries
def clear_entries():
    e1.delete(0, END)
    e2.delete(0, END)


# Main function
def main():
    global e1, e2, details_label

    root = Tk()
    root.title("Length Converter")
    root.geometry("300x250")
    root.configure(background="light gray")

    Label(root, text="Meters", bg="light gray").grid(row=0, column=0)
    e1 = Entry(root)
    e1.grid(row=0, column=1)

    Label(root, text="Centimeters", bg="light gray").grid(row=1, column=0)
    e2 = Entry(root)
    e2.grid(row=1, column=1)

    Button(root, text="Convert to Centimeters", command=calc_centimeters).grid(
        row=2, column=0
    )
    Button(root, text="Convert to Meters", command=calc_meters).grid(row=2, column=1)
    Button(root, text="Clear", command=clear_entries).grid(
        row=3, column=0, columnspan=2
    )
    Button(root, text="Show Data", command=display_data).grid(
        row=4, column=0, columnspan=2
    )
    Button(root, text="Exit", command=root.quit).grid(row=6, column=0, columnspan=2)

    details_label = Label(root, text="", bg="light gray")
    details_label.grid(row=5, column=0, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    main()
