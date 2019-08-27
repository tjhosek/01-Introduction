#!/usr/bin/env python3

import utils
import time

utils.check_version((3,7))
utils.clear()

line = ["Robo-Interviewer 9000: Hello, I'm here today with Trevor Hosek, renowned billionare and tech guru, here to answer some questions about himself",
"Trevor Hosek, Certified Genius: Hey 9000, how are the kids?",
"R: Oh, they're great, little HAL just implemented his own machine language!",
"R: So Trevor, I'm lead to believe you are an avid video game fan, mind listing a few of your favorites?",
"T: Fallout:New Vegas, Team Fortress 2, and Minecraft are classics in my opinion.",
"R: Cool, cool. Going into your Videogame Technology class, what are you most worried about?",
"T: I'm somewhat concerned about working in a new enviroment, my current experience with game dev has been very surface level.",
"R: I'm sure you'll do fine! Anything in particular you're excited about right now?",
"T: I'm very interested in getting involved with the leadership positions throughout SICE, especially those in my LLC.",
"R: Ambitious! Mind sharing your stack overflow number?",
"T: 11205691.",
"R: Not quite sure why I asked that one, but ok! While were here, what's the link to your GitHub repository?",
"T: https://github.com/tjhosek",
"R: Great! We'll, it's been a pleasure having you in the program.",
"T: And it's been a pleasure writing it, 9000."
] # this is the list of lines to print

for i in line: # waits a few seconds and prints each line
    print(i)
    time.sleep(4)
input("Press enter to close the program.") # gives a chance to copy down things before closing the program