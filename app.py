import customtkinter as ctk 
import tkinter as tk
import datetime

class UserInterface(ctk.CTk):

    def __init__(self):

        super().__init__()
        # Selecting GUI theme - dark, light , system (for system default) 
        self.selectedOption= ''
        ctk.set_appearance_mode("dark") 

        # Selecting color theme - blue, green, dark-blue 
        ctk.set_default_color_theme("blue")
 
        self.geometry("1200x700") 
        self.title("Bootcamp Library")
        self.islemler()

    def islemler(self):
        self.karsilama()

    def karsilama(self):
        karsilama=ctk.CTkFrame(self,fg_color='transparent')
        karsilama.pack(fill='both',expand=True,pady=280)
        karsilamaBankaIsimLbl=ctk.CTkLabel(karsilama,text='Bootcamp Library',font=('text',16))
        karsilamaBankaIsimLbl.pack(pady=5)
        karsilamaLbl=ctk.CTkLabel(karsilama,text='Welcome',font=('Brush Script MT',32))
        karsilamaLbl.pack(pady=0,padx=0)
        karsilama.after(1000,lambda:self.girisEkrani())
        karsilama.after(1000,lambda:karsilama.destroy())

    def girisEkrani(self):
        
        tabview = ctk.CTkTabview(self,fg_color='transparent',width=360,height=700)
        tabview.pack(pady=10,padx=10,expand=True,fill='both')
        tabview.add("Librarian") 
        tabview.add("Member")

        self.loginMessage = ''

        def openFileForLogin():
            try:
                self.fileFLogin = open('users.txt','r',encoding='utf-8')
            except:
                self.loginMessage = 'No registered user found'
            

        def girisYap():
            enteredUsrName = str(kullaniciAdiLogin.get())
            enteredMailAdr = str(eMailLogin.get())
            enteredPsw = str(parolaLogin.get())
            isEnteredTrue = False
            openFileForLogin()
            for line in self.fileFLogin.readlines():
                line = line.split(',')
                sName = line[0]
                sSurname = line[1]
                sUserPsw = line[2]
                sUserState = line[3]
                sUserSpec = line[4]
                if (sUserSpec == enteredMailAdr and sUserPsw == enteredPsw) or (sUserSpec == enteredUsrName and sUserPsw == enteredPsw):
                    gName = sName
                    gSurname = sSurname
                    gUserState = sUserState
                    isEnteredTrue = True

            print(f'{isEnteredTrue} {enteredUsrName} {sUserSpec}')


        def girisSayfasiniAc(self,ks):
                ks.pack_forget()
                self.girisEkrani()

        def kayitOl():
            librarianFrame.destroy()
            memberFrame.destroy()
            tabview.destroy()

            kayitSayfasi=ctk.CTkFrame(self) 
            kayitSayfasi.pack(pady=20,padx=40,fill='both',expand=True) 
            kayitSayfasiLbl=ctk.CTkLabel(kayitSayfasi,text="Kayıt Ol")
            kayitSayfasiLbl.pack(pady=12,padx=10)
            
            self.kutuphaneciId= ctk.CTkEntry(kayitSayfasi,placeholder_text='Librarian Id')
            self.kullaniciEmail= ctk.CTkEntry(kayitSayfasi,placeholder_text='Email')
            self.kayitOlB = ctk.CTkButton(kayitSayfasi,text='Kayıt Ol',command= lambda:kayitDurum(self))
            self.geriDonB = ctk.CTkButton(kayitSayfasi,text='Geri Dön',command=lambda:girisSayfasiniAc(self,kayitSayfasi)) 

            
            def selectedState(choice):
                self.selectedOption = choice
                if self.kutuphaneciId.winfo_ismapped() or self.kullaniciEmail.winfo_ismapped():
                    self.kullaniciEmail.pack_forget()
                    self.kutuphaneciId.pack_forget()
                    self.geriDonB.pack_forget()
                    self.kayitOlB.pack_forget()
                shownSelected()

            def shownSelected():
                self.geriDonB.pack_forget()
                if self.selectedOption=="Librarian":
                    self.kutuphaneciId.pack(pady=12,padx=10)
                elif self.selectedOption=="Member":
                    self.kullaniciEmail.pack(pady=12,padx=10)

                 
                self.kayitOlB.pack(pady=12,padx=10)
                self.geriDonB.pack(pady=12,padx=10)
                

            combobox = ctk.CTkOptionMenu(kayitSayfasi,values=["Librarian", "Member"],command=selectedState)
            combobox.pack(padx=20, pady=10)
            combobox.set("Choose Role")

            kullaniciAd= ctk.CTkEntry(kayitSayfasi,placeholder_text="Name") 
            kullaniciAd.pack(pady=12,padx=10)

            kullaniciSoyad= ctk.CTkEntry(kayitSayfasi,placeholder_text="Surname") 
            kullaniciSoyad.pack(pady=12,padx=10)

            kullaniciDogum= ctk.CTkEntry(kayitSayfasi,placeholder_text="Date of Birth(mm/dd/yyyy)") 
            kullaniciDogum.pack(pady=12,padx=10)

            kullaniciSifre= ctk.CTkEntry(kayitSayfasi,placeholder_text="Password",show="*") 
            kullaniciSifre.pack(pady=12,padx=10)     

            self.geriDonB.pack(pady=12,padx=10)

            def kayitDurum(self):
                kayitlanmaDurumu = ''
                isNameTrue = True

                if len(str(kullaniciAd.get()))<4 or len(str(kullaniciSoyad.get()))<4:
                    kayitlanmaDurumu = 'Name or Surname must consist of at least four characters.'
                    isNameTrue=False

                try:
                    datetime.datetime.strptime(kullaniciDogum.get(), '%d/%m/%Y')
                    isTimeFormatRight = True
                except:
                    isTimeFormatRight = False
                    
                if isTimeFormatRight and isNameTrue:
                    try:
                        psw = int(kullaniciSifre.get())
                    except:
                        psw = kullaniciSifre.get()
                    if isinstance(psw,int):
                        if psw>99999 and psw<1000000:
                            kayitlanmaDurumu = "Registration Successful"
                            if self.selectedOption == 'Librarian':
                                try:
                                    ktpId = int(self.kutuphaneciId.get())
                                except:
                                    ktpId = self.kutuphaneciId.get()
                                    if isinstance(ktpId,int):
                                        if ktpId>99999999 and ktpId<1000000000:
                                            kayitlanmaDurumu = 'Registration Successful'
                                        else:
                                            kayitlanmaDurumu = 'Librarian Id must be nine Digits'
                                    else:
                                        kayitlanmaDurumu = 'Librarian Id must consist of numbers'
                            elif self.selectedOption == "Member":
                                if str(self.kullaniciEmail.get()).endswith('.com'):
                                    kayitlanmaDurumu = 'Registration Successful'
                                else:
                                    kayitlanmaDurumu = 'Email address must end with .com'

                        else:
                            kayitlanmaDurumu = 'Password must be six Digits'
                    else:
                        kayitlanmaDurumu = 'Password must consist of numbers'
                elif isNameTrue and not isTimeFormatRight:
                    kayitlanmaDurumu = 'Date format is not true'

                kayitDurumlbl=ctk.CTkLabel(kayitSayfasi,text=kayitlanmaDurumu)
                kayitDurumlbl.pack(pady=12,padx=10)
                kayitDurumlbl.after(1500,lambda:kayitDurumlbl.destroy())

                if kayitlanmaDurumu == 'Registration Successful':
                    usrName = str(kullaniciAd.get())
                    usrSurname = str(kullaniciSoyad.get())
                    usrPsw = str(kullaniciSifre.get())
                    usrRole = str(self.selectedOption)
                    usrSpecialInfo =lambda usrRole:str(self.kullaniciEmail.get()) if usrRole == 'Member' else str(self.kutuphaneciId.get())
                    usrSpInfo = usrSpecialInfo(usrRole)
                    usersFile = open('users.txt','a+',encoding='utf-8')
                    usersFile.write(f'{usrName},{usrSurname},{usrPsw},{usrRole},{usrSpInfo}\n')
                    usersFile.close()
                    kayitBasariliLbl=ctk.CTkLabel(app,text='Registration Successful \n\n\n\nYou are directed to the login page',font=('text',16))
                    kayitBasariliLbl.after(1000,lambda:kayitBasariliLbl.pack(pady=150))
                    kayitBasariliLbl.after(1000,lambda:kayitSayfasi.destroy())
                    kayitBasariliLbl.after(3000,self.girisEkrani)
                    kayitBasariliLbl.after(3000,lambda:kayitBasariliLbl.destroy())
            
        
        librarianFrame = ctk.CTkFrame(tabview.tab('Librarian')) 
        librarianFrame.pack(pady=20,padx=40,fill='both',expand=True)    

        label = ctk.CTkLabel(librarianFrame,text='Login Page') 
        label.pack(pady=12,padx=10) 


        kullaniciAdiLogin= ctk.CTkEntry(librarianFrame,placeholder_text="Employee Id") 
        kullaniciAdiLogin.pack(pady=12,padx=10) 

        parolaLogin= ctk.CTkEntry(librarianFrame,placeholder_text="Password",show="*") 
        parolaLogin.pack(pady=12,padx=10) 


        girisYapB = ctk.CTkButton(librarianFrame,text='Login',command=girisYap) 
        girisYapB.pack(pady=12,padx=10)

        kayitOlB = ctk.CTkButton(librarianFrame,text='Sign in',command=kayitOl)
        kayitOlB.pack(pady=12,padx=10)

        memberFrame = ctk.CTkFrame(tabview.tab('Member')) 
        memberFrame.pack(pady=20,padx=40,fill='both',expand=True)    

        label = ctk.CTkLabel(memberFrame,text='Login Page') 
        label.pack(pady=12,padx=10) 


        eMailLogin= ctk.CTkEntry(memberFrame,placeholder_text="Email") 
        eMailLogin.pack(pady=12,padx=10) 

        parolaLogin= ctk.CTkEntry(memberFrame,placeholder_text="Password",show="*") 
        parolaLogin.pack(pady=12,padx=10) 


        girisYapB = ctk.CTkButton(memberFrame,text='Login',command=girisYap) 
        girisYapB.pack(pady=12,padx=10)

        kayitOlB = ctk.CTkButton(memberFrame,text='Sign in',command=kayitOl)
        kayitOlB.pack(pady=12,padx=10)


if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()