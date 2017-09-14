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
    outputHeaderFields = ["Fav Subject 1", "Fav Subject 2", "Fav Subject 3", "All Fav Subjects"]
    outputHeaders = inputHeaders + outputHeaderFields

    outputFile = open("output.csv", 'wb')
    outputWriter = csv.DictWriter(outputFile, outputHeaders)
    outputWriter.writeheader()

    for row in inputReader:
        #get the input and create a list to hold the output
        inputSubjects =  row["Favorite Subject(s)"]
        outputMatches = []
        #check each pattern for matches
        #TODO: append the consistent category, not the pattern
        for pattern in patternList:
            re = regex.compile(pattern)
            if re.search(inputSubjects):
                outputMatches.append(pattern)

        box = DialogBox(inputSubjects, outputMatches)

        print inputSubjects
        print outputMatches
        print box.output

        parsedOutputs = box.output

        outputWritingDict = {}
        for key in outputHeaders:
            if key in outputHeaderFields:
                if len(parsedOutputs) != 0:
                    outputWritingDict[key] = parsedOutputs.pop(0)
            else:
                outputWritingDict[key] = row[key]
        outputWriter.writerow(outputWritingDict)



    inputFile.close()
    outputFile.close()

class DialogBox(tk.Tk):
    def __init__(self, inputSubjects, outputMatches):
        """Open a dialog box for submitting majors"""
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="\nPlease ensure the boxes contain the correct subjects. See the input for what the student submitted. When you're done, press 'Submit'.\n", wraplength=600)
        self.label.pack()
        self.subjects = tk.Label(self, text="Input: "+str(inputSubjects)+"\n")
        self.subjects.pack()
        self.subjectEntries = []
        # Add an input box with default text for each subject that was matched. If less than 5 subjects match, add extra empty boxes to fill in.
        # subjectEntries tracks the entry boxes for later retrieval.
        for m in outputMatches:
            self.entry = tk.Entry(self, width=50)
            self.entry.insert(0, m)
            self.entry.pack()
            self.subjectEntries.append(self.entry)
        while len(self.subjectEntries) < 5:
            self.entry = tk.Entry(self, width=50)
            self.entry.pack()
            self.subjectEntries.append(self.entry)
        #TODO: see if I can have a button to pack in an additional input box? Can I add to tkinter boxes dynamically?
        

        self.button = tk.Button(self, text="Submit", command=self.submit)
        self.button.pack(side = tk.BOTTOM)
        self.output = None

        #Next, set up the dialog box and run it. It's size and position will be consistent even as it closes and opens
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
        self.output = [e.get() for e in self.subjectEntries];
        self.quit()
        self.withdraw()

if __name__ == "__main__":
    main()
