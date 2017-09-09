import regex, csv
import Tkinter as tk
import tkFileDialog

def main():
    patterns = ["[tT]est ?1", "[Pp]atterns?", "([Tt]hree)|3"]

    databaseFile = open("database.csv", 'rb')
    databaseReader = csv.DictReader(databaseFile)

    for row in databaseReader:
        #placeholder to make sure it's reading right
        print row

if __name__ == "__main__":
    main()
