import customtkinter as ctk 
import tkinter as tk
import datetime
import random
import user
import librarian

isBooksCategorySelected = False
isMagazineCategorySelected = False
isDvdCategorySelected = False
lastSelectedCategory = None
lastSelectedFrame = None

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

        def girisYap():
            enteredUsrName = str(kullaniciAdiLogin.get())
            enteredUsrNamePsw = str(parolaLoginLibrarian.get())
            enteredMailAdr = str(eMailLogin.get())
            enteredMailPsw = str(parolaLoginMember.get())
            gRole = str(tabview._current_name)
            girisDurum = ''
            whichFrame = ''
            kullanici = user.User()

            if gRole == 'Member':
                girisDurum = kullanici.login(enteredMailAdr,enteredMailPsw,gRole)
                whichFrame = memberFrame
            elif gRole == 'Librarian':
                girisDurum = kullanici.login(enteredUsrName,enteredUsrNamePsw,gRole)
                whichFrame = librarianFrame

            girisDurumlbl=ctk.CTkLabel(whichFrame,text=girisDurum)
            girisDurumlbl.pack(pady=12,padx=10)
            girisDurumlbl.after(1500,lambda:girisDurumlbl.destroy())

            girisDurum = 'Login Successful' #silinecek

            if girisDurum == 'Login Successful':

                kayitBasariliLbl=ctk.CTkLabel(app,text='Login Successful \n\n\n\nYou are directed to the app',font=('text',16))
                kayitBasariliLbl.after(1000,lambda:kayitBasariliLbl.pack(pady=150))
                kayitBasariliLbl.after(1000,lambda:tabview.destroy())
                kayitBasariliLbl.after(3000,lambda:self.anasayfa(kullanici))
                kayitBasariliLbl.after(3000,lambda:kayitBasariliLbl.destroy())


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
            self.kayitOlB = ctk.CTkButton(kayitSayfasi,text='Kayıt Ol',command= lambda:kayitDurum())
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

            def kayitDurum():
                kayitlanmaDurumu = str(user.User().signIn(kullaniciAd.get(),
                                                        kullaniciSoyad.get(),kullaniciDogum.get(),self.selectedOption,
                                                        self.kullaniciEmail.get(),self.kutuphaneciId.get(),kullaniciSifre.get()))
            
                kayitDurumlbl=ctk.CTkLabel(kayitSayfasi,text=kayitlanmaDurumu)
                kayitDurumlbl.pack(pady=12,padx=10)
                kayitDurumlbl.after(1500,lambda:kayitDurumlbl.destroy())

                if kayitlanmaDurumu == 'Registration Successful':

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

        parolaLoginLibrarian= ctk.CTkEntry(librarianFrame,placeholder_text="Password",show="*") 
        parolaLoginLibrarian.pack(pady=12,padx=10) 


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

        parolaLoginMember= ctk.CTkEntry(memberFrame,placeholder_text="Password",show="*") 
        parolaLoginMember.pack(pady=12,padx=10) 


        girisYapB = ctk.CTkButton(memberFrame,text='Login',command=girisYap) 
        girisYapB.pack(pady=12,padx=10)

        kayitOlB = ctk.CTkButton(memberFrame,text='Sign in',command=kayitOl)
        kayitOlB.pack(pady=12,padx=10)

    def anasayfa(self,kullanici):
        def librarianInterface():
            tabviewAnasayfa = ctk.CTkTabview(self,fg_color='transparent',width=360,height=700)
            tabviewAnasayfa.pack(pady=10,padx=10,expand=True,fill='both')
            tabviewAnasayfa.add("Add Item") 
            tabviewAnasayfa.add("Remove Item")
            tabviewAnasayfa.add('List Items')

            librarianFrameAnasayfaAdd = ctk.CTkFrame(tabviewAnasayfa.tab('Add Item')) 
            librarianFrameAnasayfaAdd.pack(pady=20,padx=40,fill='both',expand=True)

            label = ctk.CTkLabel(librarianFrameAnasayfaAdd,text='Add Item Page') 
            label.pack(pady=12,padx=10) 

            librarianFrameAnasayfaAddBook = ctk.CTkFrame(librarianFrameAnasayfaAdd)
            librarianFrameAnasayfaAddMagazine = ctk.CTkFrame(librarianFrameAnasayfaAdd)  
            librarianFrameAnasayfaAddDvd = ctk.CTkFrame(librarianFrameAnasayfaAdd)


            def selectedState(choice):
                global isBooksCategorySelected
                global isMagazineCategorySelected
                global isDvdCategorySelected
                global lastSelectedFrame
                
                selectedCategory = str(choice).lower()

                if lastSelectedFrame:
                    lastSelectedFrame.pack_forget()

                if selectedCategory == 'books':
                    if isBooksCategorySelected:
                        librarianFrameAnasayfaAddBook.pack(pady=20,padx=40,fill='both',expand=True)
                        lastSelectedFrame = librarianFrameAnasayfaAddBook
                        return
                    isBooksCategorySelected = True
                    librarianFrameAnasayfaAddBook.pack(pady=20,padx=40,fill='both',expand=True)   
                    lastSelectedFrame = librarianFrameAnasayfaAddBook

                    booksName= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Name") 
                    booksName.pack(pady=12,padx=10) 

                    booksAuthor= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Author") 
                    booksAuthor.pack(pady=12,padx=10) 

                    booksPublicationDate= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Publication Date") 
                    booksPublicationDate.pack(pady=12,padx=10)

                    booksPageNumber= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Page Number") 
                    booksPageNumber.pack(pady=12,padx=10)

                    booksStockQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Stock Quantity") 
                    booksStockQuantity.pack(pady=12,padx=10)

                    booksShelfQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Shelf Quantity") 
                    booksShelfQuantity.pack(pady=12,padx=10)


                    def addBook():
                        addStatus = None
                        sName = str(booksName.get())
                        sAuthor = str(booksAuthor.get())
                        sPublicationDate = str(booksPublicationDate.get())
                        sPageNum = str(booksPageNumber.get())
                        sStcQuantity = str(booksStockQuantity.get())
                        sShfQuantity = str(booksShelfQuantity.get())

                        addStatus = librarian.Librarian().addLibraryItems('books',sName,sAuthor,sPublicationDate,sPageNum,sStcQuantity,sShfQuantity)
                  

                        addBooklbl = ctk.CTkLabel(librarianFrameAnasayfaAddBook,text=addStatus) 
                        addBooklbl.pack(pady=12,padx=10)
                        addBooksButton.after(1000,lambda:addBooklbl.destroy()) 
                        

                    addBooksButton = ctk.CTkButton(librarianFrameAnasayfaAddBook,text='Add Book',command=addBook) 
                    addBooksButton.pack(pady=12,padx=10)

                        
                    

                elif selectedCategory == 'dvd':
                    if isDvdCategorySelected:
                        librarianFrameAnasayfaAddDvd.pack(pady=20,padx=40,fill='both',expand=True)
                        lastSelectedFrame = librarianFrameAnasayfaAddDvd
                        return
                    isDvdCategorySelected = True
                    librarianFrameAnasayfaAddDvd.pack(pady=20,padx=40,fill='both',expand=True)
                    lastSelectedFrame = librarianFrameAnasayfaAddDvd

                    dvdName= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Name") 
                    dvdName.pack(pady=12,padx=10) 

                    dvdDirector= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Director") 
                    dvdDirector.pack(pady=12,padx=10) 

                    dvdReleaseDate= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Release Date") 
                    dvdReleaseDate.pack(pady=12,padx=10)

                    dvdDuration= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Duration") 
                    dvdDuration.pack(pady=12,padx=10)

                    dvdStockQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Stock Quantity") 
                    dvdStockQuantity.pack(pady=12,padx=10)

                    dvdShelfQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Shelf Quantity") 
                    dvdShelfQuantity.pack(pady=12,padx=10)


                    def addDvd():
                        addStatus = None
                        sName = str(dvdName.get())
                        sAuthor = str(dvdDirector.get())
                        sPublicationDate = str(dvdReleaseDate.get())
                        sPageNum = str(dvdDuration.get())
                        sStcQuantity = str(dvdStockQuantity.get())
                        sShfQuantity = str(dvdShelfQuantity.get())

                        addStatus = librarian.Librarian().addLibraryItems('dvd',sName,sAuthor,sPublicationDate,sPageNum,sStcQuantity,sShfQuantity)
                  

                        addDvdlbl = ctk.CTkLabel(librarianFrameAnasayfaAddDvd,text=addStatus) 
                        addDvdlbl.pack(pady=12,padx=10)
                        addDvdButton.after(1000,lambda:addDvdlbl.destroy()) 

                    addDvdButton = ctk.CTkButton(librarianFrameAnasayfaAddDvd,text='Add DVD',command=addDvd) 
                    addDvdButton.pack(pady=12,padx=10)
                    
                elif selectedCategory == 'magazine':
                    if isMagazineCategorySelected:
                        librarianFrameAnasayfaAddMagazine.pack(pady=20,padx=40,fill='both',expand=True)
                        lastSelectedFrame = librarianFrameAnasayfaAddMagazine
                        return
                    isMagazineCategorySelected = True
                    librarianFrameAnasayfaAddMagazine.pack(pady=20,padx=40,fill='both',expand=True)
                    lastSelectedFrame = librarianFrameAnasayfaAddMagazine

                    magazineName= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Name") 
                    magazineName.pack(pady=12,padx=10) 

                    magazineISBN= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine ISBN") 
                    magazineISBN.pack(pady=12,padx=10) 

                    magazineIssue= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Issue") 
                    magazineIssue.pack(pady=12,padx=10) 

                    magazinePublicationDate= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Publication Date") 
                    magazinePublicationDate.pack(pady=12,padx=10)

                    magazineStockQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Stock Quantity") 
                    magazineStockQuantity.pack(pady=12,padx=10)

                    magazineShelfQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Shelf Quantity") 
                    magazineShelfQuantity.pack(pady=12,padx=10)

                    def addMagazine():
                        addStatus = None
                        sName = str(magazineName.get())
                        sAuthor = str(magazineISBN.get())
                        sPublicationDate = str(magazinePublicationDate.get())
                        sPageNum = str(magazineIssue.get())
                        sStcQuantity = str(magazineStockQuantity.get())
                        sShfQuantity = str(magazineShelfQuantity.get())

                        addStatus = librarian.Librarian().addLibraryItems('dvd',sName,sAuthor,sPublicationDate,sPageNum,sStcQuantity,sShfQuantity)
                  

                        addMagazinelbl = ctk.CTkLabel(librarianFrameAnasayfaAddMagazine,text=addStatus) 
                        addMagazinelbl.pack(pady=12,padx=10)
                        addMagazineButton.after(1000,lambda:addMagazinelbl.destroy()) 

                    addMagazineButton = ctk.CTkButton(librarianFrameAnasayfaAddMagazine,text='Add Magazine',command= addMagazine) 
                    addMagazineButton.pack(pady=12,padx=10)


            comboboxAddItem = ctk.CTkOptionMenu(librarianFrameAnasayfaAdd,values=["Books", "DVD", 'Magazine'],command=selectedState)
            comboboxAddItem.pack(padx=20, pady=10)
            comboboxAddItem.set("Choose Item")


            librarianFrameAnasayfaRemove = ctk.CTkFrame(tabviewAnasayfa.tab('Remove Item')) 
            librarianFrameAnasayfaRemove.pack(pady=20,padx=40,fill='both',expand=True)


            librarianFrameAnasayfaList = ctk.CTkFrame(tabviewAnasayfa.tab('List Items')) 
            librarianFrameAnasayfaList.pack(pady=20,padx=40,fill='both',expand=True)      
            

        def memberInterface():
            pass
        
        librarianInterface() #silinecek

        if kullanici.role == 'Librarian':
            librarianInterface()
        elif kullanici.role == 'Member':
            memberInterface()


if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()