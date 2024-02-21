import user
import datetime
import time
import os

class Librarian(user.User):

    def __init__(self):
        super().__init__()
        self.file = self.openTxtFile('books','a+')
    def __del__(self):
        self.file.close()

    def listItems(self,itemType):
        self.file = self.openTxtFile(itemType,'r')
        listOfItems = []
        for lines in self.file.readlines():
            listOfItems.append(lines.split(',')[1:5])
        self.file.close() 
        return listOfItems
    

    def addLibraryItems(self,itemType,addName,addPerson,addReleaseDate,addPageNumorDuration,addStockNumber,addShelfNumber):
        self.file = self.openTxtFile(itemType,'a+')
        
        situationMessage = self.checkFormat(addName,addPerson,addReleaseDate,addPageNumorDuration,addStockNumber,addShelfNumber)
        self.giveId(itemType)
        regTime = str(datetime.datetime.now().day) + '/' + str(datetime.datetime.now().month) + '/' + str(datetime.datetime.now().year) 
        
        if str(situationMessage) == 'Successful' and not self.isThereSameItem(itemType,addName,addPerson):  
            self.file.write(f'{self.Id},{addName},{addPerson},{addReleaseDate},{addPageNumorDuration},{regTime},{addStockNumber},{addShelfNumber}\n')
        elif self.isThereSameItem(itemType,addName,addPerson):
            self.changeQuantity(itemType,addName,addPerson,addReleaseDate,addPageNumorDuration,addStockNumber,addShelfNumber)
        self.file.close()
        return situationMessage
    
    

    def checkFormat(self,chkName,chkPerson,chkRelaseDate,chkPageNum,chkStckNum,chkShNum):
        situationMessage = ''

        if len(chkName) > 4:
            if len(chkPerson) > 4:
                try: 
                    datetime.datetime.strptime(chkRelaseDate, '%d/%m/%Y')
                    try:
                        int(chkPageNum)
                        try:
                            int(chkStckNum)
                            try:
                                int(chkShNum)
                                situationMessage = 'Successful'
                            except:
                                situationMessage = 'Entered Shelf Number must be Number'
                        except:
                            situationMessage = 'Entered Stock Number must be Number'
                    except:
                        situationMessage = 'Entered Page Number or Duration must be Number'
                except:
                    situationMessage = 'Date Format is not Right'
            else:
                situationMessage = 'Person Name Must be at Least 4 char'
        else:
            situationMessage = 'Name Must be at Least 4 char'    


        return situationMessage
    
    def isThereSameItem(self,itemType,isName, isPerson):
        file = self.openTxtFile(itemType,'r')
        isThereSame = False
        for line in file.readlines():
            chckItemName = line.split(',')[1]
            chckItemPerson = line.split(',')[2]
            if isName == chckItemName and isPerson == chckItemPerson:
                isThereSame = True
        
        return isThereSame

    def changeQuantity(self,itemType,qName,qPerson,qRlsDate,qPageNumorDuration,qStcNum,qShelfNum):
        self.file = self.openTxtFile(itemType,'r')
        for line in self.file.readlines():
            line = line.split(',')
            ckName = line[1]
            ckPerson = line[2]
            if str(ckName) == str(qName) and str(ckPerson) == str(qPerson):
                qStcNum = int(qStcNum) + int(line[6])
                qShelfNum = int(qShelfNum) + int(line[7])
        self.removeLibraryItem(itemType,qName)
        self.addLibraryItems(itemType,qName,qPerson,qRlsDate,qPageNumorDuration,qStcNum,qShelfNum)

    def removeLibraryItem(self,itemType,rmvItemName):
        
        if not os.path.exists(itemType+'.txt'):
            return (f'{rmvItemName} is not in Library')
        elif rmvItemName == '':
            return
        self.file = self.openTxtFile(itemType,'r')
        lines = self.file.readlines()
        if any(rmvItemName in line for line in lines):
            newLines = [line for line in lines if not rmvItemName in line] 
            self.file = self.openTxtFile(itemType,'w')
            for line in newLines:   
                self.file.write('{}'.format(line))
            return f'{rmvItemName} is removed'
        else:
            return (f'{rmvItemName} is not in Library')

    