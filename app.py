import time
import sys

def slow_print(text, delay=0.03):
    """Print slowly for dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

health = 3  # Starting health

def check_health():
    global health
    if health <= 0:
        slow_print("\nYour health is critically low, and you are fading fast.")
        slow_print("Game Over.")
        sys.exit()
    elif health == 2:
        slow_print("\nYou're feeling weak, but you can still continue.")
    elif health == 1:
        slow_print("\nYou're in pain, but you're still hanging on.")
    
    slow_print(f"\nYour current health is: {health}/3")

visited_choices = []  # Track visited choices

def get_choice(available_choices, prompt, visited_choices):
    # get user input and prevent repeating previous choices
    choice = ""
    while choice not in available_choices or choice in visited_choices:
        choice = input(prompt).strip()
        if choice in visited_choices:
            slow_print("\nYou've already chosen that option. Try something else.")
        elif choice not in available_choices:
            slow_print("\nInvalid choice. Try again.")
    visited_choices.append(choice)  # Add choice to array
    return choice

intro_displayed = False

def intro():
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")

    # Only print the intro text if it's the first time the function is being called
    if not intro_displayed:
        slow_print("You find yourself driving along a deserted road. The fog is thick, and the headlights barely cut through the mist.")
        slow_print("The town of Silent Hill looms in the distance, shrouded in darkness and silence. Your car sputters and stalls. You’re stranded.")
        slow_print("In desperation, you decide to venture into the town. You’ve heard stories, but you never believed them until now. The fog feels unnatural.")
        slow_print("Stepping out of the car, the cold air bites at your skin. The silence is suffocating. The town's oppressive atmosphere begins to close in on you.")
        intro_displayed = True
    
    choice = get_choice(["1", "2"], "\n(1) Enter Silent Hill\n(2) Stay by the car\n> ", visited_choices)
    
    if choice == '1':
        slow_print("\nYou start walking toward Silent Hill, the fog growing denser with every step. The sound of your footsteps is the only thing you can hear.")
        town_square(visited_choices)
    elif choice == '2':
        slow_print("\nYou decide to stay by the car. Hours pass, and then the sun sets. The fog deepens, and strange sounds fill the air. Eventually, you lose consciousness.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        intro()

def town_square(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("You finally reach the town square. The fog is even thicker here. Streetlights flicker, casting eerie shadows across the empty streets.")
        slow_print("A dilapidated fountain stands in the center, covered in grime. Rusted signs point toward a hospital and a school. You hear distant whispers, but there’s no one in sight.")
        slow_print("A faint sound of footsteps approaches from behind, but when you turn, there’s no one there. The atmosphere feels heavier, suffocating.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3", "4"], "\n(1) Go to the hospital\n(2) Head toward the school\n(3) Investigate the fountain\n(4) Explore the abandoned shops\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou decide to head toward the hospital, hoping to find some answers.\n")
        hospital(visited_choices)
    elif choice == '2':
        slow_print("\nYou walk toward the school, hoping to find something or someone who can help you.\n")
        school(visited_choices)
    elif choice == '3':
        slow_print("\nYou investigate the fountain. The water is stagnant and filled with something that looks like blood. A faded inscription is carved into the base.")
        slow_print("'Those who seek refuge will never find it.' A shiver runs down your spine.")
        slow_print("Suddenly, the ground beneath you trembles, and the water in the fountain swirls violently.")
        fountain_encounter(visited_choices)
    elif choice == '4':
        slow_print("\nYou decide to explore the abandoned shops. Most of them are boarded up, but a few have broken windows. The door to a small antique store creaks open.")
        slow_print("Inside, dust and cobwebs cover the shelves, but there’s an unsettling feeling that something or someone is watching you.")
        antique_shop(visited_choices)

def school(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("You approach the school, a looming, crumbling structure. The windows are shattered, and the front doors creak in the wind.")
        slow_print("A sense of dread fills the air as you step closer. The school’s eerie silence is only broken by the occasional distant creak of the building settling.")
        slow_print("You hesitate at the door, but something draws you inside. As you push the door open, it squeaks loudly, and the smell of decay hits you.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3"], "\n(1) Enter the school\n(2) Check the basement windows\n(3) Leave and head back to the town square\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou step into the school. The hallway is dark and narrow, with peeling wallpaper and broken lockers. The atmosphere is thick with unease.")
        slow_print("As you move deeper, you hear a faint, creepy voice from one of the classrooms.")
        school_hallway(visited_choices)
    elif choice == '2':
        slow_print("\nYou move around to the basement windows and peer inside. The glass is cracked, but you can see faint movement in the darkness below.")
        slow_print("Something is down there... you can’t shake the feeling that it's staring back at you.")
        basement_encounter(visited_choices)
    elif choice == '3':
        slow_print("\nYou decide it’s too dangerous to stay. You turn and head back toward the town square, but the air feels colder than before.")
        town_square(visited_choices)

def school_hallway(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("You step into the school hallway, the air heavy with dust and an unsettling silence. The walls are lined with lockers, some of which are open and empty.")
        slow_print("The flickering lights above cast long, distorted shadows on the floor, making it difficult to see clearly.")
        slow_print("A distant thud echoes through the building, making you jump. The source of the sound is unclear, but it’s coming from deeper in the school.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3", "4"], "\n(1) Investigate the first classroom\n(2) Head down to the basement\n(3) Leave and go back to the town square\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou enter the first classroom. The desks are overturned, and papers are scattered across the floor. In the corner, a chalkboard is smeared with strange symbols.")
        slow_print("Suddenly, you hear the sound of someone whispering your name. You turn, but no one is there.")
        classroom_encounter(visited_choices)
    elif choice == '2':
        slow_print("\nYou head down toward the basement, where the temperature drops significantly. The staircase creaks beneath your feet as you descend into the dark.")
        slow_print("You feel a sense of dread as you reach the bottom, and a strange figure appears in the corner of your eye.")
        basement_encounter(visited_choices)
    elif choice == '3':
        slow_print("\nYou decide to leave the hallway. The feeling of being watched only intensifies as you head back toward the town square.")
        town_square(visited_choices)

def classroom_encounter(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("You enter the classroom, the door creaking loudly as you push it open. The room is dark, save for the faint light coming through the cracked windows.")
        slow_print("The desks are in disarray, some of them overturned. A chalkboard at the front of the room is covered in strange, unsettling symbols, and there's a faint smell of something rotten in the air.")
        slow_print("You hear a faint whispering from one of the desks, but when you approach, nothing is there.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3"], "\n(1) Investigate the desk where the whisper came from\n(2) Examine the chalkboard\n(3) Leave the classroom\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou walk over to the desk, your heart racing. As you look inside, a cold hand suddenly grabs your wrist. You pull away in shock, but there's no one there.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        classroom_encounter(visited_choices)
    elif choice == '2':
        slow_print("\nYou approach the chalkboard and begin to examine the strange symbols. As you touch them, the symbols seem to shift and twist, forming disturbing images.")
        slow_print("The air grows colder, and you feel an unnatural force pushing against you. The whispers grow louder.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        classroom_encounter(visited_choices)
    elif choice == '3':
        slow_print("\nYou quickly decide to leave the classroom. The door slams shut behind you, and the whispers fade into the distance.")
        school_hallway(visited_choices)

def hospital(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("\nThe hospital is dark, decayed, and filled with a sickly smell. Broken furniture litters the hallways, and peeling wallpaper exposes the crumbling walls underneath.")
        slow_print("You can hear faint crying coming from the upper floors, and something drips steadily onto the floor from the ceiling. The place seems... alive in some way.")
        slow_print("At the far end of the hallway is a rusted elevator, but the doors are partially closed. A staircase leads upward to the second floor.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3", "4"], "\n(1) Investigate the elevator\n(2) Go up the stairs\n(3) Explore the ground floor\n(4) Find the source of the crying\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou approach the elevator. As you press the button, the lights flicker, and the door creaks open. A foul smell pours out, and the air feels thick.")
        slow_print("Inside, the walls are covered in strange symbols. The elevator descends on its own without you pressing anything.")
        elevator_ride(visited_choices)
    elif choice == '2':
        slow_print("\nYou climb the stairs cautiously. The second floor is in worse condition, the walls covered in unsettling, cryptic messages.")
        slow_print("A door creaks open by itself at the end of the hall. You hesitate but decide to investigate.")
        second_floor(visited_choices)
    elif choice == '3':
        slow_print("\nYou decide to explore the ground floor more thoroughly. As you step into one of the rooms, a rusted wheelchair rolls toward you on its own.")
        slow_print("Suddenly, the lights go out, and you hear something heavy breathing in the darkness.")
        ground_floor(visited_choices)
    elif choice == '4':
        slow_print("\nYou follow the sound of the crying, which seems to echo from the walls themselves. It leads you to an old, abandoned operating room.")
        slow_print("Inside, you find a bloody surgical table, and the crying stops abruptly. A woman appears in the doorway, her face disfigured and her hands outstretched.")
        slow_print("She whispers, 'It’s your turn now.'")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        hospital(visited_choices)

def elevator_ride(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("\nThe elevator descends deeper into the building. The air becomes oppressive, and strange whispers fill the space.")
        slow_print("The lights flicker once more, and you catch a glimpse of something moving in the corners of your eyes.")
        slow_print("When the doors open, you’re greeted by a room full of mannequins with twisted, contorted faces staring back at you. The hum grows louder, almost deafening.")
        slow_print("You step out, and the doors slam shut behind you.")
        intro_displayed = True
    
    choice = get_choice(["1", "2", "3"], "\n(1) Investigate the mannequins\n(2) Leave the room\n(3) Go deeper into the hospital\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou walk toward the mannequins. As you get closer, one of them blinks. You freeze in place, but it’s too late.")
        slow_print("The mannequins spring to life, their limbs jerking unnaturally toward you. You barely manage to dodge their grasp.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        elevator_ride(visited_choices)
    elif choice == '2':
        slow_print("\nYou decide to leave the room. As you step back into the elevator, it begins its ascent on its own, returning to the ground floor.")
        slow_print("You exit the elevator, your heart racing. Something is not right here.")
        town_square(visited_choices)
    elif choice == '3':
        slow_print("\nYou press forward, following the whispers deeper into the hospital. The walls seem to close in on you as the darkness grows thick.")
        slow_print("You stumble into a room that is filled with old medical equipment. On a table lies a journal with strange notes written in blood.")
        hospital_journal(visited_choices)
    else:
        slow_print("\nInvalid choice. Try again.\n")
        elevator_ride(visited_choices)

def hospital_journal(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")

    if not intro_displayed:
        slow_print("\nYou open the journal slowly, its pages yellowed and brittle with age. The writing inside is erratic, barely legible. Some pages are stained with what looks like blood.")
        slow_print("As you flip through the pages, a strange chill fills the air. The ink begins to blur, and the words twist and change, as if they're alive.")
        slow_print("On the last page, you find a drawing—a figure, twisted and contorted, with hollow eyes staring at you. The figure seems to move, its gaze following you.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3"], "\n(1) Read the journal's notes\n(2) Close the journal and leave the room\n(3) Look around the room\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou read the notes carefully, deciphering the garbled writing. It describes the twisted experiments that took place here, some of which are beyond comprehension.")
        slow_print("As you reach the end of the journal, you feel a sharp pain in your chest. You look down to see your own blood dripping onto the page.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        hospital_journal(visited_choices)
    elif choice == '2':
        slow_print("\nYou quickly close the journal, a sense of dread rising in your chest. You leave the room, but the oppressive atmosphere clings to you.")
        slow_print("You make your way back to the elevator, the eerie hum still lingering in the air.")
        elevator_ride(visited_choices)
    elif choice == '3':
        slow_print("\nYou glance around the room, your eyes darting nervously. The walls are covered in old medical charts, and there are strange devices that you don't recognize.")
        slow_print("One of the devices suddenly sparks to life, and you feel a jolt of electricity surge through your body.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        hospital_journal(visited_choices)

def second_floor(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("\nThe second floor is even more unsettling. The walls are covered in disturbing drawings, and the air smells of rot and decay.")
        slow_print("You hear something scratching from behind a door. Your heart races as you step toward the source of the noise.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3"], "\n(1) Open the door\n(2) Investigate the hallway\n(3) Go back downstairs\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou open the door slowly, revealing a small, dark room. Inside, you find an old wooden box with strange markings.")
        slow_print("Before you can open it, a cold hand grabs your shoulder. You spin around, but no one is there.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        second_floor(visited_choices)
    elif choice == '2':
        slow_print("\nYou cautiously investigate the hallway, but the atmosphere grows heavier with every step. Suddenly, the lights flicker and go out.")
        slow_print("You hear a whisper in the dark, 'You shouldn’t be here.' Something cold brushes against your neck.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        second_floor(visited_choices)
    elif choice == '3':
        slow_print("\nYou decide to retreat downstairs. As you leave, you hear a faint laugh from behind you, but when you turn around, the hallway is empty.")
        town_square(visited_choices)
    else:
        slow_print("\nInvalid choice. Try again.\n")
        second_floor(visited_choices)

def ground_floor(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")

    if not intro_displayed:
        slow_print("\nYou stumble into an old medical room filled with rusted equipment and old surgical tools.")
        slow_print("A strange smell fills the air. As you approach a table, you notice old bloodstains and a pair of scissors lying next to a body bag.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3"], "\n(1) Open the body bag\n(2) Search the room\n(3) Leave the room\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou open the body bag, revealing a grotesque sight. The body inside is decomposed, but its eyes are wide open, staring at you.")
        slow_print("Suddenly, the body jerks, and a hand shoots out from the bag, grabbing you by the wrist.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        ground_floor(visited_choices)
    elif choice == '2':
        slow_print("\nYou search the room but find nothing of value. The air grows colder, and you feel an overwhelming sense of dread.")
        town_square(visited_choices)
    elif choice == '3':
        slow_print("\nYou leave the room quickly, your heart racing. The hallway seems even darker now, and the silence feels suffocating.")
        town_square(visited_choices)
    else:
        slow_print("\nInvalid choice. Try again.\n")
        ground_floor(visited_choices)

def basement_encounter(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("\nYou reach the basement, and the air feels impossibly thick. There’s a sense of malevolent presence down here, something ancient and evil.")
        slow_print("The floor is covered in old, rotting medical equipment, and strange symbols are carved into the walls. A flickering light reveals a door at the far end.")
        slow_print("Suddenly, you hear footsteps behind you, but when you turn, there’s no one there.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3"], "\n(1) Open the door at the end of the room\n(2) Search for another exit\n(3) Confront whatever is following you\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou open the door, revealing a room filled with strange machinery. In the center of the room, there is a large metal chair with chains attached.")
        slow_print("A voice whispers, 'Sit down, it’s the only way.' You feel drawn to the chair, unable to resist.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    elif choice == '2':
        slow_print("\nYou search frantically for another exit, but the walls seem to shift around you. The light flickers again, revealing shadows of creatures.")
        slow_print("You run, but you can't find your way out. The walls close in, and you are consumed by the darkness.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    elif choice == '3':
        slow_print("\nYou turn to confront the entity following you, but as you do, it reveals itself—a horrifying figure, its face a twisted mass of faces, all contorted in agony.")
        slow_print("Before you can react, it lunges at you.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    else:
        slow_print("\nInvalid choice. Try again.\n")
        basement_encounter(visited_choices)

def fountain_encounter(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("\nThe fountain begins to churn violently, and you feel the ground tremble beneath your feet.")
        slow_print("The water rises, transforming into something… otherworldly. Figures begin to emerge from the water, their twisted forms barely human.")
        slow_print("They begin to move toward you, their mouths open in silent screams, their eyes hollow and empty.")
        intro_displayed = True

    choice = get_choice(["1", "2", "3"], "\n(1) Run from the fountain\n(2) Stand your ground\n(3) Try to communicate with them\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou turn and run, but the fog grows thicker, and the ground becomes slick. You stumble, and one of the figures catches up with you.")
        slow_print("You scream as it pulls you into the water.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    elif choice == '2':
        slow_print("\nYou stand firm, but as they get closer, their forms begin to distort, becoming monstrous. The sound of their screams fills your ears.")
        slow_print("In the end, you are consumed by them, lost in the darkness.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    elif choice == '3':
        slow_print("\nYou try to communicate, but the figures remain silent, their empty eyes fixed on you.")
        slow_print("As you speak, the water splashes violently, and the figures close in, dragging you into the fountain.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    else:
        slow_print("\nInvalid choice. Try again.\n")
        fountain_encounter(visited_choices)

def antique_shop(visited_choices):
    global health
    global intro_displayed
    visited_choices = []
    print("================================================================================================================")
    
    if not intro_displayed:
        slow_print("\nThe antique shop is filled with old, dusty relics. The shelves are cluttered with broken trinkets, tarnished mirrors, and warped furniture.")
        slow_print("In the back of the shop, there is an old painting. The painting depicts a figure standing alone in a foggy landscape. Its eyes seem to follow you.")
        slow_print("The shopkeeper's voice comes from nowhere, whispering, 'Be careful what you touch, everything in here is alive.'")
        intro_displayed = True

    choice = get_choice(["1", "2", "3"], "\n(1) Examine the painting\n(2) Touch one of the mirrors\n(3) Leave the shop\n> ", visited_choices)

    if choice == '1':
        slow_print("\nYou approach the painting, and as you touch it, the figure's eyes snap open. It begins to speak, 'You shouldn’t have come here.'")
        slow_print("The painting begins to bleed, and you are pulled into it, trapped inside the frame.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    elif choice == '2':
        slow_print("\nYou reach out to touch one of the mirrors. As you do, your reflection begins to distort, becoming something monstrous.")
        slow_print("The reflection smiles back at you, but it's not your smile.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    elif choice == '3':
        slow_print("\nYou decide to leave the shop, but as you step outside, the door slams shut, and the shop vanishes into thin air.")
        slow_print("You're left standing in the fog, feeling even more alone.")
        health -= 1
        slow_print("You take 1 point of damage!")
        check_health()
        town_square(visited_choices)
    else:
        slow_print("\nInvalid choice. Try again.\n")
        antique_shop(visited_choices)

intro()
