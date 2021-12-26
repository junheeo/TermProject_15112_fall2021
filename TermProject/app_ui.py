# name : Jun Hee Oh
# ID : junheeo

from cmu_112_graphics import *
import string
from aes_encrypt import aesEncryption
from aes_encrypt import aesDecryption
from rsa_encrypt import rsaCreateKeys
from rsa_encrypt import rsaEncrypt
from rsa_encrypt import rsaDecrypt
import socket
import pickle

#global encodedTextList
#encodedTextList = [('Colsolas', 'a'),('Colsolas', 'b'),('Colsolas', 'c'),('Colsolas', 'd'),('Colsolas', 'e'),('Colsolas', 'f'),('Colsolas', 'g'),('Colsolas', 'h'),('Colsolas', 'i'),('Colsolas', 'j'),('Colsolas', 'k'),('Colsolas', 'l'),('Colsolas', 'm'),('Colsolas', 'n'),('Colsolas', 'o'),('Colsolas', 'p'),('Colsolas', 'q'),('Colsolas', 'r'),('Colsolas', 's'),('Colsolas', 't'),('Colsolas', 'u'),('Colsolas', 'v'),('Colsolas', 'w'),('Colsolas', 'x'),('Colsolas', 'y'),('Colsolas', 'z'),('Colsolas', 'A'),('Colsolas', 'B'),('Colsolas', 'C'),('Colsolas', 'D'),('Colsolas', 'E'),('Colsolas', 'F'),('Colsolas', 'G'),('Colsolas', 'H'),('Colsolas', 'I'),('Colsolas', 'J'),('Colsolas', 'K'),('Colsolas', 'L'),('Colsolas', 'M'),('Colsolas', 'N'),('Colsolas', 'O'),('Colsolas', 'P'),('Colsolas', 'Q'),('Colsolas', 'R'),('Colsolas', 'S'),('Colsolas', 'T'),('Colsolas', 'U'),('Colsolas', 'V'),('Colsolas', 'W'),('Colsolas', 'X'),('Colsolas', 'Y'),('Colsolas', 'Z'),('Colsolas', '1'),('Colsolas', '2'),('Colsolas', '3'),('Colsolas', '4'),('Colsolas', '5'),('Colsolas', ' ')]
#global insertIndex
#insertIndex = -1

def appStarted(app):
    app.textsize = 30
    #app.textUnitProportion = round(app.textsize / 2.2,4)
    #app.wordWidth = round(app.textUnitProportion * 1.12, 3)
    #app.wordHeight = round(app.textUnitProportion * 2.4, 3)
    app.wordHeight = 18
    app.text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345!@#$%^'
    app.textEncodeL = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','!','@','#','$','%','^',"'",'-','_','+','=','END']
    app.consolasCharSizeDict={'0': (0, 0, 11, 16), '1': (0, 0, 11, 16), '2': (0, 0, 11, 16), '3': (0, 0, 11, 16), '4': (0, 0, 11, 16), '5': (0, 0, 11, 16), '6': (0, 0, 11, 16), '7': (0, 0, 11, 16), '8': (0, 0, 11, 16), '9': (0, 0, 11, 16), 'a': (0, 0, 10, 16), 'b': (0, 0, 10, 16), 'c': (0, 0, 10, 16), 'd': (0, 0, 10, 16), 'e': (0, 0, 10, 16), 'f': (0, 0, 7, 16), 'g': (0, 0, 10, 16), 'h': (0, 0, 10, 16), 'i': (0, 0, 6, 16), 'j': (0, 0, 6, 16), 'k': (0, 0, 9, 16), 'l': (0, 0, 6, 16), 'm': (0, 0, 14, 16), 'n': (0, 0, 10, 16), 'o': (0, 0, 10, 16), 'p': (0, 0, 10, 16), 'q': (0, 0, 10, 16), 'r': (0, 0, 7, 16), 's': (0, 0, 9, 16), 't': (0, 0, 7, 16), 'u': (0, 0, 10, 16), 'v': (0, 0, 9, 16), 'w': (0, 0, 12, 16), 'x': (0, 0, 9, 16), 'y': (0, 0, 9, 16), 'z': (0, 0, 9, 16), 'A': (0, 0, 11, 16), 'B': (0, 0, 11, 16), 'C': (0, 0, 12, 16), 'D': (0, 0, 12, 16), 'E': (0, 0, 10, 16), 'F': (0, 0, 10, 16), 'G': (0, 0, 12, 16), 'H': (0, 0, 12, 16), 'I': (0, 0, 6, 16), 'J': (0, 0, 9, 16), 'K': (0, 0, 11, 16), 'L': (0, 0, 10, 16), 'M': (0, 0, 14, 16), 'N': (0, 0, 12, 16), 'O': (0, 0, 12, 16), 'P': (0, 0, 11, 16), 'Q': (0, 0, 12, 16), 'R': (0, 0, 11, 16), 'S': (0, 0, 11, 16), 'T': (0, 0, 11, 16), 'U': (0, 0, 12, 16), 'V': (0, 0, 11, 16), 'W': (0, 0, 15, 16), 'X': (0, 0, 11, 16), 'Y': (0, 0, 11, 16), 'Z': (0, 0, 11, 16), '!': (0, 0, 6, 16), '"': (0, 0, 9, 16), '#': (0, 0, 11, 16), '$': (0, 0, 11, 16), '%': (0, 0, 14, 16), '&': (0, 0, 12, 16), "'": (0, 0, 6, 16), '(': (0, 0, 7, 16), ')': (0, 0, 7, 16), '*': (0, 0, 9, 16), '+': (0, 0, 11, 16), ',': (0, 0, 6, 16), '-': (0, 0, 9, 16), '.': (0, 0, 6, 16), '/': (0, 0, 6, 16), ':': (0, 0, 6, 16), ';': (0, 0, 6, 16), '<': (0, 0, 11, 16), '=': (0, 0, 11, 16), '>': (0, 0, 11, 16), '?': (0, 0, 9, 16), '@': (0, 0, 14, 16), '[': (0, 0, 7, 16), '\\': (0, 0, 6, 16), ']': (0, 0, 7, 16), '^': (0, 0, 11, 16), '_': (0, 0, 10, 16), '`': (0, 0, 9, 16), '{': (0, 0, 7, 16), '|': (0, 0, 6, 16), '}': (0, 0, 7, 16), '~': (0, 0, 11, 16), ' ': (0, 0, 6, 16), '\t': (0, 0, 74, 16), '\n': (0, 0, 2, 16), '\r': (0, 0, 2, 16), '\x0b': (0, 0, 2, 16), '\x0c': (0, 0, 2, 16), 'END': (0, 0, 15, 16)}
    app.charDimOnTextEditorApp = list()
    app.currFontName = 'Consolas'
    app.fixedTextWidth = 15
    app.lengthBetweenLines = 5
    app.editPositionX = -30
    app.editPositionY = -30
    app.editCharInx = len(app.textEncodeL) - 1
    app.editCharDim = (-30, -30, -30, -30)
    app.endEditCharDim = (-30, -30, -30, -30)
    app.pressKey = ''
    app.isHighlightMode = False
    app.highlightCharInx = app.editCharInx
    app.highlightInxList = list()
    app.highlightChangeDir = None
    app.previouslyStoppedBeforeEnter = False
    app.highlightInxCopiedCharsList = list()
    app.currentlyCopied = False
    app.saveButtonDim = (-1,-1,50,30)
    app.saveOperationUndergo = False
    app.saveFileName = ''
    app.openButtonDim = (50,-1,100,30)
    app.openOperationUndergo = False
    app.filesUnderTermProject = []
    app.filesUnderTermProjectDim = []
    app.openingFile = ''
    app.encryptButtonDim = (100,-1,200,30)
    app.encryptOperationUndergo = False
    app.encryptionKey = ''
    app.decryptButtonDim = (200,-1,300,30)
    app.decryptOperationUndergo = False
    app.decryptionKey = app.encryptionKey
    app.rsaCreateKeyButtonDim = (300,-1,400,30)
    app.rsaKeyCreateUndergo = False
    app.e, app.d, app.n = 0, 0, 0
    readKeysFromFile(app)
    app.rsaEncryptButtonDim = (400,-1,500,30)
    app.rsaEncryptUndergo = False
    app.rsaEncryptedL = list()
    app.rsaDecryptButtonDim = (500,-1,600,30)
    app.rsaDecryptUndergo = False
    app.sendPublicKeyButtonDim = (600,-1,750,30)
    app.sendUndergo = False
    app.recievePublicKeyButtonDim = (750,-1,900,30)
    app.recieveUndergo = False
    app.enteredHostName = False
    app.hostName = socket.gethostname()
    app.enteredPortNumber = False
    app.portNumber = 1236
    app.HEADERSIZE = 10
    app.socketFeedback = ''
    

def mousePressed(app, event):
    if app.saveOperationUndergo == True:
        pass
    elif app.openOperationUndergo == True:
        for fileInx in range(0, len(app.filesUnderTermProjectDim)):
            x0File, y0File, x1File, y1File = app.filesUnderTermProjectDim[fileInx]
            if x0File <= event.x <= x1File and y0File <= event.y <= y1File:
                print(f'len(app.filesUnderTermProject) = {len(app.filesUnderTermProject)}')
                print(f'fileInx = {fileInx}')
                app.openingFile = app.filesUnderTermProject[fileInx]
                app.text = readFile(app.openingFile)
                updateAppDotTextEncodeL(app)
                app.openOperationUndergo = False
                app.saveFileName = app.openingFile
        pass
    elif app.encryptOperationUndergo == True:
        pass
    else:
        x0SaveButton, y0SaveButton, x1SaveButton, y1SaveButton = app.saveButtonDim
        if x0SaveButton < event.x < x1SaveButton and y0SaveButton < event.y < y1SaveButton:
            app.saveOperationUndergo = True
        x0OpenButton, y0OpenButton, x1OpenButton, y1OpenButton = app.openButtonDim
        if x0OpenButton < event.x < x1OpenButton and y0OpenButton < event.y < y1OpenButton:
            app.openOperationUndergo = True
            app.filesUnderTermProject = []
            app.filesUnderTermProjectDim = []
            for fileOrFolder in os.listdir():
                if os.path.isfile(fileOrFolder):
                    app.filesUnderTermProject.append(fileOrFolder)
            x0File, y0File, x1File, y1File = 3, 3, 3 + 14, 3 + 18
            for fileCount in range(len(app.filesUnderTermProject)):
                app.filesUnderTermProjectDim.append((x0File, y0File, x1File, y1File))
                y0File += 30
                y1File = y0File + 18
        x0EncryptButton, y0EncryptButton, x1EncryptButton, y1EncryptButton = app.encryptButtonDim
        if x0EncryptButton <= event.x <= x1EncryptButton and y0EncryptButton <= event.y <= y1EncryptButton:
            app.encryptOperationUndergo = True
        x0DecryptButton, y0DecryptButton, x1DecryptButton, y1DecryptButton = app.decryptButtonDim
        if x0DecryptButton <= event.x <= x1DecryptButton and y0DecryptButton <= event.y <= y1DecryptButton:
            app.decryptOperationUndergo = True
        x0RSAKeyB, y0RSAKeyB, x1RSAKeyB, y1RSAKeyB = app.rsaCreateKeyButtonDim
        if x0RSAKeyB <= event.x <= x1RSAKeyB and y0RSAKeyB <= event.y <= y1RSAKeyB:
            app.rsaKeyCreateUndergo = True
            print(f'*')
            app.e, app.d, app.n = rsaCreateKeys()
            keysString = f'Public Key {app.e}\nPrivate Key {app.d}\nn {app.n}'
            writeFile('rsaKeys.txt', keysString)
            app.newrsaKeyMade = True
        x0RSAEncB, y0RSAEncB, x1RSAEncB, y1RSAEncB = app.rsaEncryptButtonDim
        if x0RSAEncB <= event.x <= x1RSAEncB and y0RSAEncB <= event.y <= y1RSAEncB:
            app.rsaEncryptUndergo = True
        x0RSADecB, y0RSADecB, x1RSADecB, y1RSADecB = app.rsaDecryptButtonDim
        if x0RSADecB <= event.x <= x1RSADecB and y0RSADecB <= event.y <= y1RSADecB:
            app.rsaDecryptUndergo = True
        x0Send, y0Send, x1Send, y1Send = app.sendPublicKeyButtonDim
        if x0Send <= event.x <= x1Send and y0Send <= event.y <= y1Send:
            app.sendUndergo = True
        x0Recieve, y0Recieve, x1Recieve, y1Recieve = app.recievePublicKeyButtonDim
        if x0Recieve <= event.x <= x1Recieve and y0Recieve <= event.y <= y1Recieve:
            app.recieveUndergo = True
        app.isHighlightMode = False
        if app.currentlyCopied == False:
            app.highlightChangeDir = None
        app.highlightInxList = []
        app.highlightCharInx = app.editCharInx
        for charInx in range(len(app.textEncodeL)):
            charDim = app.charDimOnTextEditorApp[charInx]
            x0, y0, x1, y1 = charDim
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                app.editCharInx = charInx
                app.editCharDim = charDim
                break

# copy paste : highlight -> press 'c' -> click location to paste -> press 'v'
# discard what was copied : press 'x'
#              highlight -> press 'c' -> click location to paste -> press 'x'

def keyPressed(app, event):
    app.timerDelay = 50
    if app.saveOperationUndergo == True:
        if event.key == 'Enter':
            writeFile(app.saveFileName, app.text)
            app.saveOperationUndergo = False
        elif event.key == 'Delete':
            app.saveFileName = app.saveFileName[:-1]
        else:
            for char in string.printable:
                if char == event.key and char != '/':
                    app.saveFileName += char
    elif app.openOperationUndergo == True:
        if event.key == 'x':
            app.openOperationUndergo = False
    elif app.encryptOperationUndergo == True or app.decryptOperationUndergo == True:
        if event.key == 'Enter':
            if app.encryptOperationUndergo == True:
                encryptText(app)
                app.encryptOperationUndergo = False
            elif app.decryptOperationUndergo == True:
                decryptText(app)
                app.decryptOperationUndergo = False
            updateAppDotTextEncodeL(app)
            app.editCharInx = len(app.textEncodeL) - 1

        if event.key == 'x':
            app.encryptOperationUndergo = False
        elif event.key == 'Delete':
            app.encryptionKey = app.encryptionKey[:-1]
        else:
            for char in string.printable:
                if char == event.key:
                    app.encryptionKey += char
    elif app.rsaKeyCreateUndergo == True:
        if event.key == 'x':
            app.rsaKeyCreateUndergo = False
            app.newrsaKeyMade = False
    #app.rsaEncryptUndergo = False
    elif app.rsaEncryptUndergo == True or app.rsaDecryptUndergo == True:
        if event.key == 'Enter':
            if app.rsaEncryptUndergo == True:
                rsaEncryptText(app)
                app.rsaEncryptUndergo = False
            elif app.rsaDecryptUndergo == True:
                rsaDecryptText(app)
                app.rsaDecryptUndergo = False
            updateAppDotTextEncodeL(app)
            app.editCharInx = len(app.textEncodeL) - 1

        if event.key == 'x':
            app.rsaEncryptUndergo = False
            app.rsaDecryptUndergo = False
        elif event.key == 'Delete':
            #app.e, app.d, app.n
            if app.rsaEncryptUndergo:
                app.e = app.e//10
            if app.rsaDecryptUndergo:
                app.d = app.d//10
        else:
            for char in string.digits:
                if char == event.key:
                    if app.rsaEncryptUndergo:
                        app.e = int(str(app.e) + char)
                    elif app.rsadecryptUndergo:
                        app.d = int(str(app.d) + char)
    elif app.sendUndergo == True or app.recieveUndergo == True:
        if app.enteredHostName == True:
            if event.key == 'Enter':
                if app.enteredPortNumber == True:
                    if event.key == 'Enter':
                        app.sendUndergo = False
                        app.recieveUndergo = False
                        app.enteredHostName = False
                        app.enteredPortNumber = False
                        app.socketFeedback = ''
                app.enteredPortNumber = True
                if app.sendUndergo == True:
                    send(app)
                elif app.recieveUndergo == True:
                    recieve(app)
            elif event.key == 'Delete':
                app.portNumber = app.portNumber//10
            else:
                for char in string.digits:
                    if char == event.key:
                        app.portNumber = app.portNumber * 10 + int(char)
        
        if app.enteredHostName == False:
            if event.key == 'Enter':
                app.enteredHostName = True
            elif event.key == 'Delete':
                app.hostName = app.hostName[:-1]
            else:
                for char in string.printable:
                    if char == event.key:
                        app.hostName += char
    else:
        app.pressKey = ''
        print(f'event.key = {event.key}')
        print(f'app.highlightInxList = {app.highlightInxList}')
        if app.highlightInxList != [] and event.key == 'c' and app.highlightInxCopiedCharsList == []:
            app.currentlyCopied = True
            if app.highlightChangeDir == 'Left' or app.highlightChangeDir == 'Up':
                for inx in range(len(app.highlightInxList) - 1, -1, -1):
                    highlightedInx = app.highlightInxList[inx]
                    app.highlightInxCopiedCharsList.append(app.textEncodeL[highlightedInx])
            elif app.highlightChangeDir == 'Right' or app.highlightChangeDir == 'Down':
                for inx in range(0, len(app.highlightInxList)):
                    highlightedInx = app.highlightInxList[inx]
                    app.highlightInxCopiedCharsList.append(app.textEncodeL[highlightedInx])
        if app.currentlyCopied == False:
            print('**')
            if event.key == 'Left':
                if app.isHighlightMode == False:
                    app.highlightCharInx = app.editCharInx
                    app.isHighlightMode = True
                if app.highlightCharInx - 1 > 0:
                    app.highlightCharInx -= 1
                    print(f'app.highlightChangeDir == "Left" or app.highlightChangeDir == None = {app.highlightChangeDir == "Left" or app.highlightChangeDir == None}')
                    if app.highlightChangeDir == 'Left' or app.highlightChangeDir == None:
                        app.highlightInxList.append(app.highlightCharInx)
                        app.highlightChangeDir = 'Left'
                    else:
                        pass

            elif event.key == 'Right':
                if app.isHighlightMode == False:
                    app.highlightCharInx = app.editCharInx - 1
                    app.isHighlightMode = True
                if app.highlightCharInx + 1 < len(app.textEncodeL):
                    app.highlightCharInx += 1
                    print(f'app.highlightChangeDir == "Right" = {app.highlightChangeDir == "Right"}')
                    print(f'app.highlightChangeDir == "Right" or app.highlightChangeDir == None = {app.highlightChangeDir == "Right" or app.highlightChangeDir == None}')
                    if app.highlightChangeDir == 'Right' or app.highlightChangeDir == None:
                        app.highlightInxList.append(app.highlightCharInx)
                        app.highlightChangeDir = 'Right'
                    else:
                        pass

            elif event.key == 'Down':
                if app.isHighlightMode == False:
                    app.highlightCharInx = app.editCharInx
                    app.isHighlightMode = True
                print(f'app.highlightCharInx = {app.highlightCharInx}')
                if app.highlightChangeDir != None and app.highlightChangeDir != 'Down':
                    pass
                else:
                    app.highlightChangeDir = 'Down'
                    xStandard0, yStandard0, xStandard1, yStandard1 = app.consolasCharSizeDict['0']
                    x0, y0, x1, y1 = app.charDimOnTextEditorApp[app.highlightCharInx]
                    y0 = y1 + app.lengthBetweenLines
                    y1 = y0 + yStandard1
                    searchDimension = (x0, y0, x1, y1)
                    searchDimensionFound = False
                    for dimensionInx in range(len(app.charDimOnTextEditorApp)):
                        dimension = app.charDimOnTextEditorApp[dimensionInx]
                        if dimension == searchDimension:
                            if dimensionInx > app.highlightCharInx:
                                searchDimensionFound = True
                                for highlightInx in range(app.highlightCharInx, dimensionInx):
                                    if app.textEncodeL[highlightInx] != 'END':
                                        app.highlightInxList.append(highlightInx)
                                app.highlightCharInx = dimensionInx
                            else:
                                break
                    if searchDimensionFound == False:
                        for highlightInx in range(app.highlightCharInx, len(app.charDimOnTextEditorApp)):
                            if (len(app.charDimOnTextEditorApp) - 2) not in app.highlightInxList:
                                if app.textEncodeL[highlightInx] != 'END':
                                    app.highlightInxList.append(highlightInx)
                    print(f'app.highlightInxList = {app.highlightInxList}')
            elif event.key == 'Up':
                if app.isHighlightMode == False:
                    app.highlightCharInx = app.editCharInx - 1
                    app.isHighlightMode = True
                if app.highlightChangeDir != None and app.highlightChangeDir != 'Up':
                    pass
                else:
                    app.highlightChangeDir = 'Up'
                    xStandard0, yStandard0, xStandard1, yStandard1 = app.consolasCharSizeDict['0']
                    x0, y0, x1, y1 = app.charDimOnTextEditorApp[app.highlightCharInx]
                    y0 = y0 - app.lengthBetweenLines - yStandard1
                    y1 = y0 + yStandard1
                    searchDimension = (x0, y0, x1, y1)
                    searchInx = app.highlightCharInx
                    foundSearchDim = False
                    while searchInx >= 0:
                        if searchDimension != app.charDimOnTextEditorApp[searchInx]:
                            searchInx -= 1
                        else:
                            foundSearchDim = True
                            for highlightInx in range(app.highlightCharInx, searchInx, -1):
                                app.highlightInxList.append(highlightInx)
                                app.highlightCharInx = searchInx
                            break
                    print(f'foundSearchDim == False = {foundSearchDim == False}')
                    if foundSearchDim == False:
                        searchInx = app.highlightCharInx
                        while searchInx >= 0:
                            if app.textEncodeL[searchInx] != '\n' or app.previouslyStoppedBeforeEnter == True:
                                searchInx -= 1
                            else:
                                foundSearchDim = True

                                for highlightInx in range(app.highlightCharInx, searchInx, -1):
                                    app.highlightInxList.append(highlightInx)
                                    app.highlightCharInx = searchInx - 1
                                break
                            print(f'searchInx = {searchInx}')
                        if foundSearchDim == False:
                            if 0 not in app.highlightInxList:
                                for highlightInx in range(app.highlightCharInx, -1, -1):
                                    app.highlightInxList.append(highlightInx)

            
            if event.key == 'Delete' and app.textEncodeL[app.editCharInx - 1] != 'END':
                app.textEncodeL.pop(app.editCharInx - 1)
                app.editCharInx -= 1
            if event.key == 'tab':
                for spaces in range(4):
                    app.textEncodeL.insert(app.editCharInx, app.pressKey)
                    app.editCharInx += 1
            else:
                for char in string.printable:
                    if event.key == char:
                        app.pressKey = char
                    elif event.key == 'Enter':
                        app.pressKey = '\n'
                    elif event.key == 'Space':
                        app.pressKey = ' '
                    elif event.key == 'Tab':
                        app.pressKey = '\t'
            if app.pressKey != '':
                app.textEncodeL.insert(app.editCharInx, app.pressKey)
                app.editCharInx += 1
            
            updateAppDotText(app)
            

        if app.currentlyCopied == True:
            print('*')
            if event.key == 'v':
                app.textEncodeL = app.textEncodeL[: app.editCharInx] + app.highlightInxCopiedCharsList + app.textEncodeL[app.editCharInx:]
                print(f'app.textEncodeL = {app.textEncodeL}')
                app.highlightInxList = []
                app.highlightInxCopiedCharsList = []
                app.currentlyCopied = False
                pass
            elif event.key == 'x':
                app.highlightInxList = []
                app.highlightInxCopiedCharsList = []
                app.currentlyCopied = False

def timerFired(app):
    #print('*')
    readKeysFromFile(app)
    print(f'app.saveOperationUndergo = {app.saveOperationUndergo}')
    print(f'app.openOperationUndergo = {app.openOperationUndergo}')
    charDimOnTextEditor = list()
    lineNumber = 0
    prevY0 = 0
    prevY1 = 30
    lineChange = True
    prevX1 = 3
    charInx = 0
    maxLineLength = app.width - 8
    if app.textEncodeL[0] == '\ufeff':
        app.textEncodeL = app.textEncodeL[1:]
        updateAppDotText(app)
        app.editCharInx = len(app.textEncodeL) - 1
    while charInx < len(app.textEncodeL):
        charStr = app.textEncodeL[charInx]
        if charStr == '\n':

            charInx += 1

            prevX1 = 3
            prevY0 = prevY1 + app.lengthBetweenLines
            x0Standard, y0Standard, x1Standard, y1Standard = app.consolasCharSizeDict['0']
            prevY1 = prevY0 + y1Standard
            x0, y0, x1, y1 = app.consolasCharSizeDict[charStr]
            x0 = prevX1-3
            x1 = 3
            #x0 = prevX1
            #x1 = prevX1 + app.fixedTextWidth
            y0 = prevY0
            y1 = prevY1
            charDimOnTextEditor.append((x0, y0, x1, y1))
            
            continue
        #print(f'char for dimension : {charStr}')
        charDim = app.consolasCharSizeDict[charStr]
        x0, y0, x1, y1 = charDim
        if x1 < app.fixedTextWidth:
            x1 = app.fixedTextWidth
        if lineChange == True:
            x0 = x0 + 3
            x1 = x1 + 3
            prevX1 = x1
            y0 = prevY1 + app.lengthBetweenLines
            y1 = y1 + prevY1 + app.lengthBetweenLines
            prevY0 = y0
            prevY1 = y1
            lineChange = False
        else:
            x0 = prevX1
            x1 = prevX1 + x1
            prevX1 = x1
            y0 = prevY0
            y1 = prevY1
            if x1 > maxLineLength:
                #print('***')
                lineChange = True
                continue
        charDimOnTextEditor.append((x0, y0, x1, y1))
        app.charDimOnTextEditorApp = charDimOnTextEditor
        charInx += 1
    app.endEditCharDim = app.charDimOnTextEditorApp[-1]
    app.editCharDim = app.charDimOnTextEditorApp[app.editCharInx]

# Source
# https://www.youtube.com/watch?v=WM1z8soch0Q
# Sockets Tutorial with Python 3 part 3 - sending and receiving Python Objects w/ Pickle
# sentdex
def send(app):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((app.hostName, app.portNumber))
    s.listen(5)

    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    app.socketFeedback = f'Connection from {address} has been established!'

    d = (app.e, app.n)
    msg = pickle.dumps(d)
    msg = bytes(f'{len(msg):<{app.HEADERSIZE}}', 'utf-8') + msg

    clientsocket.send(msg)

# Source
# https://www.youtube.com/watch?v=WM1z8soch0Q
# Sockets Tutorial with Python 3 part 3 - sending and receiving Python Objects w/ Pickle
# sentdex
def recieve(app):
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((app.hostName, app.portNumber))

    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:app.HEADERSIZE])
            new_msg = False
        
        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            print('full msg recieved')
            app.socketFeedback = 'full msg recieved'

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''
            break

    app.e, app.h = d
    print(f'app.e = {app.e}, app.n = {app.h}')
    keysString = f'Public Key {app.e}\nPrivate Key {app.d}\nn {app.n}'
    writeFile('rsaKeys.txt', keysString)


# source : https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(fileName):
    with open(fileName, "rt") as f:
        return f.read()

# source : https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def writeFile(fileName, contents):
    with open(fileName, "wt") as f:
        f.write(contents)

def readKeysFromFile(app):
    s = readFile('rsaKeys.txt')
    l = s.split('\n')
    for i in range(len(l)):
        l[i] = l[i].split(' ')
    app.e = int(l[0][-1])
    app.d = int(l[1][-1])
    app.n = int(l[2][-1])

def updateAppDotText(app):
    newTextString = ''
    for char in app.textEncodeL[:-1]:
        newTextString += char
    app.text = newTextString
    app.editCharInx = len(app.textEncodeL) - 1

def updateAppDotTextEncodeL(app):
    newTextList = list()
    for char in app.text:
        newTextList.append(char)
    newTextList.append('END')
    app.textEncodeL = newTextList
    app.editCharInx = len(app.textEncodeL) - 1
    print(f'app.textEncodeL = {app.textEncodeL} ****************')

def drawFile(app, canvas, x0, y0, x1, y1):
    canvas.create_rectangle(x0,y0,x1, y1,fill='yellow')
    canvas.create_rectangle(x1 - (x1 - x0)/8, y0 + (y1 - y0)/2,x1 + (x1 - x0)/8,y1,fill='yellow')

def drawFileWrapper(app, canvas, x0, y0):
    drawFile(app, canvas, x0, y0, x0 + 14, y0 + 18)

def encryptText(app):
    encryptedHexString = ''
    textInHexAsciiList = list()
    keyInHexAsciiList = list()
    for char in app.encryptionKey:
        asciiIntValOfChar = ord(char)
        hexValOfAsciiChar = hex(asciiIntValOfChar)[2:]
        if len(hexValOfAsciiChar) == 1:
            hexValOfAsciiChar = '0' + hexValOfAsciiChar
        keyInHexAsciiList.append(hexValOfAsciiChar)
    for char in app.text:
        asciiIntValOfChar = ord(char)
        hexValOfAsciiChar = hex(asciiIntValOfChar)[2:]
        if len(hexValOfAsciiChar) == 1:
            hexValOfAsciiChar = '0' + hexValOfAsciiChar
        textInHexAsciiList.append(hexValOfAsciiChar)
    if len(textInHexAsciiList) % 16 != 0:
        for fillInZeroesCount in range(16 - (len(textInHexAsciiList) % 16)):
            textInHexAsciiList.append('00')
    cipherKey = [keyInHexAsciiList[0:4], keyInHexAsciiList[4:8], keyInHexAsciiList[8:12], keyInHexAsciiList[12:16]]
    print(f'\n\n\n\n\n\n\n\n\n cipherKey = {cipherKey}')
    while len(textInHexAsciiList) > 0:
        rowsInARow = textInHexAsciiList[:16]
        textInHexAsciiList = textInHexAsciiList[16:]
        stateRow1 = rowsInARow[0:4]
        stateRow2 = rowsInARow[4:8]
        stateRow3 = rowsInARow[8:12]
        stateRow4 = rowsInARow[12:16]
        state = [stateRow1, stateRow2, stateRow3, stateRow4]
        result = aesEncryption(state, cipherKey)
        for row in result:
            for val in row:
                encryptedHexString += val
    print(f'\n\n\n\n\n\n\n\n encryptedHexString = {encryptedHexString}****************************\n\n\n\n\n\n\n\n\n')
    app.text = encryptedHexString
    updateAppDotTextEncodeL(app)
    app.editCharInx = len(app.textEncodeL) - 1

def decryptText(app):
    print('aes decryption start!!!!')
    decryptedString = ''
    textInHexAsciiList = list()
    keyInHexAsciiList = list()
    for char in app.encryptionKey:
        asciiIntValOfChar = ord(char)
        hexValOfAsciiChar = hex(asciiIntValOfChar)[2:]
        if len(hexValOfAsciiChar) == 1:
            hexValOfAsciiChar = '0' + hexValOfAsciiChar
        keyInHexAsciiList.append(hexValOfAsciiChar)
    twoDigitHexInStr  = ''
    for char in app.text:
        if len(twoDigitHexInStr) == 2:
            textInHexAsciiList.append(twoDigitHexInStr)
            twoDigitHexInStr = char
        else:
            twoDigitHexInStr += char
    textInHexAsciiList.append(twoDigitHexInStr)
    print(f'textInHexAsciiList = {textInHexAsciiList}')
    # if len(textInHexAsciiList) % 16 != 0:         # ERROR FROM COPY PASTING!!!
    #     for count in range(16 - (len(textInHexAsciiList) % 16)):
    #         textInHexAsciiList.append('00')
    cipherKey = [keyInHexAsciiList[0:4], keyInHexAsciiList[4:8], keyInHexAsciiList[8:12], keyInHexAsciiList[12:16]]
    while len(textInHexAsciiList) > 0:
        rowsInARow = textInHexAsciiList[:16]
        textInHexAsciiList = textInHexAsciiList[16:]
        stateRow1 = rowsInARow[0:4]
        stateRow2 = rowsInARow[4:8]
        stateRow3 = rowsInARow[8:12]
        stateRow4 = rowsInARow[12:16]
        state = [stateRow1, stateRow2, stateRow3, stateRow4]
        result = aesDecryption(state, cipherKey)
        for row in result:
            for val in row:
                c = chr(int(val, 16))
                if c != '\x00':
                    decryptedString += c
    app.text = decryptedString
    print(app.text)
    updateAppDotTextEncodeL(app)
    app.editCharInx = len(app.textEncodeL) - 1
    print('aes decryption ended!!!!!!!!!!')
    
def rsaEncryptText(app):
    asciiIntTextL = list()
    encryptedValInStr = list()
    for val in app.textEncodeL[:-1]:
        print(val)
        asciiIntTextL.append(int(ord(val)))
    for x in asciiIntTextL:
        print(f'x = {x}')
        print(type(x))
        app.rsaEncryptedL.append(rsaEncrypt(x, app.e, app.n))
    print(f'app.rsaEncryptedL = {app.rsaEncryptedL}')
    print(f'len(app.rsaEncryptedL) = {len(app.rsaEncryptedL)}')
    for encryptedInt in app.rsaEncryptedL:
        print(f'str(encryptedInt) = {str(encryptedInt)}')
        print(type(str(encryptedInt)))
        for char in str(encryptedInt):
            #print(f'char = {char}')
            #print(type(char))
            encryptedValInStr.append(char)
        encryptedValInStr.append(',')
    encryptedValInStr = encryptedValInStr[:-1]
    print(f'encryptedValInStr = {encryptedValInStr}')
    app.textEncodeL = encryptedValInStr
    print(f'app.textEncodeL = {app.textEncodeL}')
    updateAppDotText(app)
    print(f'app.text = {app.text}')

def rsaDecryptText(app):
    decryptedAsciiIntL = list()
    decryptedStringValsL = list()
    for y in app.rsaEncryptedL:
        print(f'type({y}) = {type(y)}')
        decryptedAsciiIntL.append(rsaDecrypt(y, app.d, app.n))
    app.rsaEncryptedL = list()
    print(f'decryptedAsciiIntL = {decryptedAsciiIntL}')
    for ascii in decryptedAsciiIntL:
        print(f'ascii = {ascii}')
        decryptedStringValsL.append(chr(ascii))
    decryptedStringValsL.append('END')
    app.textEncodeL = decryptedStringValsL
    print(f'app.textEncodeL = {app.textEncodeL}')
    updateAppDotText(app)
    print(f'app.text = {app.text}')


    

def drawTextEditor(app,canvas):
    canvas.create_rectangle(-1,-1,app.width+5,app.height+5,fill='#FFFFF0')
    
    if app.saveOperationUndergo == True:
        print(f'app.saveOperationUndergo == True in drawTextEditor')
        print(f'***/***')
        canvas.create_rectangle(-1,-1,app.width+5,app.height+5,fill='#FFFFF0')
        print(f'***/***/*')
        canvas.create_text(5,5,text='Enter file name to save: ', font=app.currFontName, anchor='nw')
        print(f'***/***/**')
        canvas.create_text(150,5,text=app.saveFileName, font=app.currFontName, anchor='nw')
        print(f'***/***/***')
        pass
    elif app.openOperationUndergo == True:
        print(f'***/***\t\t***')
        nextFileY = 3
        for fileCount in range(len(app.filesUnderTermProject)):
            drawFileWrapper(app, canvas, 3, nextFileY)
            canvas.create_text(25, nextFileY + 9, text=app.filesUnderTermProject[fileCount], font=app.currFontName, anchor='w')
            x0,y0,x1,y1 = app.filesUnderTermProjectDim[fileCount]
            #canvas.create_rectangle(x0-3,y0-3,x1+3,y1+3)
            nextFileY += 30
    elif app.encryptOperationUndergo == True or app.decryptOperationUndergo == True:
        canvas.create_rectangle(-1,-1,app.width+5,app.height+5,fill='#FFFFF0')
        canvas.create_text(5,5,text='Enter encryption key: ', font=app.currFontName, anchor='nw')
        canvas.create_text(140,5,text=app.encryptionKey, font=app.currFontName, anchor='nw')
    elif app.rsaKeyCreateUndergo == True or app.rsaEncryptUndergo == True or app.rsaDecryptUndergo == True:
        print(f'app.rsaKeyCreateUndergo = {app.rsaKeyCreateUndergo}')
        print(f'app.rsaEncryptUndergo = {app.rsaEncryptUndergo}')
        print(f'app.rsaDecryptUndergo = {app.rsaDecryptUndergo}')
        print('\n\n\n\n\n')
        canvas.create_rectangle(-1,-1,app.width+5,app.height+5,fill='#FFFFF0')
        canvas.create_text(5,5,text=f'Public key : {app.e}', font=app.currFontName, anchor='nw')
        canvas.create_text(5,20,text=f'Private Key : {app.d}', font=app.currFontName, anchor='nw')
        canvas.create_text(5,35,text=f'max size : {app.n}', font=app.currFontName, anchor='nw')
    elif app.sendUndergo == True or app.recieveUndergo == True:
        canvas.create_text(5,5,text=f'hostname : {app.hostName}', font=app.currFontName, anchor='nw')
        canvas.create_text(5,20,text=f'portnumber : {app.portNumber}', font=app.currFontName, anchor='nw')
        canvas.create_text(5,35,text=f'{app.socketFeedback}', font=app.currFontName, anchor='nw')
    else:
        print(f'***/***\t\t***\t\t***')
        drawHighlight(app, canvas)

        print(f'len(app.textEncodeL) = {len(app.textEncodeL)}')
        print(f'len(app.charDimOnTextEditorApp) = {len(app.charDimOnTextEditorApp)}')
        if len(app.charDimOnTextEditorApp) == len(app.textEncodeL):
            for charInx in range(len(app.textEncodeL)):
                charString = app.textEncodeL[charInx]
                charLocationDim = app.charDimOnTextEditorApp[charInx]
                x0, y0, x1, y1 = charLocationDim
                if charString != 'END': # and charString != '\n'
                    canvas.create_text(x0, y0, text=charString, font=app.currFontName, anchor='nw')
                canvas.create_rectangle(x0, y0, x1, y1)

        moveEditPositionColorByClick(app, canvas)
            
        canvas.create_rectangle(-1,-1,app.width+5,30,fill='#FFFFF0')
        canvas.create_rectangle(app.saveButtonDim,fill='red')
        x0Save, y0Save, x1Save, y1Save = app.saveButtonDim
        canvas.create_text((x0Save+x1Save)/2, (y0Save+y1Save)/2, text='Save', font=app.currFontName)
        canvas.create_rectangle(app.openButtonDim,fill='yellow')
        x0Open, y0Open, x1Open, y1Open = app.openButtonDim
        canvas.create_text((x0Open+x1Open)/2, (y0Open+y1Open)/2, text='Open', font=app.currFontName)
        canvas.create_rectangle(app.encryptButtonDim,fill='pink')
        x0Encrypt, y0Encrypt, x1Encrypt, y1Encrypt = app.encryptButtonDim
        canvas.create_text((x0Encrypt+x1Encrypt)/2, (y0Encrypt+y1Encrypt)/2, text='aesEncrypt', font=app.currFontName)
        canvas.create_rectangle(app.decryptButtonDim,fill='green')
        x0Decrypt, y0Decrypt, x1Decrypt, y1Decrypt = app.decryptButtonDim
        canvas.create_text((x0Decrypt+x1Decrypt)/2, (y0Decrypt+y1Decrypt)/2, text='aesDecrypt', font=app.currFontName)
        canvas.create_rectangle(app.rsaCreateKeyButtonDim,fill='purple')
        x0RSAKey, y0RSAKey, x1RSAKey, y1RSAKey = app.rsaCreateKeyButtonDim
        canvas.create_text((x0RSAKey+x1RSAKey)/2, (y0RSAKey+y1RSAKey)/2, text='create rsaKeys', font=app.currFontName)
        canvas.create_rectangle(app.rsaEncryptButtonDim,fill='orange')
        x0RSAEncrypt, y0RSAEncrypt, x1RSAEncrypt, y1RSAEncrypt = app.rsaEncryptButtonDim
        canvas.create_text((x0RSAEncrypt+x1RSAEncrypt)/2, (y0RSAEncrypt+y1RSAEncrypt)/2, text='rsaEncrypt', font=app.currFontName)
        canvas.create_rectangle(app.rsaDecryptButtonDim,fill='#87CEEB')
        x0RSADecrypt, y0RSADecrypt, x1RSADecrypt, y1RSADecrypt = app.rsaDecryptButtonDim
        canvas.create_text((x0RSADecrypt+x1RSADecrypt)/2, (y0RSADecrypt+y1RSADecrypt)/2, text='rsaDecrypt', font=app.currFontName)
        canvas.create_rectangle(app.sendPublicKeyButtonDim,fill='#87CEEB')
        x0Send, y0Send, x1Send, y1Send = app.sendPublicKeyButtonDim
        canvas.create_text((x0Send+x1Send)/2, (y0Send+y1Send)/2, text='send rsa PublicK', font=app.currFontName)
        canvas.create_rectangle(app.recievePublicKeyButtonDim,fill='#87CEEB')
        x0Recieve, y0Recieve, x1Recieve, y1Recieve = app.recievePublicKeyButtonDim
        canvas.create_text((x0Recieve+x1Recieve)/2, (y0Recieve+y1Recieve)/2, text='recieve rsa PublicK', font=app.currFontName)


def drawHighlight(app, canvas):
    for highlightInx in app.highlightInxList:
        x0, y0, x1, y1 = app.charDimOnTextEditorApp[highlightInx]
        img1 = makeTranslucentRectangle(app, (x1-x0), (y1-y0), "Blue", 0.2)
        canvas.create_image((x0+x1)/2, (y0+y1)/2, image=img1)

def moveEditPositionColorByClick(app, canvas):
    if app.editCharDim == (-30, -30, -30, -30):
        x0, y0, x1, y1 = app.endEditCharDim
    else:
        x0, y0, x1, y1 = app.editCharDim
    canvas.create_rectangle(x0, y0, x1, y1, fill='black')
    
    editPositionCharString = app.textEncodeL[app.editCharInx]
    if editPositionCharString != 'END':
        canvas.create_text(x0, y0, text=editPositionCharString, font=app.currFontName, fill='white', anchor='nw')
    


# creates img for translucent rectangle
# Source : Kian Nassre
def makeTranslucentRectangle(app, width, height, fill, opacity):
    fill = app._root.winfo_rgb(fill) + (int(255*opacity),)
    image = Image.new('RGBA', (width, height), fill)
    return ImageTk.PhotoImage(image)


def fontTextSizes(app, canvas, fontName=None):
    charSizeDict = dict()
    maxWidth = 0
    for alphabet in string.printable: 
        newTextID = canvas.create_text(0, 0, text=alphabet, font={fontName}, anchor='nw')
        x0, y0, x1, y1 = canvas.bbox(newTextID)
        charSizeDict[alphabet] = (x0+1, y0, x1+1, y1)
        if x1-x0 > maxWidth:
            maxWidth = x1-x0
    print(f'\n{fontName} charSizeDict={charSizeDict}')
    print(f'maxWidth = {maxWidth}')
    return charSizeDict

def testTextID(app, canvas):
   textID1 = canvas.create_text(100, 100, text="H", anchor='nw')
   x00, y00, x10, y10 = canvas.bbox(textID1)
   canvas.create_rectangle(x00+1, y00, x10-1, y10)
   textID2 = canvas.create_text(x10, 100, text="i", anchor='nw')
   x01, y01, x11, y11 = canvas.bbox(textID2)
   canvas.create_rectangle(x01+1, y01, x11-1, y11)
   textID3 = canvas.create_text(x11, 100, text=" ", anchor='nw')
   x02, y02, x12, y12 = canvas.bbox(textID3)
   canvas.create_rectangle(x02+1, y02, x12-1, y12)
   textID4 = canvas.create_text(x12, 100, text="m", anchor='nw')
   x03, y03, x13, y13 = canvas.bbox(textID4)
   canvas.create_rectangle(x03+1, y03, x13-1, y13)
   print(f'x00, y00, x10, y10 = {x00, y00, x10, y10}')
   print(f'x01, y01, x11, y11 = {x01, y01, x11, y11}')
   print(f'x02, y02, x12, y12 = {x02, y02, x12, y12}')
   print(f'x03, y03, x13, y13 = {x03, y03, x13, y13}')
   

def redrawAll(app, canvas):
    drawTextEditor(app,canvas)
    pass

runApp(width=900, height=900)