This is a personality quiz, specifically a Chakra quiz, with ~70 questions in the form of a video game.

There are 2 classes for this project:
- The first class is "char", which has 7 methods in total.
+) __init__(win,x1,y1): The first method is draw the main character (the player) in the game window.
This takes 3 parameters: win, x1, y1. win is the name of the game window, while (x1,y1) is the point where the main character will be drawn.

+) getBack() and getFront(): These methods will return the x value in the back and the front of the character.

+) standBy(): this method will make sure when called, the character will not move.

+) moveChar(key, vel): this method needs 2 parameters: key and vel. When the play push "a", the character moves left; otherwise, when "d" is pushed, the character moves right.
Parameter "key" is what key the player pushed, and vel is the velocity of the character.

+) choose(key): return True if the player pushes "c" and False if the player pushes other keys.

+) undrawChar(): delete the main character

- The second class is "game", which has 9 methods in total.
+) __init__(win, char): win is the working window, char is the main character.

+) addNPC(img, xpos, ypos): draw an NPC at (xpos, ypos). img is the image of the NPC.

+) delNPC(): delete a NPC

+) startConvo(key): return True when player pushes "c" and the distance from the front of the NPC to the front of the player is less than 80 pixels.

+) dialog(sentence): draw the dialogue box with the sentence in the center.

+) changeDia(sentence): replace the previous sentence to a new one without having to draw multiple dialogue boxes.

+) stopDia(): stop the conversation by undraw both the sentence and the box.

+) selection(clist, sen1, sen2, category): draw 2 choices on the screen. If the player choose sen1, the "category" will +1 frequency in "clist". If they pick sen2, the game will continue without adding.

+) quitGame(): quit game by undrawing the main character.


This project also has a function that returns the second variable in a pair so that when showing the highest result, the program can sort from the category with the highest frequency to that with the lowest frequency.

At first, I tried to put all the scenes in a single while loop, the program still ran but there was a problem: when I press "c" or "enter", the game keeps progress to the next scene without having any conversation with the NPC.
Therefore, I have to split every scene out.
I also tried to implement an Exit/Quit button. It worked, but after having clicked the button, the game will not close immediately. Instead, the player have to press a random key after clicking on the button in order to close the game.
After splitting all the scenes out, I also make sure after each scene the player can close the game if they want to quit early. I kept getting a error saying getKey() was unable to execute because the window had been closed. As a result,
I put each scene in a condition: "if run:" so that getKey() only be read when the game is running.
I also attempted to include all the dialogues in a single textfile (like the testdialog.txt I included in the program) and set a loop so that it can save some time. However, each dialogues have different length and while some have latter response from the NPC, some do not, a loop will not be able to perform my desired result.
For future development, I want to figure out how to condense the codes, especially the dialogues.