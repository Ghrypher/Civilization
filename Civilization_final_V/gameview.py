try:
    import pygame
except ImportError:
    print("PyGame library is not installed. Please install it. CMD: pip install pygame")

pygame.init()

class GameView():
    def __init__(self):
        """Function __init__"""
        self.screensx = 1280 #Is the width from the window
        self.screensy = 704 #Is the height from the window
        self.screensize = (self.screensx,self.screensy) #Is the size from the window
        self.screen = pygame.display.set_mode(self.screensize, pygame.RESIZABLE)
        self.windowicon,self.windowname,self.menufont,self.menufontlittle,self.menufontlittle2,self.buttonwoodtexture,self.buttonselector = self.systemLoads() #Uses the systemLoads function from systemcontroller
        self.clock = pygame.time.Clock() #Creates the clock function from the game
        self.mousepos = (0,0) #Records the position from the mouse
        self.screenlogo = pygame.image.load('resources/assets/gamelogo.png') #Loads the logo from the main menu
        self.screenlogocoll = self.screenlogo.get_rect(center = (350,360)) #Creates the collision from the previous logo
        self.loadingtext,self.loadingtextcoll,self.loadingbar,self.loadingbarcoll = self.menuesLoads(9)

        self.event = ''
        self.mouseclicked = False
        self.defaultbackground = None
        self.menumusic = None
        self.defaultcursor = None
        self.handcursor = None
        self.workinprogressmessage = None
        self.underconstruction = None
        self.exitbackground = None
        self.exitbackgroundpos = None
        self.exittext = None
        self.exittextpos = None
        self.exitbuttonyes = None
        self.exitbuttonyescoll = None
        self.exitbuttonyestext = None
        self.exitbuttonyestextcoll = None
        self.exitbuttonno = None
        self.exitbuttonnocoll = None
        self.exitbuttonnotext = None
        self.exitbuttonnotextcoll = None
        self.mapselectorbutton = None
        self.mapselectorbuttoncoll = None
        self.mapselectorbuttontext = None
        self.mapselectorbuttontextcoll = None
        self.menubuttoncredits = None
        self.menubuttoncreditstext = None
        self.menubuttoncreditscoll = None
        self.menubuttoncreditstextcoll = None
        self.menubuttoninstructions = None
        self.menubuttoninstructionstext = None
        self.menubuttoninstructionscoll = None
        self.menubuttoninstructionstextcoll = None
        self.randomplaybutton = None
        self.randomplaybuttoncoll = None
        self.randomplaybuttontext = None
        self.randomplaybuttontextcoll = None
        self.createdplaybutton = None
        self.createdplaybuttoncoll = None
        self.createdplaybuttontext = None
        self.createdplaybuttontextcoll = None
        self.swordcursor = None
        self.foundersprite = None
        self.founderspriteposx = None
        self.founderspriteposy = None
        self.founderspritecoll = None
        self.biometiles = None
        self.hidden = None
        self.gamemusic1 = None
        self.gamemusic2 = None
        self.mouseoldpos = None

    def screenUpdate(self,clock,fps):
        """Function screenUpdate, updates the screen and updates the clock"""
        pygame.display.update()
        clock.tick(fps)

    def systemLoads(self):
        """Function systemLoads, loads all the vital resources from the game"""
        windowiconload = pygame.image.load('resources/assets/windowicon.png') #Loads the window icon
        windowicon = pygame.display.set_icon(windowiconload) #Sets the window icon
        windowname = pygame.display.set_caption('T-H-E') #Sets the title of the window
        self.menufont = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',100) #Loads the default font
        self.menufontlittle = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',90) #Loads the default font but smaller than the previous one
        self.menufontlittle2 = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',73) #Loads the default font but smaller than the rest
        self.buttexture = pygame.image.load('resources/assets/menubuttontexture.jpg') #Loads the texture from the game buttons
        buttselector = pygame.image.load('resources/assets/buttonselector.png')
        return windowicon,windowname,self.menufont,self.menufontlittle,self.menufontlittle2,self.buttexture,buttselector

    def menuesLoads(self,num):
        """Function menuesLoads, loads all the menues resources, renders the texts and creates the collisions"""
        if num == 1: #Background image
            defback = pygame.image.load('resources/assets/defaultback.jpg') #Loads the 'background' image
            menumusic = pygame.mixer.Sound('resources/audio/menusong.mp3')
            defaultcursor = pygame.image.load('resources/assets/defaultcursor.png').convert_alpha() #Loads the default cursor image
            handcursor = pygame.image.load('resources/assets/handcursor.png').convert_alpha() #Loads the hand cursor image
            return defback,menumusic,defaultcursor,handcursor
        elif num == 2: #Work in progress
            workinprogmess = self.menufont.render('WORK IN PROGRESS',True,[0,0,0]) #Renders the message on the selected font
            underconstruc = pygame.image.load('resources/assets/underconstruction.png').convert_alpha() #Loads the 'under construction' image
            return workinprogmess,underconstruc
        elif num == 3: #Exit UI
            exitback = pygame.image.load('resources/assets/exitback.png') #Loads the exit background
            exitback.set_alpha(5) #Makes the exit background a bit less opaque
            exitbackpos = (0,0) #Establishes the position from the previous background
            exittext = self.menufont.render('DO YOU WANT TO EXIT?',True,[255,255,255]) #Renders the message on the selected font
            exittextpos = (215,50) #Establishes the position from the previous message
            exitbtnyes = self.buttexture #Adds the wood button texture to this button
            exitbtnyescoll = exitbtnyes.get_rect(center = (640,275)) #Creates the collision from the previous button
            exitbtnyestext = self.menufont.render('YES',True,[0,0,0]) #Renders the message on the selected font
            exitbtnyestextcoll = exitbtnyestext.get_rect(midleft = (585,275)) #Creates the surface from the previous text
            exitbtnno = self.buttexture #Adds the wood button texture to this button
            exitbtnnocoll = exitbtnno.get_rect(center = (640,425)) #Creates the collision from the previous button
            exitbtnnotext = self.menufont.render('NO',True,[0,0,0]) #Renders the message on the selected font
            exitbtnnotextcoll = exitbtnnotext.get_rect(midleft = (585,425)) #Creates the collision from the previous text
            return exitback,exitbackpos,exittext,exittextpos,exitbtnyes,exitbtnyescoll,exitbtnyestext,exitbtnyestextcoll,exitbtnno,exitbtnnocoll,exitbtnnotext,exitbtnnotextcoll
        elif num == 4: #Map selector
            mapselbtn = self.buttexture #Adds the wood button texture to this button
            mapselbtncoll = mapselbtn.get_rect(midleft = (640,238)) #Creates the collision from the previous button
            mapselbtntext = self.menufontlittle.render('MAP SELECTION',True,[0,0,0]) #Renders the message on the selected font
            mapselbtntextcoll = mapselbtntext.get_rect(center = (946,230)) #Creates the collision from the previous text
            return mapselbtn,mapselbtncoll,mapselbtntext,mapselbtntextcoll
        elif num == 5: #Credits
            btncreds = self.buttexture #Adds the wood button texture to this button
            btncredstext = self.menufont.render('CREDITS',True,[0,0,0]) #Renders the message on the selected font
            btncredscoll = btncreds.get_rect(midleft = (640,368)) #Creates the collision from the previous button
            btncredstextcoll = btncredstext.get_rect(center = (952,368)) #Creates the surface from the previous text
            return btncreds,btncredstext,btncredscoll,btncredstextcoll
        elif num == 6: #Instructions
            btninstrs = self.buttexture #Adds the wood button texture to this button
            btninstrstext = self.menufont.render('INSTRUCTIONS',True,[0,0,0]) #Renders the message on the selected font
            btninstrscoll = btninstrs.get_rect(midleft = (640,498)) #Creates the collision from the previous button
            btninstrstextcoll = btninstrstext.get_rect(center = (940,498)) #Creates the surface from the previous text
            return btninstrs,btninstrstext,btninstrscoll,btninstrstextcoll
        elif num == 7: #Random mode
            btnrandom = self.buttexture #Adds the wood button texture to this button
            btnrandomcoll = btnrandom.get_rect(midleft = (335,275)) #Creates the collision from the previous button
            btnrandomtext = self.menufontlittle.render('PLAY RANDOM',True,[0,0,0]) #Renders the message on the selected font
            btnrandomtextcoll = btnrandomtext.get_rect(center = (635,275)) #Creates the surface from the previous text
            return btnrandom,btnrandomcoll,btnrandomtext,btnrandomtextcoll
        elif num == 8: #Created mode
            btncreated = self.buttexture #Adds the wood button texture to this button
            btncreatedcoll = btncreated.get_rect(midleft = (335,425)) #Creates the collision from the previous button
            btncreatedtext = self.menufontlittle2.render('PLAY PRE-CREATED',True,[0,0,0]) #Renders the message on the selected font
            btncreatedtextcoll = btncreatedtext.get_rect(center = (635,425)) #Creates the surface from the previous text
            return btncreated,btncreatedcoll,btncreatedtext,btncreatedtextcoll
        elif num == 9: #Loading
            loadingtext = self.menufont.render('LOADING...',True,[255,255,255]) #Renders the message on the selected font
            loadingtextcoll = loadingtext.get_rect(center = (640,352)) #Creates the collision from the previous text
            loadingbar = pygame.image.load('resources/assets/loadingbar.png') #Loads the loading bar image
            loadingbarcoll = loadingbar.get_rect(center = (640,552)) #Creates the collision from the previous button
            return loadingtext,loadingtextcoll,loadingbar,loadingbarcoll

    def gameLoads(self,num):
        """Function gameLoads, loads all the game resources and creates the collisions"""
        if num == 1:
            swordcursor = pygame.image.load('resources/assets/swordcursor.png').convert_alpha() #Loads the sword cursor image
            foundsprites = pygame.image.load('resources/assets/foundersprite.png') #Loads the default character image
            foundspriteposx = 515 #Establishes the position on 'x' from the default character
            foundspriteposy = 325 #Establishes the position on 'y' from the default character
            foundspritecoll = foundsprites.get_rect().move(foundspriteposx,foundspriteposy) #Creates the collision from the default character
            biometiles = {  #Active
                            "D" : pygame.image.load("resources/assets/map/floor/Dirt.png"),
                            "F" : pygame.image.load("resources/assets/map/floor/Forest.png"),
                            "W" : pygame.image.load("resources/assets/map/floor/Water.png"),
                            "M" : pygame.image.load("resources/assets/map/floor/Mountain.png"),
                            "I" : pygame.image.load("resources/assets/map/floor/Iron_Mountain.png"),
                            "G" : pygame.image.load("resources/assets/map/floor/Gold_Mountain.png"),
                            #Inactive
                            " D" : pygame.image.load("resources/assets/map/floor/Dirt_inactive.png"),
                            " F" : pygame.image.load("resources/assets/map/floor/Forest_inactive.png"),
                            " W" : pygame.image.load("resources/assets/map/floor/Water_inactive.png"),
                            " M" : pygame.image.load("resources/assets/map/floor/Mountain_inactive.png"),
                            " I" : pygame.image.load("resources/assets/map/floor/Iron_Mountain_inactive.png"),
                            " G" : pygame.image.load("resources/assets/map/floor/Gold_Mountain_inactive.png"),
                            #hidden
                            " " : pygame.image.load("resources/assets/map/floor/off_world.png"),
                            } #Dictionary that records the different sprites from the leeters that appears on the map txt
            hidden = pygame.image.load("resources/assets/map/floor/off_world.png")
            return swordcursor,foundsprites,foundspriteposx,foundspriteposy,foundspritecoll,biometiles,hidden
        if num == 2: #Music and Sounds
            gamemusic1 = pygame.mixer.Sound('resources/audio/gamemusic1.mp3')
            gamemusic2 = pygame.mixer.Sound('resources/audio/gamemusic2.mp3')
        return gamemusic1,gamemusic2

    def loadBarView(self,mode):
        """Function loadBarView, is the loop from the load bar"""
        loading = True
        loadingstep = 0
        loadingprogressvalue = 0
        while loading:
            loadingstep += 1

            """Background"""
            self.screen.fill([0,0,0])
            """Text"""
            self.screen.blit(self.loadingtext,self.loadingtextcoll)
            """Loading Bar"""
            self.screen.blit(self.loadingbar,self.loadingbarcoll)
            """Loading Bar Content Complete"""
            pygame.draw.rect(self.screen,[116,125,131],(250,542,loadingprogressvalue,20)) #97 == 8% progress

            """Loads"""
            """Menues Loads"""
            if mode == 1:
                if loadingstep == 1:
                    loadingprogressvalue += 130
                if loadingstep == 10:
                    """Menues All"""
                    self.defaultbackground,self.menumusic,self.defaultcursor,self.handcursor = self.menuesLoads(1) #Uses the menuLoads function from systemcontroller
                    loadingprogressvalue += 130
                elif loadingstep == 15:
                    """Work In Progress"""
                    self.workinprogressmessage,self.underconstruction = self.menuesLoads(2) #Uses the menuLoads function from systemcontroller
                    loadingprogressvalue += 130
                elif loadingstep == 20:
                    """Exit"""
                    self.exitbackground,self.exitbackgroundpos,self.exittext,self.exittextpos,self.exitbuttonyes,self.exitbuttonyescoll,self.exitbuttonyestext,self.exitbuttonyestextcoll,self.exitbuttonno,self.exitbuttonnocoll,self.exitbuttonnotext,self.exitbuttonnotextcoll = self.menuesLoads(3) #Uses the menuLoads function from systemcontroller
                    loadingprogressvalue += 130
                elif loadingstep == 25:
                    """Map Selector"""
                    self.mapselectorbutton,self.mapselectorbuttoncoll,self.mapselectorbuttontext,self.mapselectorbuttontextcoll= self.menuesLoads(4) #Uses the menuLoads function from systemcontroller
                    loadingprogressvalue += 130
                elif loadingstep == 30:
                    """Credits"""
                    self.menubuttoncredits,self.menubuttoncreditstext,self.menubuttoncreditscoll,self.menubuttoncreditstextcoll = self.menuesLoads(5) #Uses the menuLoads function from systemcontroller
                    loadingprogressvalue += 130
                elif loadingstep == 35:
                    """Instructions"""
                    self.menubuttoninstructions,self.menubuttoninstructionstext,self.menubuttoninstructionscoll,self.menubuttoninstructionstextcoll = self.menuesLoads(6) #Uses the menuLoads function from systemcontroller
                    loading = False
            """Game Loads"""
            if mode == 2:
                if loadingstep == 1:
                    loadingprogressvalue += 195
                if loadingstep == 10:
                    """Play Random"""
                    self.randomplaybutton,self.randomplaybuttoncoll,self.randomplaybuttontext,self.randomplaybuttontextcoll = self.menuesLoads(7) #Uses the menuLoads function from systemcontroller
                    loadingprogressvalue += 195
                elif loadingstep == 15:
                    """Play Pre-Created"""
                    self.createdplaybutton,self.createdplaybuttoncoll,self.createdplaybuttontext,self.createdplaybuttontextcoll = self.menuesLoads(8) #Uses the menuLoads function from systemcontroller
                    loadingprogressvalue += 195
                elif loadingstep == 30:
                    """Game"""
                    self.swordcursor,self.foundersprite,self.founderspriteposx,self.founderspriteposy,self.founderspritecoll,self.biometiles,self.hidden = self.gameLoads(1) #Uses the gameLoads function from systemcontroller
                    loadingprogressvalue += 195
                elif loadingstep == 35:
                    self.gamemusic1,self.gamemusic2 = self.gameLoads(2) #Uses the gameLoads function from systemcontroller
                    loading = False

            try:
                self.screenUpdate(self.clock,30)
            except:
                pass

        return self.defaultbackground,self.menumusic,self.defaultcursor,self.handcursor,self.workinprogressmessage,self.underconstruction,self.exitbackground,self.exitbackgroundpos,self.exittext,self.exittextpos,self.exitbuttonyes,self.exitbuttonyescoll,self.exitbuttonyestext,self.exitbuttonyestextcoll,self.exitbuttonno,self.exitbuttonnocoll,self.exitbuttonnotext,self.exitbuttonnotextcoll,self.mapselectorbutton,self.mapselectorbuttoncoll,self.mapselectorbuttontext,self.mapselectorbuttontextcoll,self.menubuttoncredits,self.menubuttoncreditstext,self.menubuttoncreditscoll,self.menubuttoncreditstextcoll,self.menubuttoninstructions,self.menubuttoninstructionstext,self.menubuttoninstructionscoll,self.menubuttoninstructionstextcoll,self.randomplaybutton,self.randomplaybuttoncoll,self.randomplaybuttontext,self.randomplaybuttontextcoll,self.createdplaybutton,self.createdplaybuttoncoll,self.createdplaybuttontext,self.createdplaybuttontextcoll,self.swordcursor,self.foundersprite,self.founderspriteposx,self.founderspriteposy,self.founderspritecoll,self.biometiles,self.hidden,self.gamemusic1,self.gamemusic2

    def menuFirstDraw(self):
        """Function menuFirstDraw, draws in the menu the basic draw"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Game Logo"""
        self.screen.blit(self.screenlogo,self.screenlogocoll)
        """Buttons"""
        """Play"""
        self.screen.blit(self.mapselectorbutton,self.mapselectorbuttoncoll)
        self.screen.blit(self.mapselectorbuttontext,self.mapselectorbuttontextcoll)
        """Credits"""
        self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
        self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)
        """Instructions"""
        self.screen.blit(self.menubuttoninstructions,self.menubuttoninstructionscoll)
        self.screen.blit(self.menubuttoninstructionstext,self.menubuttoninstructionstextcoll)
        self.menumusic.play(loops = -1)
        self.menumusic.set_volume(0.50)

    def menuView(self,mousepos,keyevent):
        """Function menuView, is the menu loop"""
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'exit'
        elif self.event == 'mouseon':
            self.mouseclicked = True

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Game Logo"""
                self.screen.blit(self.screenlogo,self.screenlogocoll)
                """Buttons"""
                """Play"""
                self.screen.blit(self.mapselectorbutton,self.mapselectorbuttoncoll)
                self.screen.blit(self.mapselectorbuttontext,self.mapselectorbuttontextcoll)
                """Credits"""
                self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
                self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)
                """Instructions"""
                self.screen.blit(self.menubuttoninstructions,self.menubuttoninstructionscoll)
                self.screen.blit(self.menubuttoninstructionstext,self.menubuttoninstructionstextcoll)
        except:
            pass

        """Mouses"""
        if self.mapselectorbuttoncoll.collidepoint(self.mousepos) == True or self.menubuttoncreditscoll.collidepoint(self.mousepos) == True or self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.handcursor,self.mousepos)
        else:
            self.screen.blit(self.defaultcursor,self.mousepos)

        """Control"""
        """Mouse Passes Over the Buttons"""
        """Map Select"""
        if self.mapselectorbuttoncoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.mapselectorbuttoncoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                self.menumusic.stop()
                returnedvalue = 'map'
        """Credits"""
        if self.menubuttoncreditscoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.menubuttoncreditscoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                returnedvalue = 'crets'
        """Instructions"""
        if self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.menubuttoninstructionscoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                returnedvalue = 'insts'

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue

    def workInProgressFirstDraw(self):
        """Function workInProgressFirstDraw, draws in the screen the basic work in progress menu"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))
    
    def workInProgressView(self,mousepos,keyevent):
        """Function workInProgressView, is the work in progress menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'exit'
        elif self.event == 'nonexit':
            returnedvalue = 'nonexit'

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Under Construction"""
                self.screen.blit(self.workinprogressmessage,(275,300))
                self.screen.blit(self.underconstruction,(425,75))
                self.screen.blit(self.defaultcursor,self.mousepos)
        except:
            pass

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue

    def exitUIFirstDraw(self):
        """Function exitUIFirstDraw, draws in the screen the basic exit UI menu"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.exitbackground,self.exitbackgroundpos)
        """Question"""
        self.screen.blit(self.exittext,self.exittextpos)
        """Buttons"""
        """Yes"""
        self.screen.blit(self.exitbuttonyes,self.exitbuttonyescoll)
        self.screen.blit(self.exitbuttonyestext,self.exitbuttonyestextcoll)
        """No"""
        self.screen.blit(self.exitbuttonno,self.exitbuttonnocoll)
        self.screen.blit(self.exitbuttonnotext,self.exitbuttonnotextcoll)
        oldmousepos = (0,0)

    def exitUIView(self,mousepos,keyevent):
        """Function exitUIView, is the exit UI menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'mouseon':
            self.mouseclicked = True
        elif self.event == 'mouseoff':
            self.mouseclicked = False

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Draw Calls"""
                """Background"""
                self.screen.blit(self.exitbackground,self.exitbackgroundpos)
                """Question"""
                self.screen.blit(self.exittext,self.exittextpos)
                """Buttons"""
                """Yes"""
                self.screen.blit(self.exitbuttonyes,self.exitbuttonyescoll)
                self.screen.blit(self.exitbuttonyestext,self.exitbuttonyestextcoll)
                """No"""
                self.screen.blit(self.exitbuttonno,self.exitbuttonnocoll)
                self.screen.blit(self.exitbuttonnotext,self.exitbuttonnotextcoll)
                """Mouse"""
                self.screen.blit(self.defaultcursor,self.mousepos)

                """Control"""
                """Mouse Passes Over the Buttons"""
                """Yes"""
                if self.exitbuttonyescoll.collidepoint(self.mousepos) == True:
                    self.screen.blit(self.buttonselector,self.exitbuttonyescoll)
                    self.screen.blit(self.handcursor,self.mousepos)
                    if self.mouseclicked == True:
                        self.mouseclicked = False
                        pygame.quit()
                        exit()
                """No"""
                if self.exitbuttonnocoll.collidepoint(self.mousepos) == True:
                    self.screen.blit(self.buttonselector,self.exitbuttonnocoll)
                    self.screen.blit(self.handcursor,self.mousepos)
                    if self.mouseclicked == True:
                        self.mouseclicked = False
                        returnedvalue = 'nonexit'
        except:
            pass

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

    def creditsFirstDraw(self):
        """Function creditsFirstDraw, draws in the screen the basic credits menu"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))

    def creditsView(self,mousepos,keyevent):
        """Function creditsView, is the credits menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'credits'
        elif self.event == 'nonexit':
            returnedvalue = 'nonexit'

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Under Construction"""
                self.screen.blit(self.workinprogressmessage,(275,300))
                self.screen.blit(self.underconstruction,(425,75))
                self.screen.blit(self.defaultcursor,self.mousepos)
        except:
            pass

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue

    def instructionsFirstDraw(self):
        """Function instructionsFirstDraw, draws in the screen the basic instructions menu"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))

    def instructionsView(self,mousepos,keyevent):
        """Function instructionsView, is the instructions menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'credits'
        elif self.event == 'nonexit':
            returnedvalue = 'nonexit'

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Under Construction"""
                self.screen.blit(self.workinprogressmessage,(275,300))
                self.screen.blit(self.underconstruction,(425,75))
                self.screen.blit(self.defaultcursor,self.mousepos)
        except:
            pass

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue

    def mapSelectorFirstDraw(self):
        """Function mapSelectorFirstDraw, draws in the screen the basic map selector menu"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Buttons"""
        """Play Random"""
        self.screen.blit(self.randomplaybutton,self.randomplaybuttoncoll)
        self.screen.blit(self.randomplaybuttontext,self.randomplaybuttontextcoll)
        """Play Pre-Created"""
        self.screen.blit(self.createdplaybutton,self.createdplaybuttoncoll)
        self.screen.blit(self.createdplaybuttontext,self.createdplaybuttontextcoll)

    def mapSeclectorView(self,mousepos,keyevent):
        """Function mapSeclectorView, is the map selector menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'exit'
        elif self.event == 'nonexit':
            returnedvalue = 'nonexit'
        elif self.event == 'mouseon':
            self.mouseclicked = True

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Draw Calls"""
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Buttons"""
                """Play Random"""
                self.screen.blit(self.randomplaybutton,self.randomplaybuttoncoll)
                self.screen.blit(self.randomplaybuttontext,self.randomplaybuttontextcoll)
                """Play Pre-Created"""
                self.screen.blit(self.createdplaybutton,self.createdplaybuttoncoll)
                self.screen.blit(self.createdplaybuttontext,self.createdplaybuttontextcoll)
                """Mouses"""
                if self.createdplaybuttoncoll.collidepoint(self.mousepos) == True or self.randomplaybuttoncoll.collidepoint(self.mousepos) == True:
                    self.screen.blit(self.handcursor,self.mousepos)
                else:
                    self.screen.blit(self.defaultcursor,self.mousepos)
        except:
            pass

        """Control"""
        """Mouse Passes Over the Buttons"""
        """Random Map"""
        if self.randomplaybuttoncoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.randomplaybuttoncoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                self.menumusic.stop()
                returnedvalue = 'random'
        """Pre-Created Map"""
        if self.createdplaybuttoncoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.createdplaybuttoncoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                self.menumusic.stop()
                returnedvalue = 'pre'

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue

    def gameLoopView(self,M_surf,mapRect,mousepos,cursor):
        self.screen.fill((0,0,0))

        # Dibuja el mapa en la pantalla del display
        self.screen.blit(M_surf, mapRect)
        self.screen.blit(cursor,mousepos)
        
        try:
            self.screenUpdate(self.clock,60)
        except:
            pass

    def updateSprite(self, unitSprite):
            """ """
            newSprite = pygame.image.load("resources/assets/characters/" + str(unitSprite))
            return newSprite
