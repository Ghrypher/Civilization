import pygame

"""Function loadWindowIcon, sets the window icon and name from the resources and loads the different fonts from the game"""
def systemLoads():
    windowiconload = pygame.image.load('resources/icons/windowicon.png') #Loads the window icon
    windowicon = pygame.display.set_icon(windowiconload) #Sets the window icon
    windowname = pygame.display.set_caption('T-H-E') #Sets the title of the window
    global menufont,menufont,menufontlittle,menufontlittle2,buttexture
    menufont = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',100) #Loads the default font
    menufontlittle = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',90) #Loads the default font but smaller than the previous one
    menufontlittle2 = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',73) #Loads the default font but smaller than the rest
    buttexture = pygame.image.load('resources/icons/menubuttontexture.jpg') #Loads the texture from the game buttons
    return windowicon,windowname,menufont,menufontlittle,menufontlittle2,buttexture

"""Function screenLogo, loads the logo and creates the collision"""
def  screenLogo():
    screenlogo = pygame.image.load('resources/icons/gamelogo.png') #Loads the logo from the main menu
    screenlogocoll = screenlogo.get_rect(center = (350,360)) #Creates the collision from the previous logo
    return screenlogo,screenlogocoll

"""Function menuesLoads, loads all the menues resources, renders the texts and creates the collisions"""
def menuesLoads(num):
    if num == 1: #Background image
        defback = pygame.image.load('resources/icons/defaultback.jpg') #Loads the 'background' image
        menumusic = pygame.mixer.Sound('resources/audio/menusong.mp3')
        defaultcursor = pygame.image.load('resources/icons/defaultcursor.png').convert_alpha() #Loads the default cursor image
        handcursor = pygame.image.load('resources/icons/handcursor.png').convert_alpha() #Loads the hand cursor image
        return defback,menumusic,defaultcursor,handcursor
    elif num == 2: #Work in progress
        workinprogmess = menufont.render('WORK IN PROGRESS',True,[0,0,0]) #Renders the message on the selected font
        underconstruc = pygame.image.load('resources/icons/underconstruction.png').convert_alpha() #Loads the 'under construction' image
        return workinprogmess,underconstruc
    elif num == 3: #Exit UI
        exitback = pygame.image.load('resources/icons/exitback.png') #Loads the exit background
        exitback.set_alpha(5) #Makes the exit background a bit less opaque
        exitbackpos = (0,0) #Establishes the position from the previous background
        exittext = menufont.render('DO YOU WANT TO EXIT?',True,[255,255,255]) #Renders the message on the selected font
        exittextpos = (215,50) #Establishes the position from the previous message
        exitbtnyes = buttexture #Adds the wood button texture to this button
        exitbtnyescoll = exitbtnyes.get_rect(center = (640,275)) #Creates the collision from the previous button
        exitbtnyestext = menufont.render('YES',True,[0,0,0]) #Renders the message on the selected font
        exitbtnyestextcoll = exitbtnyestext.get_rect(midleft = (585,275)) #Creates the surface from the previous text
        exitbtnno = buttexture #Adds the wood button texture to this button
        exitbtnnocoll = exitbtnno.get_rect(center = (640,425)) #Creates the collision from the previous button
        exitbtnnotext = menufont.render('NO',True,[0,0,0]) #Renders the message on the selected font
        exitbtnnotextcoll = exitbtnnotext.get_rect(midleft = (585,425)) #Creates the collision from the previous text
        return exitback,exitbackpos,exittext,exittextpos,exitbtnyes,exitbtnyescoll,exitbtnyestext,exitbtnyestextcoll,exitbtnno,exitbtnnocoll,exitbtnnotext,exitbtnnotextcoll
    elif num == 4: #Map selector
        mapselbtn = buttexture #Adds the wood button texture to this button
        mapselbtncoll = mapselbtn.get_rect(midleft = (640,238)) #Creates the collision from the previous button
        mapselbtntext = menufontlittle.render('MAP SELECTION',True,[0,0,0]) #Renders the message on the selected font
        mapselbtntextcoll = mapselbtntext.get_rect(center = (946,230)) #Creates the collision from the previous text
        return mapselbtn,mapselbtncoll,mapselbtntext,mapselbtntextcoll
    elif num == 5: #Credits
        btncreds = buttexture #Adds the wood button texture to this button
        btncredstext = menufont.render('CREDITS',True,[0,0,0]) #Renders the message on the selected font
        btncredscoll = btncreds.get_rect(midleft = (640,368)) #Creates the collision from the previous button
        btncredstextcoll = btncredstext.get_rect(center = (952,368)) #Creates the surface from the previous text
        return btncreds,btncredstext,btncredscoll,btncredstextcoll
    elif num == 6: #Instructions
        btninstrs = buttexture #Adds the wood button texture to this button
        btninstrstext = menufont.render('INSTRUCTIONS',True,[0,0,0]) #Renders the message on the selected font
        btninstrscoll = btninstrs.get_rect(midleft = (640,498)) #Creates the collision from the previous button
        btninstrstextcoll = btninstrstext.get_rect(center = (940,498)) #Creates the surface from the previous text
        return btninstrs,btninstrstext,btninstrscoll,btninstrstextcoll
    elif num == 7: #Random mode
        btnrandom = buttexture #Adds the wood button texture to this button
        btnrandomcoll = btnrandom.get_rect(midleft = (335,275)) #Creates the collision from the previous button
        btnrandomtext = menufontlittle.render('PLAY RANDOM',True,[0,0,0]) #Renders the message on the selected font
        btnrandomtextcoll = btnrandomtext.get_rect(center = (635,275)) #Creates the surface from the previous text
        return btnrandom,btnrandomcoll,btnrandomtext,btnrandomtextcoll
    elif num == 8: #Created mode
        btncreated = buttexture #Adds the wood button texture to this button
        btncreatedcoll = btncreated.get_rect(midleft = (335,425)) #Creates the collision from the previous button
        btncreatedtext = menufontlittle2.render('PLAY PRE-CREATED',True,[0,0,0]) #Renders the message on the selected font
        btncreatedtextcoll = btncreatedtext.get_rect(center = (635,425)) #Creates the surface from the previous text
        return btncreated,btncreatedcoll,btncreatedtext,btncreatedtextcoll

"""Function gameLoads, loads all the game resources and creates the collisions"""
def gameLoads():
    swordcursor = pygame.image.load('resources/icons/swordcursor.png').convert_alpha() #Loads the sword cursor image
    foundsprites = pygame.image.load('resources/icons/foundersprite.png') #Loads the default character image
    foundspriteposx = 515 #Establishes the position on 'x' from the default character
    foundspriteposy = 325 #Establishes the position on 'y' from the default character
    foundspritecoll = foundsprites.get_rect().move(foundspriteposx,foundspriteposy) #Creates the collision from the default character
    biometiles = {
    "X": pygame.image.load("resources/icons/map/floor/dirt.png"),
    "M": pygame.image.load("resources/icons/map/floor/mountain.png"),
    "Y": pygame.image.load("resources/icons/map/floor/water.png"),
    " ": pygame.image.load("resources/icons/map/floor/offworld.png")
    } #Dictionary that records the different sprites from the leeters that appears on the map txt
    hidden = pygame.image.load("resources/icons/map/floor/offworld.png")
    gamemusic1 = pygame.mixer.Sound('resources/audio/gamemusic1.mp3')
    gamemusic2 = pygame.mixer.Sound('resources/audio/gamemusic2.mp3')
    return swordcursor,foundsprites,foundspriteposx,foundspriteposy,foundspritecoll,biometiles,gamemusic1,gamemusic2,hidden