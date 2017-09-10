import regex, csv
import Tkinter as tk
import tkFileDialog

def main():
    # I'll use regexes to match the favorite subject to the
    patterns = ["[tT]est ?1", "[Pp]atterns?", "([Tt]hree)|3"]

    inputFile = open("database.csv", 'rb')
    inputReader = csv.DictReader(inputFile)

    inputHeaders = inputReader.fieldnames[:]
    outputHeaders = inputHeaders + ["Fav Subject 1", "Fav Subject 2", "Fav Subject 3"]

    outputFile = open("output.csv", 'wb')
    outputWriter = csv.DictWriter(outputFile, outputHeaders)
    outputWriter.writeheader()
    
    for row in inputReader:
        #placeholder to make sure it's reading right
        print row

    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()
