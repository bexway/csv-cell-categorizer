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
    box.mainloop()

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

    def submit(self):
        self.quit()
        self.withdraw()

if __name__ == "__main__":
    main()
