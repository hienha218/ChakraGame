from buttonclass import *
from graphics import *
import winsound

class char:
    def __init__(self, win, x1, y1):
        """Draw the main character (the player) in the game window. win is the name of the game window, (x1,y1) is the point where the main character will be drawn."""
        self.x = x1
        self.y = y1
        self.win = win
        self.char = Image(Point(x1, y1), "character\pr_fred.gif")
        self.char.draw(win)
        self.walkCount = 0

    def getBack(self):
        """Return the x value of the back of the main character."""
        self.center = self.char.getAnchor()
        self.face = self.center.getX() - 20
        return self.face

    def getFront(self):
        """Return the x value of the front of the main character."""
        self.center = self.char.getAnchor()
        self.back = self.center.getX() + 20
        return self.back

    def standBy(self):
        """Make the character stand still."""
        self.char.move(0, 0)

    def moveChar(self, key, vel):
        """the character move to the left when "a" is pressed,
            move to the right when "d" is pressed
            vel is the velocity of the main character.
            Also make sure that the character cannot walk off-screen."""
        self.key = key
        if self.key == "a" and self.x > vel:
            self.char.move(-1 * vel, 0)
            self.x -= vel
        elif self.key == "d" and self.x < 800 - 50 - vel:
            self.char.move(vel, 0)
            self.x += vel

    def choose(self, key):
        """return True if the player press "c" """
        self.key = key
        if key == "c":
            return True
        else:
            return False

    def undrawChar(self):
        """undraw the main character"""
        self.char.undraw()


class game:
    def __init__(self, win, char):
        """The game contains a main character"""
        self.win = win
        self.char = char

    def addNPC(self, img, xpos, ypos):
        """add a NPC at (xpos,ypos)"""
        self.npc = Image(Point(xpos, ypos), img)
        self.npc.draw(self.win)

    def delNPC(self):
        """delete a NPC"""
        self.npc.undraw()

    def startConvo(self, key):
        """return True when player pushes "c" and the distance from the front of the NPC to the front of the player is less than 80."""
        self.npcenter = self.npc.getAnchor()
        self.npcface = self.npcenter.getX() - 25
        self.npcback = self.npcenter.getX() + 25
        if self.npcface - 80 <= self.char.getBack():
            return self.char.choose(key)
        elif self.npcback + 80 <= self.char.getFront():
            return self.char.choose(key)

    def dialog(self, sentence):
        """draw a dialogue box with the sentence in the center."""
        self.diaBox = Rectangle(Point(0, 400), Point(800, 500))
        self.diaBox.setFill("lightgray")
        self.diaBox.draw(self.win)
        self.sentence = Text(Point(400, 410), sentence)
        self.sentence.draw(self.win)

    def changeDia(self, sentence):
        """replace the previous sentence to a new one without having to draw multiple dialogue boxes."""
        self.sentence.undraw()
        self.sentence = Text(Point(400, 410), sentence)
        self.sentence.draw(self.win)

    def stopDia(self):
        """stop the conversation by undraw both the sentence and the box."""
        self.sentence.undraw()
        self.diaBox.undraw()

    def selection(self, clist, sen1, sen2, category):
        """draw 2 choices on the screen.
        If the player choose sen1, the category will +1 frequency in clist.
        If they pick sen2, the game will continue without adding."""
        opt1 = Button(self.win, Point(400, 150), 320, 35, sen1)
        opt2 = Button(self.win, Point(400, 260), 320, 35, sen2)
        pt = self.win.getMouse()
        if opt1.clicked(pt):
            clist[category] = clist.get(category, 0) + 1
            opt1.undraw()
            opt2.undraw()
        elif opt2.clicked(pt):
            opt1.undraw()
            opt2.undraw()
        else:
            pt = self.win.getMouse()

    def quitGame(self):
        """quit game by undrawing the main character."""
        self.char.undrawChar()


def byFreq(pair):
    # return the second half of the item in the dictionary.
    return pair[1]


def main():
    win = GraphWin("Your Chakra", 800, 500)

    # intro screen
    intBg = Image(Point(400, 250), "graphics\p_bgintro.gif")
    intBg.draw(win)
    startBtn = Button(win, Point(400, 345), 90, 45, "Start game")
    run = True
    logo = Image(Point(400, 158), "graphics\ptxt_TheChakraQuiz.gif")
    logo.draw(win)
    winsound.PlaySound("Into-The-Sunset.wav", winsound.SND_ASYNC)

    # move to the next screen when start button is clicked
    while run:
        pt = win.getMouse()
        if startBtn.clicked(pt):
            winsound.PlaySound(None, winsound.SND_ASYNC)
            break

    startBtn.undraw()
    logo.undraw()

    # Name the main character screen
    txtBox = Rectangle(Point(300, 180), Point(500, 290))
    txtBox.setFill("light grey")
    txtBox.draw(win)
    txtName = Image(Point(400, 180), "graphics\p_Name.gif")
    txtName.draw(win)
    txt = Text(Point(400, 220), "What is your name?")
    txt.draw(win)
    userID = Entry(Point(400, 250), 15)
    userID.setText("Papyrus123")
    userID.draw(win)
    contBtn = Button(win, Point(400, 345), 90, 45, "Continue")
    # move to the next screen as soon as the continue button is clicked
    while run:
        pt = win.getMouse()
        if contBtn.clicked(pt):
            break

    userName = userID.getText()
    txt.undraw()
    userID.undraw()
    txtBox.undraw()
    txtName.undraw()
    contBtn.undraw()

    # Instruction screen
    insBox = Rectangle(Point(50, 50), Point(750, 450))
    insBox.setFill("light grey")
    insBox.draw(win)
    insLogo = Image(Point(400, 50), "graphics\p_Instructions.gif")
    insLogo.draw(win)
    rdirections = Text(Point(340, 110), "Move right:           D")
    rdirections.draw(win)
    ldirections = Text(Point(340, 170), "Move left:            A")
    ldirections.draw(win)
    intKey = Text(Point(340, 230), "Talk to NPC:              C")
    intKey.draw(win)
    intReminder = Text(Point(390, 250), "* You can only talk to NPC when you get close to them.")
    intReminder.setSize(9)
    intReminder.draw(win)
    intKey = Text(Point(340, 300), "Continue dialogue:               C")
    intKey.draw(win)
    intAns = Text(Point(340, 350), "Choose a reply:              Left mouse click")
    intAns.draw(win)
    textmsg = Text(Point(400, 430), "Click mouse to begin")
    textmsg.setStyle("bold")
    textmsg.draw(win)
    win.getMouse()


    contBtn.undraw()

    # first scene
    bg1 = Image(Point(400, 200), "graphics\p_village01.gif")
    bg1.draw(win)
    exitBtn = Button(win, Point(770, 35), 40, 20, "Quit")
    main_char = char(win, 30, 446)
    gme = game(win, main_char)
    gme.addNPC("character\p_mred.gif", 560, 400)
    # read logs from the text file
    diaTxt = open("testdialog.txt", "r", encoding="utf8").read()
    logs = diaTxt.split("\n")
    counts = {}  # make a dictionary counting the frequency of each category

    while run:
        pt = win.checkMouse()
        # if clicked the exit button, run will be False => skip every scene, turn off sounds, and close window immediately
        if exitBtn.clicked(pt):
            run = False

        # run still True
        elif not exitBtn.clicked(pt):
            key = win.getKey()
            main_char.moveChar(key, 15)
            # start the conversation when main character is near the NPC and the player pressed "c"
            if key == "c" and gme.startConvo(key) == True:
                main_char.standBy()
                exitBtn.deactivate()
                for dialog in logs[:11]:
                    gme.dialog(dialog)
                    win.getKey()
                    gme.stopDia()
                gme.dialog("You like having schedule, yes or no?")
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("Interesting.")
                win.getKey()
                gme.changeDia("Alright, next!")
                win.getKey()
                gme.changeDia("Do you want to travel to places you've never been in before?")
                win.getKey()
                gme.selection(counts, "No", "Yes", "Root")
                gme.changeDia("Oh, really?")
                win.getKey()
                gme.changeDia("Me too.")
                win.getKey()
                gme.changeDia("It's so hard to find someone like you in this town.")
                win.getKey()
                gme.changeDia("Do you think you are ambitious?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("When you are out shopping, do you always demand the things you buy to be high-quality?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("Do you have a consistent routine?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("Do you workout a lot?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("Now, I know everyone loves food...")
                win.getKey()
                gme.changeDia("But do you enjoy food more than the average person?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("Do you get obsessed with things easily?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("In classes or in daily life, do you usually compare yourself to others?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("Do you consider yourself a workaholic?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("You are very competitive and loyal, yes or no?")
                win.getKey()
                gme.selection(counts, "Yes", "No", "Root")
                gme.changeDia("Great.")
                win.getKey()
                gme.changeDia("I got all your infos I need now.")
                win.getKey()
                gme.changeDia("I will bring this home and make a conclusion.")
                win.getKey()
                gme.changeDia("I will send you an email later, okay?")
                win.getKey()
                gme.changeDia("Bye, for now.")
                win.getKey()
                gme.delNPC()
                gme.stopDia()
                break
    if not run:
        win.close()

    # scene 2
    if run:
        key = win.getKey()
        gme.quitGame()
        bg2 = Image(Point(400, 250), "graphics\p_groundlightresized(1).gif")
        bg2.draw(win)
        exitBtn = Button(win, Point(770, 35), 40, 20, "Quit")
        main_char = char(win, 30, 370)
        gme = game(win, main_char)
        gme.addNPC("character\p_forange.gif", 450, 370)

        while run:
            pt = win.checkMouse()
            if exitBtn.clicked(pt):
                run = False
            elif not exitBtn.clicked(pt):
                key = win.getKey()
                main_char.moveChar(key, 15)
                if key == "c" and gme.startConvo(key) == True:
                    main_char.standBy()
                    exitBtn.deactivate()
                    gme.dialog("Hiiii ~ My name is Lorelai.")
                    win.getKey()
                    gme.changeDia("Weird name, I know, but I like it!")
                    win.getKey()
                    gme.changeDia("Hey, you know what?")
                    win.getKey()
                    gme.changeDia("No?")
                    win.getKey()
                    gme.changeDia("I feel like we can be friends!")
                    win.getKey()
                    gme.changeDia("Let's get to know each other first.")
                    win.getKey()
                    gme.changeDia(
                        "Have anyone told you that you looks really flirty even when you are not trying to be?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Sacral")
                    gme.changeDia("That was a weird question to ask a new friend...")
                    win.getKey()
                    gme.changeDia("Alright, next!")
                    win.getKey()
                    gme.changeDia("Do you feel like you fall for someone easily?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Sacral")
                    gme.changeDia("Oh really?")
                    win.getKey()
                    gme.changeDia("Hey, I am going to attend a party tonight.")
                    win.getKey()
                    gme.changeDia("Do you want to go with me?")
                    win.getKey()
                    gme.selection(counts, "Of course I will", "No", "Sacral")
                    gme.changeDia("Are you willing to do anything to get what you want?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Sacral")
                    gme.changeDia("Do you often fantasize about love?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Sacral")
                    gme.changeDia("Can you be codependent in a relationship?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Sacral")
                    gme.changeDia("Are you a free spirit?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Sacral")
                    gme.changeDia("Are your actions mostly emotional-driven?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Sacral")
                    gme.changeDia("Do you change your mind a lot?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Sacral")
                    gme.changeDia("I know this is a bit personal...")
                    win.getKey()
                    gme.changeDia("Is sex one of your favorite pastimes?")
                    win.getKey()
                    gme.selection(counts, "Yes...", "No...", "Sacral")
                    gme.changeDia("Great.")
                    win.getKey()
                    gme.changeDia("With this information...")
                    win.getKey()
                    gme.changeDia("I can conclude that...")
                    win.getKey()
                    gme.changeDia("YOU")
                    win.getKey()
                    gme.changeDia("ARE")
                    win.getKey()
                    gme.changeDia("MY")
                    win.getKey()
                    gme.changeDia("BESTFRIEND !!!!!")
                    win.getKey()
                    gme.changeDia("I really like your answers.")
                    win.getKey()
                    gme.changeDia("I have to go shopping for tonight's party now...")
                    win.getKey()
                    gme.changeDia("See yaaaa ~ New bestfriend.")
                    win.getKey()
                    gme.delNPC()
                    gme.stopDia()
                    break

    # scene 3
    if run:
        key = win.getKey()
        gme.quitGame()
        bg2 = Image(Point(400, 250), "graphics\p_groundlightresized(2).gif")
        bg2.draw(win)
        exitBtn = Button(win, Point(770, 35), 40, 20, "Quit")
        main_char = char(win, 30, 370)
        gme = game(win, main_char)
        gme.addNPC("character\p_fgreenblue.gif", 350, 370)
        while run:
            pt = win.checkMouse()
            if exitBtn.clicked(pt):
                run = False
            elif not exitBtn.clicked(pt):
                key = win.getKey()
                main_char.moveChar(key, 15)
                if key == "c" and gme.startConvo(key) == True:
                    exitBtn.deactivate()
                    main_char.standBy()
                    gme.dialog("!")
                    win.getKey()
                    gme.dialog("Oh, Hi.")
                    win.getKey()
                    gme.dialog("What is your name?")
                    win.getKey()
                    gme.dialog(str(userName) + " ?")
                    win.getKey()
                    gme.dialog("That's a beautiful name.")
                    win.getKey()
                    gme.dialog("My name is Tina.")
                    win.getKey()
                    gme.changeDia("Nice to meet you.")
                    win.getKey()
                    gme.changeDia("I just moved here.")
                    win.getKey()
                    gme.changeDia("Oh, you too?")
                    win.getKey()
                    gme.changeDia("I'm so glad to see someone like me!")
                    win.getKey()
                    gme.changeDia("Hey, has anyone told you that you looks really young or child-like?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Solar Plexus")
                    gme.changeDia("Just what I thought.")
                    win.getKey()
                    gme.changeDia("How do you usually cheer people up?")
                    win.getKey()
                    gme.selection(counts, "Making jokes", "Trying to empathize", "Solar Plexus")
                    gme.changeDia("Oh really?")
                    win.getKey()
                    gme.changeDia("Are you an optimist or an pessimist?")
                    win.getKey()
                    gme.selection(counts, "Optimist", "Pessimist", "Solar Plexus")
                    gme.changeDia("Are you easy to get along with?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Solar Plexus")
                    gme.changeDia("Do you enjoy drawing or any other art forms?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Solar Plexus")
                    gme.changeDia("Do you like travelling?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Solar Plexus")
                    gme.changeDia("Do you like to read books or to play video games?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Solar Plexus")
                    gme.changeDia("Do you know what you want to do in the future?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Solar Plexus")
                    gme.changeDia("Can you make decisions in seconds?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Solar Plexus")
                    gme.changeDia("You are a bit non-confrontational, aren't you?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Solar Plexus")
                    gme.changeDia("It was nice talking to you.")
                    win.getKey()
                    gme.changeDia("My mom is calling me.")
                    win.getKey()
                    gme.changeDia("I have to go now.")
                    win.getKey()
                    gme.changeDia("See you.")
                    win.getKey()
                    gme.delNPC()
                    gme.stopDia()
                    break

    # scene 4
    if run:
        key = win.getKey()
        gme.quitGame()
        bg2 = Image(Point(400, 250), "graphics\p_grounddark1cropped (1).gif")
        bg2.draw(win)
        exitBtn = Button(win, Point(770, 35), 40, 20, "Quit")
        main_char = char(win, 30, 384)
        gme = game(win, main_char)
        gme.addNPC("character\p_flblue.gif", 700, 370)
        while run:
            pt = win.checkMouse()
            if exitBtn.clicked(pt):
                run = False
            elif not exitBtn.clicked(pt):
                key = win.getKey()
                main_char.moveChar(key, 15)
                if key == "c" and gme.startConvo(key) == True:
                    exitBtn.deactivate()
                    main_char.standBy()
                    gme.dialog("Oh, look who's here")
                    win.getKey()
                    gme.changeDia("A new neighbor.")
                    win.getKey()
                    gme.changeDia("Just so you know...")
                    win.getKey()
                    gme.changeDia("I HATE noisy neighbor")
                    win.getKey()
                    gme.changeDia("So please don't make too much noise...")
                    win.getKey()
                    gme.changeDia("especially AT NIGHT.")
                    win.getKey()
                    gme.changeDia("Is that clear?")
                    win.getKey()
                    gme.selection(counts, "Yes, I understand.", "No, I can do whatever I want in my house.", "Heart")
                    gme.changeDia("...")
                    win.getKey()
                    gme.changeDia("Are you a sensitive person?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Heart")
                    gme.changeDia("Oh really?")
                    win.getKey()
                    gme.changeDia("Can you sense others' emotions without them saying anything?")
                    win.getKey()
                    gme.selection(counts, "Yes", "Of course not", "Heart")
                    gme.changeDia("Do you spend time on dressing up and decorating your house?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Heart")
                    gme.changeDia("Do you love animals?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Heart")
                    gme.changeDia("Do you feel like you have a hard time saying no to others?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Heart")
                    gme.changeDia("Do you yearn for a committed relationship?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Heart")
                    gme.changeDia("Let's be honest, do you think most people around you are toxic or mean?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Heart")
                    gme.changeDia("Do you enjoy going out and being in nature?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Heart")
                    gme.changeDia("Do you feel emotions more deeply than others?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Heart")
                    gme.changeDia("Hmm...")
                    win.getKey()
                    gme.changeDia("You are actually not that bad")
                    win.getKey()
                    gme.changeDia("Believe me, I've met people worse than you")
                    win.getKey()
                    gme.changeDia("I will see you later, new neighbor.")
                    win.getKey()
                    gme.changeDia("And DON'T BE NOISY TONIGHT.")
                    win.getKey()
                    gme.delNPC()
                    gme.stopDia()
                    break

    # scene 5
    if run:
        key = win.getKey()
        gme.quitGame()
        bg2 = Image(Point(400, 250), "graphics\p_grounddark1cropped(2).gif")
        bg2.draw(win)
        exitBtn = Button(win, Point(770, 35), 40, 20, "Quit")
        main_char = char(win, 30, 380)
        gme = game(win, main_char)
        gme.addNPC("character\p_fpink.gif", 640, 380)
        while run:
            pt = win.checkMouse()
            if exitBtn.clicked(pt):
                run = False
            elif not exitBtn.clicked(pt):
                key = win.getKey()
                main_char.moveChar(key, 15)
                if key == "c" and gme.startConvo(key) == True:
                    exitBtn.deactivate()
                    main_char.standBy()
                    gme.dialog("Do re mi fa sol la ti doooo~~")
                    win.getKey()
                    gme.changeDia("Oh!")
                    win.getKey()
                    gme.changeDia("...")
                    win.getKey()
                    gme.changeDia("H-Hi...")
                    win.getKey()
                    gme.changeDia("You heard me sing, right?")
                    win.getKey()
                    gme.changeDia("I'm sorry if my singing was too bad...")
                    win.getKey()
                    gme.changeDia("I'm trying to become a singer!")
                    win.getKey()
                    gme.changeDia("Say, do you usually walking on the street and randomly humming or singing a song?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Throat")
                    gme.changeDia("Awww")
                    win.getKey()
                    gme.changeDia("Do you think that you are good at making a first impression?")
                    win.getKey()
                    gme.selection(counts, "I think so", "Not at all", "Throat")
                    gme.changeDia("Hm...")
                    win.getKey()
                    gme.changeDia("Do you relate to the lyrics most in songs?")
                    win.getKey()
                    gme.selection(counts, "Yes", "Not really", "Throat")
                    gme.changeDia("Do you enjoy creative writing?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Throat")
                    gme.changeDia("Are you an opinionated person?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Throat")
                    gme.changeDia("Are you striving to be a singer or some kind of a public figure?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Throat")
                    gme.changeDia("Do you need a lot of freedom in a relationship?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Throat")
                    gme.changeDia("Do you dislike clingy people?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Throat")
                    gme.changeDia("Do you secretly (or not so secretly) like being the center of attention?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Throat")
                    gme.changeDia("Can you talk for hours about your subject of interest?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Throat")
                    gme.changeDia("You actually have some potentials...")
                    win.getKey()
                    gme.changeDia("Oh!")
                    win.getKey()
                    gme.changeDia("Don't mind me, I'm just talking to myself ^ ^")
                    win.getKey()
                    gme.changeDia("It's nice to talk to you.")
                    win.getKey()
                    gme.changeDia("I have a concert I have to attend now.")
                    win.getKey()
                    gme.changeDia("Oh, by the way, my name is Ophelia")
                    win.getKey()
                    gme.changeDia("Nice to meet you, " + str(userName))
                    win.getKey()
                    gme.changeDia("See you later.")
                    win.getKey()
                    gme.delNPC()
                    gme.stopDia()
                    break

    # scene 6
    if run:
        key = win.getKey()
        gme.quitGame()
        bg2 = Image(Point(400, 250), "graphics\p_bg1.gif")
        bg2.draw(win)
        exitBtn = Button(win, Point(770, 35), 40, 20, "Quit")
        main_char = char(win, 30, 320)
        gme = game(win, main_char)
        gme.addNPC("character\p_mgreen.gif", 390, 320)
        while run:
            pt = win.checkMouse()
            if exitBtn.clicked(pt):
                run = False
            elif not exitBtn.clicked(pt):
                key = win.getKey()
                main_char.moveChar(key, 15)
                if key == "c" and gme.startConvo(key) == True:
                    exitBtn.deactivate()
                    main_char.standBy()
                    exitBtn.deactivate()
                    gme.dialog("Hi, I am Sean.")
                    win.getKey()
                    gme.changeDia("Nice to meet you.")
                    win.getKey()
                    gme.changeDia("Do you have some time?")
                    win.getKey()
                    gme.changeDia("Yeah?")
                    win.getKey()
                    gme.changeDia("Great! I have a few questions for you.")
                    win.getKey()
                    gme.changeDia("Are you rebellious by nature?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Just what I thought.")
                    win.getKey()
                    gme.changeDia("Do you conform to the norm or march to the beat of your own drum?")
                    win.getKey()
                    gme.selection(counts, "My own drum, of course", "I try to be as normal as I could", "Third Eye")
                    gme.changeDia("Oh really?")
                    win.getKey()
                    gme.changeDia("Are you politically and socially driven?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Are you introverted?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Are you interested in magic, occult or Tarot?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Do you feel like you dislike school but still enjoy learning?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Do you have psychic experiences?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Do you constantly have existential thoughts?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Do you find it hard to fit in or relate to your peers?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Are you drawn to conspiracy theories?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Third Eye")
                    gme.changeDia("Thank you for your cooperation.")
                    win.getKey()
                    gme.changeDia("That was a survey to see how common do people believe in supernatural stuffs.")
                    win.getKey()
                    gme.changeDia("Ah! I need to go now.")
                    win.getKey()
                    gme.changeDia("Again, thank you so much.")
                    win.getKey()
                    gme.changeDia("Bye bye.")
                    win.getKey()
                    gme.delNPC()
                    gme.stopDia()
                    break

    # scene 7
    if run:
        key = win.getKey()
        gme.quitGame()
        bg2 = Image(Point(400, 200), "graphics\p_village02.gif")
        bg2.draw(win)
        exitBtn = Button(win, Point(770, 35), 40, 20, "Quit")
        main_char = char(win, 30, 440)
        gme = game(win, main_char)
        gme.addNPC("character\p_fyellow.gif", 540, 420)
        while run:
            pt = win.checkMouse()
            if exitBtn.clicked(pt):
                run = False
            elif not exitBtn.clicked(pt):
                key = win.getKey()
                main_char.moveChar(key, 15)
                if key == "c" and gme.startConvo(key) == True:
                    exitBtn.deactivate()
                    main_char.standBy()
                    gme.dialog("Hello!")
                    win.getKey()
                    gme.changeDia("Are you, by any chance, " + str(userName) + "?")
                    win.getKey()
                    gme.changeDia("I am your new roommate.")
                    win.getKey()
                    gme.changeDia("Haha, yeah, we had only talked briefly through Rmail.")
                    win.getKey()
                    gme.changeDia("I usually have a list of questions for new roommate")
                    win.getKey()
                    gme.changeDia("so you also have to do it!")
                    win.getKey()
                    gme.changeDia(
                        "First question: Usually, you look up things because you want to, not because you have to, true or false?")
                    win.getKey()
                    gme.selection(counts, "True", "False", "Crown")
                    gme.changeDia("Huh.")
                    win.getKey()
                    gme.changeDia("Do you feel you are more intelligent than most people?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Crown")
                    win.getKey()
                    gme.changeDia("How often do people come to you for advice?")
                    win.getKey()
                    gme.selection(counts, "Frequently", "Once in a while", "Crown")
                    gme.changeDia("Has anyone told you that you are more mature than your age?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Crown")
                    gme.changeDia("Do you feel that you are older than your age?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Crown")
                    gme.changeDia("Was school easy and boring for you?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Crown")
                    gme.changeDia("Have you ever had paranormal experiences?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Crown")
                    gme.changeDia("Are you easy to be aloof and detach from your feelings?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Crown")
                    gme.changeDia("Is it hard for you to open up to others on an authentic level?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Crown")
                    gme.changeDia("Can you learn something quickly?")
                    win.getKey()
                    gme.selection(counts, "Yes", "No", "Crown")
                    gme.changeDia("Okay...")
                    win.getKey()
                    gme.changeDia("So...")
                    win.getKey()
                    gme.changeDia("You are definitely not a bad roommate...")
                    win.getKey()
                    gme.changeDia("But also not that good...")
                    win.getKey()
                    gme.changeDia("I still think we can live together peacefully though")
                    win.getKey()
                    gme.changeDia("It's getting cold outside.")
                    win.getKey()
                    gme.changeDia("Let's get inside.")
                    win.getKey()
                    gme.delNPC()
                    gme.stopDia()
                    break

    # Conclusion screen
    exitBtn.activate()
    while run:
        pt = win.checkMouse()
        if exitBtn.clicked(pt):
            run = False
        elif not exitBtn.clicked(pt):
            win.getKey()
            break

    if not run:
        win.close()
    else:
        gme.quitGame()

        bg = Image(Point(400, 250), "graphics\p_introbyaconfuseddragon.gif")
        bg.draw(win)
        bg2 = Rectangle(Point(50, 50), Point(750, 450))
        bg2.setFill("lightgray")
        bg2.draw(win)
        resultLogo = Image(Point(400, 50), "graphics\p_results.gif")
        resultLogo.draw(win)
        exitBtn = Button(win, Point(770, 35), 40, 20, "Quit")

        # transparent root chakra logo
        rootLogo = Image(Point(100, 100), "graphics\p_rootchakra.gif")
        [rWidth, rHeight] = rootLogo.getWidth(), rootLogo.getHeight()
        rootBg = Image(Point(100, 100), rWidth, rHeight)
        for x in range(rWidth):
            for y in range(rHeight):
                [r1, g1, b1] = rootLogo.getPixel(x, y)
                if r1 > 0 and g1 < 200 and b1 < 200:
                    rootBg.setPixel(x, y, color_rgb(r1, g1, b1))
        rootBg.draw(win)
        rootName = Text(Point(178, 100), "Root Chakra:")
        rootName.setStyle("bold")
        rootName.draw(win)
        rootRsl = Text(Point(350, 100), "You got " + str(counts["Root"]) + " out of 10 credits.")
        rootRsl.draw(win)

        # transparent sacral chakra logo
        sacralLogo = Image(Point(100, 150), "graphics\p_sacralchakra.gif")
        [sWidth, sHeight] = sacralLogo.getWidth(), sacralLogo.getHeight()
        sacralBg = Image(Point(100, 150), sWidth, sHeight)
        for x in range(sWidth):
            for y in range(sHeight):
                [r2, g2, b2] = sacralLogo.getPixel(x, y)
                if r2 > 0 and g2 < 230 and b2 < 218:
                    sacralBg.setPixel(x, y, color_rgb(r2, g2, b2))
        sacralBg.draw(win)
        sacralName = Text(Point(183, 150), "Sacral Chakra:")
        sacralName.setStyle("bold")
        sacralName.draw(win)
        sacralRsl = Text(Point(350, 150), "You got " + str(counts["Sacral"]) + " out of 10 credits.")
        sacralRsl.draw(win)

        # transparent heart chakra logo
        heartLogo = Image(Point(100, 200), "graphics\p_heartchakra.gif")
        [hWidth, hHeight] = heartLogo.getWidth(), heartLogo.getHeight()
        heartBg = Image(Point(100, 200), hWidth, hHeight)
        for x in range(hWidth):
            for y in range(hHeight):
                [r3, g3, b3] = heartLogo.getPixel(x, y)
                if r3 < 232 and g3 > 0 and b3 < 249:
                    heartBg.setPixel(x, y, color_rgb(r3, g3, b3))
        heartBg.draw(win)
        heartName = Text(Point(178, 200), "Heart Chakra:")
        heartName.setStyle("bold")
        heartName.draw(win)
        heartRsl = Text(Point(348, 200), "You got " + str(counts["Heart"]) + " out of 10 credits.")
        heartRsl.draw(win)

        # transparent solar-p chakra logo
        solarpLogo = Image(Point(100, 250), "graphics\p_solarpchakra.gif")
        [spWidth, spHeight] = solarpLogo.getWidth(), solarpLogo.getHeight()
        spBg = Image(Point(100, 250), spWidth, spHeight)
        for x in range(spWidth):
            for y in range(spHeight):
                [r4, g4, b4] = solarpLogo.getPixel(x, y)
                if r4 < 252 and g4 < 238 and b4 < 238:
                    spBg.setPixel(x, y, color_rgb(r4, g4, b4))
        spBg.draw(win)
        spName = Text(Point(210, 250), "Solar Plexus Chakra:")
        spName.setStyle("bold")
        spName.draw(win)
        spRsl = Text(Point(393, 250), "You got " + str(counts["Solar Plexus"]) + " out of 10 credits.")
        spRsl.draw(win)

        # transparent throat chakra logo
        throatLogo = Image(Point(100, 300), "graphics\p_throatchakra.gif")
        [tWidth, tHeight] = throatLogo.getWidth(), throatLogo.getHeight()
        throatBg = Image(Point(100, 300), tWidth, tHeight)
        for x in range(tWidth):
            for y in range(tHeight):
                [r5, g5, b5] = throatLogo.getPixel(x, y)
                if r5 < 238 and g5 < 236 and b5 > 0:
                    throatBg.setPixel(x, y, color_rgb(r5, g5, b5))
        throatBg.draw(win)
        throatName = Text(Point(185, 300), "Throat Chakra:")
        throatName.setStyle("bold")
        throatName.draw(win)
        throatRsl = Text(Point(350, 300), "You got " + str(counts["Throat"]) + " out of 10 credits.")
        throatRsl.draw(win)

        # transparent third-eye chakra logo
        teLogo = Image(Point(100, 350), "graphics\p_techakra.gif")
        [teWidth, teHeight] = teLogo.getWidth(), teLogo.getHeight()
        teBg = Image(Point(100, 350), teWidth, teHeight)
        for x in range(teWidth):
            for y in range(teHeight):
                [r6, g6, b6] = teLogo.getPixel(x, y)
                if r6 < 238 and g6 < 238 and b6 > 0:
                    teBg.setPixel(x, y, color_rgb(r6, g6, b6))
        teBg.draw(win)
        teName = Text(Point(200, 350), "Third-eye Chakra:")
        teName.setStyle("bold")
        teName.draw(win)
        teRsl = Text(Point(380, 350), "You got " + str(counts["Third Eye"]) + " out of 10 credits.")
        teRsl.draw(win)

        # transparent crown chakra logo
        crownLogo = Image(Point(100, 400), "graphics\p_crownchakra.gif")
        [cWidth, cHeight] = crownLogo.getWidth(), crownLogo.getHeight()
        crownBg = Image(Point(100, 400), cWidth, cHeight)
        for x in range(cWidth):
            for y in range(cHeight):
                [r7, g7, b7] = crownLogo.getPixel(x, y)
                if r7 < 235 and g7 < 243 and b7 < 238:
                    crownBg.setPixel(x, y, color_rgb(r7, g7, b7))
        crownBg.draw(win)
        crownName = Text(Point(185, 400), "Crown Chakra:")
        crownName.setStyle("bold")
        crownName.draw(win)
        crownRsl = Text(Point(350, 400), "You got " + str(counts["Crown"]) + " out of 10 credits.")
        crownRsl.draw(win)

        sortedList = list(counts.items())
        sortedList.sort(key=byFreq, reverse=True)
        strChakra = Text(Point(603, 130), "Your strongest Chakra is: " + str((sortedList[0])[0]) + ".")
        strChakra.draw(win)
        details = Text(Point(600, 310), "To learn more about yourself,\nsee " + str(
            (sortedList[0])[0]) + ".txt file in the Details folder.")
        details.draw(win)

        pt = win.getMouse()
        while not exitBtn.clicked(pt):
            pt = win.getMouse()

        win.close()


if __name__ == "__main__":
    main()
