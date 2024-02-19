import random
import os

class Library():

    def __init__(self):
        self.name = 'none'
        self.registrationDate = 'none'
        self.Id = 'none'

    def giveId(self,idType):
        firstTwoLetters = str(idType[:2].upper())
        if idType == 'member' or idType == 'librarian':
            idType = 'users'
        randomIdNum = str(random.randint(10000,100000))
        randId = str(firstTwoLetters + randomIdNum)
        if not self.isIdUsed(idType,randId):
            self.Id = randId
        else:
            return self.giveId(idType)


    def isIdUsed(self,idType,checkedId):
        isUsed = False
        if not os.path.exists(idType + '.txt'):
            return isUsed
        file = self.openTxtFile(idType,'r')
        for line in file.readlines():
            idFromFile = line.split(',')[0]
            if(str(idFromFile) == str(checkedId)):
                isUsed = True
        file.close()
        return isUsed

    def openTxtFile(self,fileName,openMode):
        fileName = fileName + '.txt'
        if not os.path.exists(fileName):
            return False
        return open(fileName,openMode,encoding='utf-8')
