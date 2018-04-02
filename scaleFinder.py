#create the list of notes to be referenced
noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def scaleFinder(scale, solfege):
    #Find the base index of the wanted scale
    scaleIndex = noteList.index(scale)
    
    #Determine the solfege offset
    if solfege == "Do":
        solfegeOffset = 0
    elif solfege == "Re":
        solfegeOffset = 2
    elif solfege == "Mi":
        solfegeOffset = 4
    elif solfege == "Fa":
        solfegeOffset = 5
    elif solfege == "So":
        solfegeOffset = 7
    elif solfege == "La":
        solfegeOffset = 9
    elif solfege == "Ti":
        solfegeOffset = 11
        
    #Compute target index and print note
    target = (scaleIndex + solfegeOffset) % 12
    
    print(noteList[target])

def printScale(scale):
    scaleFinder(scale, "Do")
    scaleFinder(scale, "Re")
    scaleFinder(scale, "Mi")
    scaleFinder(scale, "Fa")
    scaleFinder(scale, "So")
    scaleFinder(scale, "La")
    scaleFinder(scale, "Ti")

printScale("F")