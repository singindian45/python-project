"""
Terminal Game
"""
import atexit
import sys
import time
from game_functions import *
from classes import *


def exit_handler():
    # exit handler so that user doesnt abruptly exit the game (we can add a function that saved user's progress here)
    print("My application is ending!")


atexit.register(exit_handler)


# -------------------------------------------------------

# start the BATTLE!
Charizard.local_fight(Venusaur)

# -----------------------------------------------------------------------------------------------------------

# ----------Story-----------
dialogue(
    {
        "???": "Hello there! Welcome to the world of Pokemon! My name is Oak!",
        "Prof.Oak": [
            "People call me the Pokemon Professor!",
            "This world is inhabited by creatures called Pokemon!",
            "For some people, Pokemon are pets. Others use them for fights. Myself...",
            "I study Pokemon as a profession.",
            "First, what is your name?",
        ],
    }
)

player = Trainer(confirm("Enter your name:\t"), 0, {}, "Pallet Town")
printf(f"Right! So your name is {player.name}!")
print()

dialogue(
    {
        "Prof.Oak": [
            "This is my grandson. He's been your rival since you were a baby.",
            "...Erm, what is his name again?",
        ]
    }
)

rival = Trainer(confirm("Enter your rival's name:\t"), 0, {}, player.location)
printf(f"That's right! I remember now! His name is {rival.name}!")
print()

dialogue(
    {
        "Prof.Oak": "Your very own POKEMON legend is about to unfold! A world of dreams and adventures with POKEMON awaits! Let's go!"
    }
)

print(
    """Scene: You are in your bedroom now. You go downstairs to find your mother watching a program on T.V.
Talk to her?
"""
)

event_choice(
    {
        "Yes": "Mother: Right. All boys leave home some day. It said so on TV.\nProf.Oak, next door, is looking for you.",
        "No": "You rude! Go talk to her anyway.\nMother: Right. All boys leave home some day. It said so on TV.\nProf.Oak, next door, is looking for you.",
    }
)

printf(
    """
You step outside the house and see explore your hometown.
You look at the boundless blue sky above you, while the sweet scent of oddish in the forests
reminds you of the amazing journey you're about to embark on!

'There's no place like Pallet Town', you say as you run towards Prof. Oak's Lab.

You arrive at the lab, and look around but Prof.Oak seems to be nowhere in sight.
Upon asking one of the aides, you find out that Prof.Oak has gone to run an errand.

What do you do?
"""
)

event_choice(
    {
        "Wait for Prof.Oak at the lab": [
            "You wait for long but Professor still hasn't returned,\nYou decide to venture into the town and find clues to where he might have gone.",
            "You see a young kid wearing shorts, Talk to him?",
            {
                "Yes": "You talk to the kid\nYoungster Jimmy: When you hear grass rustling, it's usually a pokemon.\nProf.Oak told us so in his orientation class.",
                "No": "You aimlessly roam around the town waiting for Prof.Oak to show up",
            },
        ],
        "Go out and explore the town": [
            "You start exploring the town and try to ask if anyone has seen where Prof. Oak has gone.",
            "You see a young kid wearing shorts, Talk to him?",
            {
                "Yes": "You talk to the kid\nYoungster Jimmy: When you hear grass rustling, it's usually a pokemon.\nProf.Oak told us so in his orientation class.",
                "No": "You aimlessly roam around the town waiting for Prof.Oak to show up",
            },
        ],
        f"Go to {player.name}'s house": [
            f"You enter {player.name}'s house.",
            {
                "Talk to mom?": "Mom: Prof. Oak is the authority on Pokemon, Many pokemon trainers hold him in high regard.\nYou then come out of your house and explore the town again.",
                "Go back to town": "You come out of your house and roam aimlessly hoping Prof. Oak would arrive soon.",
            },
        ],
    }
)


printf(
    "As you're waiting outside in the town, you hear rustling grass in distance. Do you check it out?\n"
)
event_choice(
    {
        "Yes": "You carefully tiptoe towards the grass so you don't scare the pokemon in grass",
        "No": "You decide to not pay attention to the rustling, but after a few minutes your curiosity gets the better of you\nYou carefully tiptoe towards the grass.",
    }
)

printf(
    f"""You see the silhouette of a mouse like pokemon feasting on berries.
'That's a pikachu!' you shout in excitment. The wild Pikachu notices you and prepares to attack.
You notice the electricity crackling near Pikachu's cheeks and suddenly you hear someone shout
"""
)

dialogue({"Prof.Oak": "Hey! Wait! Don't get closer!"})
printf(
    "Prof.Oak throws a pokeball at Pikachu... The pokeball shakes a few times before sparking slightly indicating Pikachu has been captured."
)

dialogue(
    {
        "Prof.Oak": [
            "Whew...",
            "A pokemon can appear anytime in tall grass. You need your own pokemon for your protection.",
            "I know!",
        ]
    }
)

printf(
    """
Prof.Oak asks you to come with him to his lab, to which you happilly agree.

==========================================================================================================

At Prof.Oak's Lab:
"""
)

dialogue(
    {
        rival.name: "Gramps! I'm fed up with waiting!",
        "Prof.Oak": [
            f"{rival.name}? Let me think... Oh, that's right, I told you to come!",
            "Just wait!",
            "",
            f"Here, {player.name}! There are 3 Pokemon here! Haha! They are inside the pokeballs."
            "When I was young, I was a serious Pokemon trainer."
            "In my old age I have only 3 left, but you can have one! Choose!",
        ],
        rival.name: "Hey! Gramps! What about me?",
        "Prof.Oak": f"Be patient! {rival.name}, you can have one too!",
    }
)
