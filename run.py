import regex, csv
import Tkinter as tk
import tkFileDialog

def main():
    # I'll use regexes to match the favorite subject to the pattern
    # TODO: add file reading for patterns, and add a corresponding title (what should be written to the output) to the list
    patternList = ["[tT]est ?1", "[Pp]atterns?", "[Mm]ath"]

    inputFile = open("database.csv", 'rb')
    inputReader = csv.DictReader(inputFile)

    inputHeaders = inputReader.fieldnames[:]
    outputHeaders = inputHeaders + ["Fav Subject 1", "Fav Subject 2", "Fav Subject 3"]

    outputFile = open("output.csv", 'wb')
    outputWriter = csv.DictWriter(outputFile, outputHeaders)
    outputWriter.writeheader()
    
    for row in inputReader:
        inputSubjects =  row["Favorite Subject(s)"]
        outputSubjects = []
        for pattern in patternList:
            re = regex.compile(pattern)
            if re.search(inputSubjects):
                outputSubjects.append(pattern)

        print inputSubjects
        print outputSubjects

    box = DialogBox()

    inputFile.close()
    outputFile.close()

class DialogBox(tk.Tk):
    def __init__(self):
        """Open a dialog box for submitting majors"""
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="Test", wraplength=600)
        self.label.pack()

        self.button = tk.Button(self, text="Submit", command=self.submit)
        self.button.pack(side = tk.BOTTOM)

        #Next, set up the dialog box and run it
        #box sizing: https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
        
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        # width and height of tK window; scaled based on screen size
        w = ws/1.5
        h = hs/1.5

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.mainloop()

    def submit(self):
        self.quit()
        self.withdraw()

if __name__ == "__main__":
    main()
