import library
import datetime

class User(library.Library):

    def __init__(self):
        super().__init__()
        self.surname = 'no info'
        self.dateOfBirth = 'no info'
        self.role = 'no info'
        self.spec = 'no info'
        self.password = 'no info'


    def signIn(self,signName,signSurname,signDateOfBirth,signRole,signEmail,signLibrarianId,signPsw):

        isNameTrue = True
        selectedOption = signRole
        kayitlanmaDurumu = ''

        if len(str(signName))<4 or len(str(signSurname))<4:
            kayitlanmaDurumu = 'Name or Surname must consist of at least four characters.'
            isNameTrue=False

        try:
            datetime.datetime.strptime(signDateOfBirth, '%d/%m/%Y')
            isTimeFormatRight = True
        except:
            isTimeFormatRight = False
            
        if isTimeFormatRight and isNameTrue:
            try:
                psw = int(signPsw)
            except:
                psw = signPsw
            if isinstance(psw,int):
                if psw>99999 and psw<1000000:
                    kayitlanmaDurumu = "Registration Successful"
                    if selectedOption == 'Librarian':
                        try:
                            librarianId = int(signLibrarianId)
                        except:
                            ktpId = signLibrarianId
                            if isinstance(ktpId,int):
                                if ktpId>99999999 and ktpId<1000000000:
                                    kayitlanmaDurumu = 'Registration Successful'
                                else:
                                    kayitlanmaDurumu = 'Librarian Id must be nine Digits'
                            else:
                                kayitlanmaDurumu = 'Librarian Id must consist of numbers'
                    elif selectedOption == "Member":
                        if str(signEmail.get()).endswith('.com'):
                            kayitlanmaDurumu = 'Registration Successful'
                        else:
                            kayitlanmaDurumu = 'Email address must end with .com'

                else:
                    kayitlanmaDurumu = 'Password must be six Digits'
            else:
                kayitlanmaDurumu = 'Password must consist of numbers'
        elif isNameTrue and not isTimeFormatRight:
            kayitlanmaDurumu = 'Date format is not true'

        if kayitlanmaDurumu == 'Registration Successful':
            usrName = str(signName)
            usrSurname = str(signSurname)
            usrPsw = str(signPsw)
            usrRole = str(selectedOption)
            usrSpecialInfo =lambda usrRole:str(signEmail) if usrRole == 'Member' else str(signLibrarianId)
            usrSpInfo = usrSpecialInfo(usrRole)
            usrIdInfo = lambda usrRole: self.giveId('member') if usrRole == 'Member' else self.giveId('librarian')
            usrIdInfo(usrRole)
            usrRgDate = str(datetime.datetime.now().day) + '/' + str(datetime.datetime.now().month) + '/' + str(datetime.datetime.now().year)
            usersFile = self.openTxtFile('users','a+')
            usersFile.write(f'{self.Id},{usrName},{usrSurname},{signDateOfBirth},{usrPsw},{usrRole},{usrSpInfo},{usrRgDate}\n')
            usersFile.close()
        
        return kayitlanmaDurumu
    

    def login(self,lName,lPassword,lRole):

        girisDurum = f'incorrect information entered'

        self.file = self.openTxtFile('users','r')

        if self.file == False:

            return 'The file containing the users is empty or not found'
        
        for line in self.file.readlines():

            line = line.split(',')
            chkSpec = line[6]
            chkPsw = line[4]
            chkRole = line[5]
            if chkSpec ==  lName and chkPsw ==  lPassword and chkRole == lRole:
                self.Id = line[0]
                self.name = line[1]
                self.surname = line[2]
                self.dateOfBirth = line[3]
                self.password = line[4]
                self.role = line[5]
                self.spec = line[6]
                self.registrationDate = line[7].strip('\n')

                girisDurum = 'Login Successful'
        
        self.file.close()
        return girisDurum