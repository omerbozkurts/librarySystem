import random

class Library():

    def __init__(self):
        self.name = 'none'
        self.registrationDate = 'none'
        self.Id = 'none'

    def giveId(self,idType):
        firstTwoLetters = str(idType[:2].upper())
        randomIdNum = str(random.randint(10000,100000))
        randId = str(firstTwoLetters + randomIdNum)
        if not self.isIdUsed(idType,randId):
            self.Id = randId
        else:
            return self.giveId(idType)


    def isIdUsed(self,idType,checkedId):
        file = self.openTxtFile(idType,'r')
        isUsed = False
        for line in file.readlines():
            idFromFile = line.split(',')[0]
            if(str(idFromFile) == str(checkedId)):
                isUsed = True
        file.close()
        return isUsed

    def openTxtFile(self,fileName,openMode):
        fileName = fileName + '.txt'
        return open(fileName,openMode,encoding='utf-8')
