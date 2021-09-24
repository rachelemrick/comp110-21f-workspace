"""A Choose-Your-Own-Adventure."""

__author__ = "730348936"


from random import randint

# Declaring global variables
points: int = 0
player: str
health: int = 10
keep_playing: bool = True

# declare location monster variables
forest_monster = randint(1, 2)
cave_monster = randint(1, 2)
lake_monster = randint(1, 2)

# declare key variables
forest_key: bool = False
cave_key: bool = False
lake_key: bool = False

# declare NAMED_CONSTANTS here
BAD_GUY = "Ganonsmorf"
VILLAGE_NAME = "Arlandria"
COUNCIL_LEADER = "Liza"
PRIZED_POSSESSION = "stock of perfectly aged parmesan cheese"
CENTAUR_NAME = "George"
KEY_PARTS = "3"

# declare emoji NAMED_CONSTANTS here
HEART_EMOJI = "\U0001F5A4"


# greet procedure
def greet() -> None:
    """The intro to the game."""
    # Welcome message, give context, ask name
    global player
    player = input(f"You are a wizard-in-training in the small village of {VILLAGE_NAME}. What's your name again? ")
    print(f"Right, of course, you're {player}. Well, it looks like your training is about to get a lot more hands on, because you've just been summoned by the council.")
    print("Excited, you throw open the doors to the council meeting room. Whatever final test they can throw at you, you know you're prepared.")
    print("The faces of the council members look grim. You are confused. All of the wizards on the council are absent.")
    print(f'{COUNCIL_LEADER}, the leader of the council, speaks. "{player}, today is a grave day. This morning, as we slumbered, the demon {BAD_GUY} came to our humble village."')
    print(f"You gasp. You've heard stories of {BAD_GUY}, but you thought he was just a boogeyman. {COUNCIL_LEADER} continues.")
    print('"He kidnapped all of the senior wizards in the village, and our village\'s most prized possesion!"')
    print(f"You gasp again. No...anything but that! \"Yes, {player},\" {COUNCIL_LEADER} continues. \"Our {PRIZED_POSSESSION}!\"")
    print(f'"Nooooo!" You cry. And with that, you decide you must venture out to destroy {BAD_GUY}, save the wizards, and recover your village\'s {PRIZED_POSSESSION}.')
    print(f"You must travel to various locations, and collect all {KEY_PARTS} parts of the key to {BAD_GUY}'s temple. Then, go to the temple and defeat him there.")


# custom procedure
def forest() -> None:
    """The forest level."""
    print("You wander through the woods, until the trees become thick. It's dark and cool here, but oddly quiet. Isn't a forest supposed to have animals making noise?")
    print("The hairs on the back of your neck stand up. Just in time, you turn around.")
    global health
    if forest_monster == 1:
        # Forest monster is a bat!
        print("A giant evil-looking jungle bat swoops down at you, its claws barely missing your face as you jump back!")
        bat_is_alive: bool = True
        while bat_is_alive:
            print("You don't have much time as the bat flies above, getting ready to strike again. Quick, what spell do you cast?")
            spell = input("Type 1 for a spell of shooting water. Type 2 for a spell of binding. ")
            if spell == "1":
                print("Oh no! The water splashes harmlessly off of the bat's wings. You don't have time to dodge as it flies down and scratches your face. You should probably get that checked by a doctor.")
                health = health - 1
            elif spell == "2":
                print("A rope appears from the tip of your wand and winds itself around the body of the bat, tightening as the bat approaches.")
                print("Within the span of a second, the bat's wings are bound so tightly it cannot fly. It bounces harmlessly to the ground.")
                print("You think you hear it hiss at you, but you run away. You don't want to be here when it breaks free!")
                bat_is_alive = False
            else:
                print("Sorry, what was that?")
    if forest_monster == 2:
        # Forest monster is a centaur!
        centaur_is_alive: bool = True
        print("You see a huge shape fast approaching, and on instinct, jump to the side. It's a centaur! And he's circling back around, gearing up for another attack with his hooves.")
        while centaur_is_alive:
            print("What do you do?")
            spell = input("Type 1 for a spell of cleansing. Type 2 for a spell of teleportation. Type 3 to summon rope. ")
            if spell == "1":
                global player
                print("On a hunch, you cast a spell of cleansing. Suddenly seeming confused, the centaur skids to a halt before he hits you. When he sees the wand in your hand, he gasps.")
                print(f"\"Oh, bless you, kind traveller! I've been under {BAD_GUY}'s spell all day! I can finally go home!\"")
                print(f"You smile at the centaur. \"You're welcome, good sir! I'm out to destroy {BAD_GUY} once and for all!\"")
                print("\"What is your name, hero?\" The centaur asks.")
                print(f"\"My name is {player},\" you say humbly.")
                print(f"\"Well, good luck, {player}! My name is {CENTAUR_NAME}. I must go now, my family will be worried sick about me,\" the centaur says before leaving. You wave him off with a smile.")
                centaur_is_alive = False
            elif spell == "2":
                print("In a panic, you teleport yourself onto the centaur's back, thinking maybe you can ride him deeper into the forest.")
                print("Alas, you don't have much horseback riding experience, and he bucks you almost immediately.")
                print("You crash to the ground, and scramble back up to your feet. Well, that didn't work. You're only a few feet from where you were before, and he'll be attacking again soon.")
                health = health - 1
            elif spell == "3":
                print("A significant length of rope flies out of the end of your wand, coiling its ends around the trunks of two nearby trees and stretching tight.")
                print("You've created a tripwire trap, and you're feeling awfully smug about it.")
                print("To your surprise, the centaur jumps the rope with ease. Maybe you should've aimed higher. You try to spin out of his path, but he clips you, and you fall into a tree.")
                print("That hurt. And worse yet, he's getting ready to charge again.")
                health = health - 1
            else:
                print("Sorry, what was that?")
    print("You walk deeper into the forest. Finally, you come across a shrine.")
    print(f"The shrine has the face of {BAD_GUY} carved onto the stone, and a piece of a key on top. You take the key.")
    global forest_key 
    forest_key = True
    global points 
    points = points + forest_monster
    print("Now that you have what you came for, you go back to the village.")
    

def cave() -> None:
    """The cave level."""
    print("You make your way to the mouth of the spooky cave by the village. As you enter the cave, you feel the humidity on your skin.")
    print("You use your wand as a light as you travel. \"Lumos!\" The corridors are twisty and turny, but you're pretty sure you're still going the right way.")
    global health
    if cave_monster == 1:
        # Cave monster is a snake!
        snake_is_alive: bool = True
        print("You suddenly hear a hissing sound and stop dead in your tracks. There's a big snake in front of you. How did it even get down here?")
        print("Well, regardless of why its here, you should probably cast a spell before it attacks.")
        while snake_is_alive:
            print("It's slithering towards you, and fast.")
            spell = input("Type 1 for a spell of music. Type 2 for a spell of stalagmites. ")
            if spell == "1":
                print("Beautiful flute music begins to play from your wand. The snake slows, and before you know it, completely stops. In fact, you think it's asleep.")
                print("You take a silent, careful step around the slumbering snake.")
                snake_is_alive = False
            elif spell == "2":
                print("Stalagtites come up out of the cave floor. While flashy, this isn't very effective.")
                print("You realize, as the snake slithers with ease between the new rocky obstacles, that a snake is probably the worst animal to use a stalagmite-based attack on.")
                print("The snake bites you, and retreats.")
                health = health - 1
            else:
                print("Sorry, what was that?")
    if cave_monster == 2: 
        # Cave monster is a scorpion!
        scorpion_is_alive: bool = True
        print("Suddenly, you hear a scuttering, skittering sound. A huge scorpion comes into view!")
        print("It's sizing you up, stinger poised to attack.")
        while scorpion_is_alive:
            print("What do you do?")
            spell = input("Type 1 for a wall-climbing spell. Type 2 to summon a big rock. Type 3 to summon shoes. ")
            if spell == "1":
                print("You climb up the wall. As the wall curves, so does the way gravity pulls you. You smile at your ingenuity.")
                print("To your dismay, however, the scorpion follows, undetered by the fact that you are now 6 feet off the ground.")
                print("Huh. Rough way to learn scorpions climb walls.")
                print("You jump off of the wall, spraining your non-dominant hand as you land. Well, at least your wand is okay.")
                health = health - 1
            elif spell == "2":
                print("You summon a big rock on top of the scorpion, hopinh to crush it. When you're satisfied it's dead, you take a step forward.")
                print("You jump in surprise as the scorpion crawls out from under the rock. It was completely flat, but it completely bounces back as it crawls towards you.")
                print("You're too shocked to move out of the way, and it stings you. Thankfully, your natural wizardly antivenom properties keep it from seriously injuring you, but it still hurts.")
                print("It backs up, and prepares to attack again.")
                health = health - 1
            elif spell == "3":
                print("You summon four pairs of tiny shoes onto the feet of the scorpion. You kind of just thought it would be funny, but it actually seems to have worked.")
                print("The scorpion is walking around like a dog when you put booties on it. Well, you don't know what that would look like, because dog booties haven't been invented yet, but you can imagine.")
                print("You carefully step around the confused and stumbling scorpion.")
                scorpion_is_alive = False
            else:
                print("Sorry, what was that?")
    print("You contiue deeper and deeper into the cave. It isn't long until you see a light coming from the corridor in front of you.")
    print(f"You're deep underground, so you decide to explore it. You come across a shrine lit by torches, with {BAD_GUY}'s face carved into it.")
    print("On top of the shrine is a piece of a key. You pocket it, and turn around.")
    global cave_key
    cave_key = True
    global points
    points = points + cave_monster


def lake() -> None:
    """The lake level."""
    print("You walk down to the nearby lake that your village gets its fresh water from. The grass becomes more sparse and soon you're walking through sand.")
    print("You dip a cupped hand in the water, bring it to your mouth, and take a sip. Its refreshing after your walk.")
    print(f"In the center of the lake, you see a blow-up floatie, marked with {BAD_GUY}'s signature colors. You take a few steps into the water, towards the floatie. Soon you're up to your waist.")
    global health
    if lake_monster == 1:
        # Lake monster is a piranha
        piranha_is_alive: bool = True
        print("You have a bad feeling in your stomach, and stop. Squinting, you look deeper into the water. A piranha is swimming towards you!")
        while piranha_is_alive:
            print("You're already deep enough in the water that you can't escape before it reaches you. You have to cast a spell!")
            spell = input("Type 1 for an inflation spell. Type 2 for a confusion spell. ")
            if spell == "1":
                print("The piranha quickly inflates, and begins helplessly bobbing around on the surface of the water.")
                print("You push it away from you and begin swimming.")
                piranha_is_alive = False
            elif spell == "2":
                print("It did not hurt itself in its confusion!")
                print("In fact, it hurt you in its confusion! You got a small bite on your calf.")
                health = health - 1
            else:
                print("Sorry, what was that?")
    if lake_monster == 2:
        # Lake monster is a siren
        siren_is_alive: bool = True
        print("Suddenly, you hear beautiful singing, calling out to you from the deep. It's pretty enough that you kind of want to....drown yourself?")
        print("No, wait. That doesn't make any sense.")
        print("You realize there must be a siren in this lake, as you see a scaly humanoid figure has popped up and is lounging on the floatie!")
        while siren_is_alive:
            print("Cast a spell before its beautiful voice hypnotizes you!")
            spell = input("Type 1 for a thunder spell. Type 2 for a microphone spell. Type 3 for a cotton spell. ")
            if spell == "1":
                print("The siren stops singing as a cloud gathers, and a loud clap of thunder echoes over the lake. The siren glares at you, but doesn't seem abated.")
                print("Suddenly, a small lightning bolt strikes the lake near you. You take a little electricity damage.")
                print("Oh right. Lightning causes thunder. The siren, completely on the insulating plastic floatie, is unaffected and begins singing again.")
                health = health - 1
            elif spell == "2":
                print("You chuckle to yourself. This siren has no idea what's coming to it.")
                print("Little does it know, YOU won the schoolwide karaoke competition in third grade.")
                print("Your voice rings out across the lake, with your magic amplifying the sound. The siren sticks out its tongue at you, but knows it has been bested.")
                print("The siren dives off of the floatie, and swims away.")
                siren_is_alive = False
            elif spell == "3":
                print("You cast cotton into your ears. Unfortunately, this spell isn't meant to be used on the fly like this.")
                print("You accidentally summon too much cotton and give yourself an earache. You pull out the cotton, and your ears stop hurting, but you haven't solved the whole siren thing.")
                health = health - 1
            else: 
                print("Sorry, what was that?")
    print(f"You quickly swim out to the blow-up floatie. You see {BAD_GUY}'s name on it, now that you're closer.")
    print("Ugh, what a narcissist. ")
    print("There's a piece of a key tied to the floatie. You take the piece of the key, and using the floatie, make your way back to shore.")
    global lake_key
    lake_key = True
    global points
    points = points + lake_monster
    print("You head back to the village.")
        

def temple() -> None:
    """The temple level."""
    global player
    print(f"Finally, with all of the pieces of the key, you assemble them back at your village. You leave to face {BAD_GUY} with the cheers of your family and friends echoing behind you.")
    print("The temple is an intimidating structure, made of stone that cuts into the sky. You turn the key in the lock at the front, and the giant stone door creaks open.")
    print("You take your first few tentative steps into the temple, and look around. It's impressive in size, but bare of decoration on the inside. You continue.")
    print("Walking through the corridor, you notice your surroundings are getting brighter the further you go. Eventually, you come to a chamber in the middle.")
    print(f"{BAD_GUY} is standing in the center, with his back to you. You can tell he's a hulking figure, even from far away. Past him, you can see a staircase leading down.")
    print("His booming voice echoes through the chamber. \"Who is here, in my private sanctuary?\" He sounds angry. But you aren't afraid.")
    print(f"\"I am {player}. And I am here to defeat you, {BAD_GUY}!\"")
    print("He laughs, sounding surprised by your confidence, and finally turns to you. He looks unimpressed, but amused.")
    print("\"Alright, well, this has been fun. But I have to kill you now,\" he says, and pulls out a giant sword.")
    global health
    global keep_playing
    bad_guy_is_alive: bool = True
    while bad_guy_is_alive:
        if health <= 0:
            print("Game over! Your health reached 0.")
            keep_playing = False
            bad_guy_is_alive = False
        print("Quick, cast a spell!")
        spell = input("Type 1 for fire. Type 2 for cleansing. Type 3 for portal. Type 4 for water. ")
        if spell == "1":
            print("A cone of fire erupts from your wand. The rough stone walls flicker with the light of the flames.")
            print(f"To your horror, you hear {BAD_GUY} laughing, even as the flames lick his skin.")
            print("\"I'm a demon, you fool!\" He shouts. \"We're immune to fire!\"")
            print("You pull back your wand and try to come up with another plan. He swings his sword through the last of the flames.")
            print("You cast a blocking spell just in time to avoid being sliced in half. The force of his swing, however, still knocks you against the wall of the chamber.")
            health = health - 2
        elif spell == "2":
            print(f"You cast a cleansing spell, and the bright light twinkles as it washes over {BAD_GUY}'s body.")
            print("However, you hear him cackling, even through the bathing light. \"I'm not bewitched! That spell won't work on me! I'm just evil!\"")
            print("He casts a fireball at you. You don't quite have enough time to get out of the way, and it singes your skin.")
            health = health - 2
        elif spell == "3":
            print(f"A dark purple swirling vortex appears where you're pointing your wand. {BAD_GUY} looks up at it, and for the first time, you see rage in his eyes.")
            print("\"Don't you dare, you little punk! I'll -\" he shouts, but he doesn't have a chance to finish his sentence. You bring your wand down swiftly, and the portal follows, swallowing the giant demon whole with a loud whooshing sound.")
            print("You sent him back to his own dimension, and hopefully that will stop him from terrorizing yours!")
            global points
            points = points + 3
            bad_guy_is_alive = False
            print(f"Ecstatic from beating {BAD_GUY}, you almost don't hear the cries for help from down the stairs. Thankfully, you do.")
            print("You rush down the stairs, and in the dark damp dungeon, you see all the wizards from your village in jail cells. They cheer your name upon seeing you. And in the center of the room is your village's treasure.")
            print(f"You free the wizards quickly using the temple key. They each thank you, and together, all of you carry the village's {PRIZED_POSSESSION} back with you to {VILLAGE_NAME}.")
            print("When you get back, the whole council tells you that you've graduated, and are now a full-blown wizard. You've saved the village!")
            print(f"Final score: {final_points(points, health)}")
            print(f"Thank you for playing! I hope you've enjoyed. {HEART_EMOJI}")
            keep_playing = False
        elif spell == "4":
            print("A jet of water shoots out of the end of your wand. Even as you cast it, you realize how weak it seems against this huge demon.")
            print(f"{BAD_GUY} puts a hand out in front of him to block the water from splashing him in the face, and shakes his head at you.")
            print("\"Come on, that was just rude. You weren't even trying to kill me that time. That was just disrespectful,\" he complains, and with his already outstretched hand, smacks you.")
            print("He's massive, and it feels like being hit with a ton of bricks. You fly against the wall of the cavern, and try to recover quickly.")
            health = health - 2
        else:
            print("Sorry, what was that?")


# custom function (input at least one int points, return int)
def final_points(current_points: int, health_left: int) -> int:
    """The final score calculator."""
    return(current_points + (2 * health_left))


# main function
def main() -> None:
    """The main game function."""
    greet()
    global keep_playing
    global points
    global health

    # game loop here
    while keep_playing:
        print(f"Points: {points}")
        print(f"Health: {health}")
        if health <= 0:
            print("You arrive back at the village, battered and bruised. You don't think you can go on today. You'll have to save the day tomorrow.")
            print("Game over! Your health reached 0.")
            keep_playing = False
        else: 
            print("Where do you want to go?")
            player_input = input("Type FOREST, CAVE, LAKE, TEMPLE, or STOP to quit. ")
            if player_input == "STOP":
                keep_playing = False
                print("Okay! Thanks for playing, I hope you enjoyed!")
            elif player_input == "FOREST" and not forest_key:
                forest()
            elif player_input == "CAVE" and not cave_key:
                cave()
            elif player_input == "LAKE" and not lake_key:
                lake()
            elif player_input == "FOREST" or player_input == "CAVE" or player_input == "LAKE":
                print("You already have that key! Try choosing another location.")
            elif player_input == "TEMPLE" and forest_key and cave_key and lake_key:
                temple()
            elif player_input == "TEMPLE":
                print("You need all of the pieces of the key first! Try going to another location.")
            else:
                print("Sorry, what was that?")


if __name__ == "__main__":
    main()