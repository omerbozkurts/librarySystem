import customtkinter as ctk 
import tkinter as tk
from functools import partial

class UserInterface(ctk.CTk):

    def __init__(self):

        super().__init__()
        # Selecting GUI theme - dark, light , system (for system default) 
        
        self.state=''
        
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
        karsilamaLbl=ctk.CTkLabel(karsilama,text='Hos Geldiniz',font=('Brush Script MT',32))
        karsilamaLbl.pack(pady=0,padx=0)
        karsilama.after(1000,lambda:self.girisEkrani())
        karsilama.after(1000,lambda:karsilama.destroy())

    def girisEkrani(self):
        
        tabview = ctk.CTkTabview(self,fg_color='transparent',width=360,height=700)
        tabview.pack(pady=10,padx=10,expand=True,fill='both')
        tabview.add("Librarian") 
        tabview.add("Member")

        def girisYap():
            pass

        def kayitOl():
            librarianFrame.destroy()
            memberFrame.destroy()
            tabview.destroy()

            kayitSayfasi=ctk.CTkFrame(self) 
            kayitSayfasi.pack(pady=20,padx=40,fill='both',expand=True) 
            kayitSayfasiLbl=ctk.CTkLabel(kayitSayfasi,text="Kayıt Ol")
            kayitSayfasiLbl.pack(pady=12,padx=10)
            

            def selectedState(choice):
                self.state = choice

            combobox = ctk.CTkOptionMenu(kayitSayfasi,values=["Librarian", "Member"],command=partial(selectedState,self))
            combobox.pack(padx=20, pady=10)
            combobox.set("Choose Role")

            kullaniciAd= ctk.CTkEntry(kayitSayfasi,placeholder_text="Name") 
            kullaniciAd.pack(pady=12,padx=10)

            kullaniciSoyad= ctk.CTkEntry(kayitSayfasi,placeholder_text="Surname") 
            kullaniciSoyad.pack(pady=12,padx=10)

            kullaniciDogum= ctk.CTkEntry(kayitSayfasi,placeholder_text="Date of Birth") 
            kullaniciDogum.pack(pady=12,padx=10)

            kullaniciSifre= ctk.CTkEntry(kayitSayfasi,placeholder_text="Password",show="*") 
            kullaniciSifre.pack(pady=12,padx=10)
            

            if self.state=="Librarian":
                kutuphaneciId= ctk.CTkEntry(kayitSayfasi,placeholder_text='Librarian Id')
                kutuphaneciId.pack(pady=12,padx=10)
            elif self.state=="Member":    
                kullaniciEmail= ctk.CTkEntry(kayitSayfasi,placeholder_text='Email')
                kullaniciEmail.pack(pady=12,padx=10)

        
        librarianFrame = ctk.CTkFrame(tabview.tab('Librarian')) 
        librarianFrame.pack(pady=20,padx=40,fill='both',expand=True)    

        label = ctk.CTkLabel(librarianFrame,text='Login Page') 
        label.pack(pady=12,padx=10) 


        kullaniciAdi= ctk.CTkEntry(librarianFrame,placeholder_text="Employee Id") 
        kullaniciAdi.pack(pady=12,padx=10) 

        parola= ctk.CTkEntry(librarianFrame,placeholder_text="Password",show="*") 
        parola.pack(pady=12,padx=10) 


        girisYapB = ctk.CTkButton(librarianFrame,text='Login',command=girisYap) 
        girisYapB.pack(pady=12,padx=10)

        kayitOlB = ctk.CTkButton(librarianFrame,text='Sign in',command=kayitOl)
        kayitOlB.pack(pady=12,padx=10)

        memberFrame = ctk.CTkFrame(tabview.tab('Member')) 
        memberFrame.pack(pady=20,padx=40,fill='both',expand=True)    

        label = ctk.CTkLabel(memberFrame,text='Login Page') 
        label.pack(pady=12,padx=10) 


        kullaniciAdi= ctk.CTkEntry(memberFrame,placeholder_text="Email") 
        kullaniciAdi.pack(pady=12,padx=10) 

        parola= ctk.CTkEntry(memberFrame,placeholder_text="Password",show="*") 
        parola.pack(pady=12,padx=10) 


        girisYapB = ctk.CTkButton(memberFrame,text='Login',command=girisYap) 
        girisYapB.pack(pady=12,padx=10)

        kayitOlB = ctk.CTkButton(memberFrame,text='Sign in',command=kayitOl)
        kayitOlB.pack(pady=12,padx=10)


if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()