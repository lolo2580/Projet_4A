# -*-coding:Latin-1 -*-
from tkinter import *                                           #1
                                                                #2
class MenuBar(Frame):                                           #3
    """Barre de menus déroulants"""                             #4
    def __init__(self, boss =None):                             #5
        Frame.__init__(self, borderwidth =1)                    #6
                                                                #7
        ##### Menu <Type> #####                              #8
        fileMenuType = Menubutton(self, text ='Type', relief=RAISED)            #9
        fileMenuType.pack(side =LEFT)

        ##### Menu <Durée> #####                              #8
        fileMenuDuree = Menubutton(self, text ='Durée', relief=RAISED)            #9
        fileMenuDuree.pack(side =RIGHT) 

        # Partie "déroulante" :                                 #11
        me1 = Menu(fileMenuType)                                    #12
        me1.add_command(label ='Effacer', underline =0,         #13
                        command = boss.effacer)                 #14
        me1.add_command(label ='Terminer', underline =0,        #15
                        command = boss.quit)                    #16
        # Intégration du menu :                                 #17
        fileMenuType.configure(menu = me1)                          #18
                                                                #19
class Application(Frame):                                       #20
    """Application principale"""                                #21
    def __init__(self, boss =None):                             #22
        Frame.__init__(self)                                    #23
        self.master.title('Fenêtre avec menus')                 #24
        mBar = MenuBar(self)                                    #25
        mBar.pack()                                             #26
        self.can = Canvas(self, bg='light grey', height=50,    #27
                          width=250, borderwidth =2)            #28
        self.can.pack()                                         #29
        self.pack()                                             #30
                                                                #31
    def effacer(self):                                          #32
        self.can.delete(ALL)
        print("lol")
                                                                #34
if __name__ == '__main__':                                      #35
    app = Application()                                         #36
    app.mainloop()
    
