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

    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()
