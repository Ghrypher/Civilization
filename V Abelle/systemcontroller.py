import pygame

pygame.init()

class SystemController():
    def __init__(self):
        self.event = None
        self.mousepos = None
        self.menufont = None
        self.menufontlittle = None
        self.menufontlittle2 = None
        self.buttexture = None

    def controlInputsEvents(self,mode):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                return 'exit'
            """For All Except Credits, Instructions"""
            if mode != 'credits' or mode != 'insts':
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    return 'mouseon'
            """Only for WorkInProgress, Credits, Instructions, MapSelector"""
            if mode == 'work' or mode == 'credits' or mode == 'insts' or mode == 'map':
                if self.event.type == pygame.KEYDOWN:
                    """Escape"""
                    if self.event.key == pygame.K_ESCAPE:
                        return 'nonexit'

    def controlMouseMovement(self):
        self.mousepos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        return self.mousepos

    def createScreen(self,screensize):
        screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
        return screen

    def createClock(self):
        clock = pygame.time.Clock()
        return clock

    def screenUpdate(self,clock,fps):
        pygame.display.update()
        clock.tick(fps)

    """Function loadWindowIcon, sets the window icon and name from the resources and loads the different fonts from the game"""
    def systemLoads(self):
        windowiconload = pygame.image.load('resources/icons/windowicon.png') #Loads the window icon
        windowicon = pygame.display.set_icon(windowiconload) #Sets the window icon
        windowname = pygame.display.set_caption('T-H-E') #Sets the title of the window
        self.menufont = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',100) #Loads the default font
        self.menufontlittle = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',90) #Loads the default font but smaller than the previous one
        self.menufontlittle2 = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',73) #Loads the default font but smaller than the rest
        self.buttexture = pygame.image.load('resources/icons/menubuttontexture.jpg') #Loads the texture from the game buttons
        return windowicon,windowname,self.menufont,self.menufontlittle,self.menufontlittle2,self.buttexture

    """Function screenLogo, loads the logo and creates the collision"""
    def  screenLogo(self):
        screenlogo = pygame.image.load('resources/icons/gamelogo.png') #Loads the logo from the main menu
        screenlogocoll = screenlogo.get_rect(center = (350,360)) #Creates the collision from the previous logo
        return screenlogo,screenlogocoll

    """Function menuesLoads, loads all the menues resources, renders the texts and creates the collisions"""
    def menuesLoads(self,num):
        if num == 1: #Background image
            defback = pygame.image.load('resources/icons/defaultback.jpg') #Loads the 'background' image
            menumusic = pygame.mixer.Sound('resources/audio/menusong.mp3')
            defaultcursor = pygame.image.load('resources/icons/defaultcursor.png').convert_alpha() #Loads the default cursor image
            handcursor = pygame.image.load('resources/icons/handcursor.png').convert_alpha() #Loads the hand cursor image
            return defback,menumusic,defaultcursor,handcursor
        elif num == 2: #Work in progress
            workinprogmess = self.menufont.render('WORK IN PROGRESS',True,[0,0,0]) #Renders the message on the selected font
            underconstruc = pygame.image.load('resources/icons/underconstruction.png').convert_alpha() #Loads the 'under construction' image
            return workinprogmess,underconstruc
        elif num == 3: #Exit UI
            exitback = pygame.image.load('resources/icons/exitback.png') #Loads the exit background
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
            loadingbar = pygame.image.load('resources/icons/loadingbar.png') #Loads the loading bar image
            loadingbarcoll = loadingbar.get_rect(center = (640,552)) #Creates the collision from the previous button
            return loadingtext,loadingtextcoll,loadingbar,loadingbarcoll

    """Function gameLoads, loads all the game resources and creates the collisions"""
    def gameLoads(self,num):
        if num == 1:
            swordcursor = pygame.image.load('resources/icons/swordcursor.png').convert_alpha() #Loads the sword cursor image
            foundsprites = pygame.image.load('resources/icons/foundersprite.png') #Loads the default character image
            foundspriteposx = 515 #Establishes the position on 'x' from the default character
            foundspriteposy = 325 #Establishes the position on 'y' from the default character
            foundspritecoll = foundsprites.get_rect().move(foundspriteposx,foundspriteposy) #Creates the collision from the default character
            biometiles = {
            "X": pygame.image.load("resources/icons/map/floor/dirt.png"), #16+16+16%
            "M": pygame.image.load("resources/icons/map/floor/mountain.png"), #16+16+16+8%
            "Y": pygame.image.load("resources/icons/map/floor/water.png"),#16+16+16+16%
            " ": pygame.image.load("resources/icons/map/floor/offworld.png") #16+16+16+16+8%
            } #Dictionary that records the different sprites from the leeters that appears on the map txt
            hidden = pygame.image.load("resources/icons/map/floor/offworld.png")
            return swordcursor,foundsprites,foundspriteposx,foundspriteposy,foundspritecoll,biometiles,hidden
        if num == 2: #Music and Sounds
            gamemusic1 = pygame.mixer.Sound('resources/audio/gamemusic1.mp3')
            gamemusic2 = pygame.mixer.Sound('resources/audio/gamemusic2.mp3')
        return gamemusic1,gamemusic2