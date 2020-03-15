# -*- coding: utf-8 -*-
"""
    Formatter - Demo

    Format column based document on user choice

    Usage:
    Run script to see how it works

    Note: By commenting or deleting everything, including,
    the <comment_or_delete> tags it is ready to be used

"""
from Npp import editor, notepad, console, MESSAGEBOXFLAGS

setlayer = False

layerNumber=0
cancella=False

def delContents(contents, lineNumber, totalLines):
    global layerNumber
    global cancella
            
    if ((contents.startswith('G0 Z')==True) or (contents.startswith('G1 Z')==True)):
        # trovato un layer
        setlayer = True
        #editor.replaceLine(lineNumber, contents.strip() + ' ; Layer {}'.format(layerNumber))
        if ((layerNumber == 29) and (layerNumber > 0)):
            cancella=True
            #editor.deleteLine(lineNumber)
            editor.replaceLine(lineNumber, contents.strip() + ' ###')
            layerNumber = layerNumber + 1
            #return 0
        else:
            cancella=False
            layerNumber = layerNumber + 1
    else:
        if (cancella==True):
            #editor.deleteLine(lineNumber)
            editor.replaceLine(lineNumber, contents + ' ###')
            #return 0
  
               
def testContents(contents, lineNumber, totalLines):
    global layerNumber
            
    if ((contents.startswith('G0 Z')==True) or (contents.startswith('G1 Z')==True)):
        # trovato un layer
            setlayer = True
            editor.replaceLine(lineNumber, contents.strip() + ' ; Layer {}'.format(layerNumber))
            layerNumber = layerNumber + 1
    else:
            editor.setLineIndentation(lineNumber, 4)
           
editor.forEachLine(testContents)  
