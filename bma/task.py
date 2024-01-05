"""
The code for the task loop
"""

from random import choice, randint
from typing import Tuple
from bma.session import U, Dict, Session, time
from subprocess import run

# Blackmail file path
BMAIL_PATH = "./bmail.txt"

# List of tasks and descriptions
TASKS: Dict[float, Tuple[str, str]] = {

    0: ("error", "error state"),
    1: ("reset", "reset from prior task loops"),
    2: ("humiliation", "write on body"),
    3: ("pain", "equip pain equipment"),
    4: ("fuck", "equip fuck equipment"),
    5: ("bondage", "equip partial bondage"),
    6: ("crossdressing", "dress like the opposite gender"),
    7: ("humiliation", "wear exposing clothes"),
    8: ("hidden", "wear cover up clothes"),
    9: ("psudo", "wear cover up clothes"),
    10: ("exposed", "wear cover up clothes"),
    11: ("piss", "drink fluids"),
    12: ("rape", "you must do as told"),
    13: ("public", "go somewhere physical"),
    14: ("protected", "go somewhere physical"),
    15: ("private", "go somewhere physical"),
    16: ("humiliation", "record / stream"),
    17: ("hidden", "record / stream"),
    18: ("psudo", "record / stream"),
    19: ("exposed", "record / stream"),
    20: ("humiliation", "do humiliation act"),
    21: ("piss", "do piss act"),
    22: ("fuck", "do fuck act"),
    23: ("pain", "do pain act"),
    24: ("alt", "do alt cum act"),
    25: ("cum", "do cum act"),
    26: ("humiliation", "cleanup"),
    27: ("hidden", "post"),
    28: ("psudo", "post"),
    29: ("exposed", "post"),
    30: ("debug", "debug")
}

def format_task(user: Session, dif: int) -> str:
    """
    The actual cration of text for a task

    :param user: The user data
    :param dif: The difficulty
    :return: the generated task
    """
    def c(s: str) -> str:
        t = choice(s.split())
        return (t.replace("_", " "))
    i = user.task_count
    s1 = "bitch whore cum_here fuck_me free_use slave use_me fuck_toy slut"
    s2 = "thigh chest upper_arm ass stomach foot"
    s3 = "face forhead neck lower_leg lower_arm hand foot colar neck"
    s4 = "clamps/clothes_pins rice_pads hot_sauce tooth_paste pin_pads"
    s5 = "legs toung arms stomach"
    s6 = "dick/clit ass nips"
    s6 = "arms legs thighs ankels wrists feet"
    s7 = "tape rope chain clothes"
    s8 = "x x x x x x x x x x x x x"
    s9 = "colar_bone knee waist"
    s10 = "coffie tea soda water"
    s11 = "DOB height weight age sex gender initals"
    s12 = "first_name last_name country state postal-code"
    s13 = "full_name address phone_number personal_email"
    s14 = (
            "pretend_you_are_on_a_phone_call_and_explain_something_embaressing_out_loud"
            " pretend_you_are_on_a_phone_call_and_explain_you_have_a_std_out_loud"
            " say_'i_am_a_public_use_whore'_in_a_normal_speaking_voice"
            " say_'i_am_less_than_human'_in_a_normal_speaking_voice"
            " say_'i_am_whore_slave'_in_a_normal_speaking_voice"
            " say_'i_do_not_deserve_love'_in_a_normal_speaking_voice"
            " say_'i_am_a_slave'_in_a_normal_speaking_voice"
            " make_a_100_word_post_on_discord_about_how_horny_you_are"
            " make_a_100_word_post_on_discord_about_one_of_your_falures"
            " make_a_100_word_post_on_discord_about_why_you_are_grose"
            " hold_your_mouth_open_untill_you_drool_on_your_self"
            " hold_your_mouth_open_untill_you_drool_on_your_self"
            " buy_an_embarsing_product_from_a_store"
            " interact_with_people"
            "crawll_on_the_floor_for_5m"
    )
    s15 = (
            "lick_a_floor_/_toilet_/_someting_dirty"
            " piss_your_pants"
            " give_yourself_a_golden_shower"
            " drink_a_cup_of_your_piss"
            " piss_into_some_food_and_eat_it"
            " chew_up_some_food_and_spit_it_back_out;_then_eat_it_up"
            " chew_up_some_food_and_spit_it_back_out_on_the_floor;_then_eat_it_up"
            " piss_on_on_the_floor;_then_lick_it_up"
            " piss_on_on_the_floor"
            " piss_your_pants;then_suck_the_mosture_out_of_your_clothes"
            " crawll_on_the_floor_for_10m"
    )
    s16 = "dick/clit ass ass/pussy nips mouth"
    s17 = "hand dildo marker/pen the_first_thing_you_see_that_will_fit vibe"
    s18 = (
            "keep_this_media_on you_device"
            " set_it_as_your_phone_background"
            " crop_the_media_to_be_SFW_and_set_it_as_your_profile_pic"
           )
    s19 = (
            "print_out_a_frame_and_leave_it_somewhere_hidden_in_public"
            " put_it_on_a_thumb_drive_and_leave_it_somewhere_hidden_in_public"
            " post_it_to_the_discord"
            " post_it_to_the_discord"
            " post_it_to_the_discord"
            " post_it_to_a_porn_site"
            " post_it_to_a_porn_subredit"
            " post_it_to_a_porn_subredit"
            " send_it_to_a_random_email"
            " send_it_to_a_random_email"
            " send_it_to_a_random_email"
            " send_it_to_a_random_discord_user"
            " send_it_to_a_random_discord_user"
            " send_it_to_a_random_discord_user"
            " set_it_as_a_lock_screen"
            " set_it_as_a_lock_screen"
            " set_it_as_a_lock_screen"
           )
    tmp = ""
    if (i == 0):
        tmp += (f"You should not be able to see this. Contact an admin."
                f" (CODE-A) ")
    elif (i == 1):
        if (dif >= 2):
            tmp += (f"You may not remove or undo anything from the last task"
                    f" for this task. ")
        else:
            tmp += (f"You may remove or undo anything from the last task"
                    f" for this task. ")
    elif (i == 2):
        if (dif <= 1):
            tmp += (f"Write {c(s1)}"
                    f" on your {c(s2)}.")
        elif (dif <= 3):
            tmp += (f"Write {c(s1)}"
                    f" on your {c(s3)}.")
        else:
            tmp += (f"Write {c(s1)}"
                    f" on your {c(s3)} with permanant marker.")
    elif (i == 3):
        if (dif <= 2):
            tmp += (f"Apply {dif} {c(s4)}"
                    f" to your {c(s5)}.")
        else:
            tmp += (f"Apply {dif} {c(s4)}"
                    f" to your {c(s6)}.")
    elif (i == 4):
        if (dif >= 3):
            tmp += (f"Apply {c(s4)}"
                    f" to your {c(s5)}. It should be on the {dif}th"
                    f"highest setting or be the {dif}th largest you own.")
        elif (dif <= 2):
            tmp += (f"You may not fuck / masturbate untill told too.")
                    
        else:
            tmp += (f"You must try and always masturbate untill told too.")
    elif (i == 5):
        if (dif <= 1):
            tmp += (f"Put in a gag")
        elif (dif <= 2):
            tmp += (f"Bind your {c(s6)} together"
                    f" with {c(s7)}.")
        else:
            tmp += (f"Apply the bondage in image {c(s8)}.")
    elif (i == 6):
        tmp += (f"Wear {dif} clothes of the opposite gender.")
    elif (i == 7):
        tmp += (f"Wear / remove clothes untill the skin {dif} inches above and below your"
                f" {c(s9)}. If you cant fo this with clothes, be nude.")
    elif (i == 8):
        if (dif <= 1):
            tmp += (f"You may cover up whaterver you are currently wearing however"
                    f" you want.")
        elif (dif <= 3):
            tmp += (f"You may cover up whaterver you are currently wearing however"
                    f" you want in public. You must remove these cover clothes when"
                    f" you are in a location others can not acess.")
        else:
            tmp += (f"You may cover up whaterver you are currently wearing however"
                    f" you want in public. You must remove these cover clothes when"
                    f" are not directly being viewd by a person or camra.")
    elif (i == 9):
        tmp += (f"You may cover up whaterver you are currently wearing"
                f" with only {dif} clothes.")
    elif (i == 10):
        tmp += (f"You may not cover up what you are waring.")
    elif (i == 11):
        tmp += (f"Drink {dif} cups of {c(s10)}. You may not pee untill told.")
    elif (i == 12):
        tmp += (f"If someone tells you to do something you must do it."
                f" You do get {5-dif} vetos though.")
    elif (i == 13):
        if (dif <= 1):
            tmp += (f"Go to an isolated area where you do not have explicit privacy."
                    f" There should be a  very few people at this location."
                    f" It should be easy not to be seen IE: Late at night,"
                    f" an empty car park, a hiking trail")
        elif (dif <= 3):
            tmp += (f"Go to a public area where you do not have explicit privacy."
                    f" There should be a few people at this location. It should be 50/50"
                    f" not to be seen IE: A university after class hours, an office after hours,"
                    f" an active parking lot")
        else:
            tmp += (f"Go to a crowded area where you do not have explicit privacy."
                    f" There should be many people at this location. It should be"
                    f" impossible not to be seen. IE: A busy university while people"
                    f" are going to class, mall, store")
    elif (i == 14):
        if (dif <= 1):
            tmp += (f"Go to a location in public where you will have full privacy"
                    f" like a single user bathroom.")
        elif (dif <= 3):
            tmp += (f"Go to a public location where you will have partial privacy."
                    f" IE: A multi-user bathroom, a changing stall, lockers, a car in a lot")
        else:
            tmp += (f"Go to a location where it would be socialy ok to be nude / exposed"
                    f" IE: A locker room, your house / room, a bathroom. In this location"
                    f" you must make it so other people passing by can see in"
                    f" IE: Open the blinds / door / window")
    elif (i == 15):
        if (dif <= 1):
            tmp += (f"Go to a location where you will have full privacy")
        elif (dif >= 3):
            tmp += (f"Go to a location where you will have full privacy that is"
                    f" not a location you have been to this session")
    elif (i == 16):
        if (dif <= 1):
            tmp += (f"Untill you are told to stop, you must take photos of each"
                    f" task you are given that has you doing a physical activity")
        elif (dif <= 3):
            tmp += (f"Untill you are told to stop, you must record each"
                    f" task you are given that has you doing a physical activity")
        else:
            tmp += (f"Untill you are told to stop, you must stream each"
                    f" task you are given that has you doing a physical activity")
    elif (i == 17):
            tmp += (f"You may hide any identifying features in your recording"
                    f" / stream / photos")
    elif (i == 18):
        if (dif <= 1):
            tmp += (f"You must write a username you use online on your skin and show it"
                    f" on the recording / stream / photo")
        elif (dif <= 3):
            tmp += (f"You must write your {c(s11)} on your skin and show it"
                    f" on the recording / stream / photo")
        else:
            tmp += (f"You must show your face on the recording / stream / photo"
                    f" and talk if applicable")
    elif (i == 19):
        if (dif <= 1):
            tmp += (f"You must show your face on the recording / stream / photo"
                    f" and talk if applicable")
        elif (dif <= 3):
            tmp += (f"You must write your {c(s12)} on your skin and show it"
                    f" on the recording / stream / photo")
        else:
            tmp += (f"You must write your {c(s13)} on your skin and show it"
                    f" on the recording / stream / photo")
    elif (i == 20):
        if (dif <= 1):
            tmp += (f"Perform one of the following:\n"
                    f"- {c(s14)}\n- {c(s14)}")
        elif (dif <= 3):
            tmp += (f"Perform one of the following:\n"
                    f"- {c(s15)}\n- {c(s14)}")
        else:
            tmp += (f"Perform one of the following:\n"
                    f"- {c(s15)}\n- {c(s15)}")
    elif (i == 21):
        if (dif <= 1):
            tmp += (f"You may use the restroom")
        elif (dif >= 3):
            tmp += (f"You are still not allowed to use the restroom")
    elif (i == 22):
        tmp += (f"Fuck / stumulate your {c(s16)} at {dif * 50}bpm for {dif}m."
                f" Use a {c(s17)} to fuck yourself"
                f" The thing you are fucking yourself with should be on the"
                f" {dif}th highest setting or be the {dif}th largest you own."
                f" If it is your hand, use {dif} fingers")
    elif (i == 23):
        if (dif <= 2):
            tmp += (f"Hit / spank your {c(s5)} {dif} times"
                    f". The hit only counts if it leaves a red mark")
        else:
            tmp += (f"Hit / spank your {c(s6)} {dif} times"
                    f". The hit only counts if it leaves a red mark")
    elif (i == 24):
        tmp += (f"You must cum, but not by your primary sex organs.")
    elif (i == 25):
        tmp += (f"You must cum using your primary sex organs.")
    elif (i == 26):
        if (dif <= 2):
            tmp += (f"You must clean up any mess you have made with your clothes")
        else:
            tmp += (f"You must clean up any mess you have made with your mouth")
    elif (i == 27):
        tmp += (f"If you have recorded any of the last tasks you must"
                f" {c(s18)} for {dif} days")
    elif (i == 28):
        tmp += (f"If you have recorded any of the last tasks you must"
                f" {c(s19)} for {dif} days")
    elif (i == 29):
        tmp += (f"If you have recorded any of the last tasks you must"
                f" {c(s19)} and destroy any way to undo this.")
    elif (i == 30):
        tmp += (f"DEBUG")
    return tmp


def get_task(uuid: str, action: str = "reload") -> str:
    """
    Generates the next task

    :param uuid: The user id
    :param action: The action the user selected
    :return: The result to display
    """
    user = U.data[uuid]
    cont = check_ub(user)
    tmp = "> " + cont[1] + "\n\n"
    if (cont[0]):
        tmp += "> " + update_n(user, action) + "\n\n"
        if (action in "done fail err".split()):
            tmp += "\t'" + new_task(user) + "'\n"
        else:
            tmp += "\t'" + user.trace.split("|")[-1] + "'\n"
    U.update()
    return tmp

def new_task(user: Session) -> str:
    """
    Creates a new task for a user

    :param user: The user 
    :return: The result to display
    """
    tmp = ""
    options = list()
    if (user.n < 0):
        tmp +=  "This is a punishment: "
        options = user.punishments.split()
    else:
        options = user.kinks.split()
        if ((user.n + 1) >= user.u):
            options.extend(user.final_kinks.split())
    while (True):
        user.task_count += randint(2, 4)
        if (user.task_count not in TASKS):
            user.task_count = 1
        if (TASKS[user.task_count][0] in options):
            break
    task_dificulty = randint(1, user.difficulty)
    ftask = f"{format_task(user, task_dificulty)}"
    user.task_time = (time() + (randint(1, task_dificulty) * task_dificulty
                                * 60))
    tmp += ftask
    user.trace += f"|{tmp}"
    return tmp

def update_n(user: Session, action: str) -> str:
    """
    Updates the n value based off of what the user chose.

    :param user: The user 
    :param action: The action the user selected
    :return: The result to display
    """
    tmp = ""
    if (action == "done"):
        tmp += ("Your master is happy with your obedience."
               " They have another task for you: ")
        user.n += randint(1, user.difficulty)
    elif (action == "fail"):
        tmp += ("You have failed your master. Keep this up and you will be"
               " punished."
               " They have another task for you: ")
        user.n -= randint(0, user.difficulty)
    elif (action == "err"):
        is_pos = False
        if (user.n > user.n):
            is_pos = True
        tmp += ("Your master is suspicious but will let this slide."
               " Keep this up and you will be punished."
               " They have another task for you: ")
        user.n -= randint(0, user.difficulty)
        if (user.n < 0 and is_pos):
            user.n = 0
    else:
        tmp += ("Your master is still wating for you to finish your last task."
               " Take to long and you will be punished."
               " Your curent task is: ")
    return tmp

def check_ub(user: Session) -> Tuple[bool, str]:
    """
    Check the unlock or blackmail conditions

    :param user: The user 
    :return: The result to display and a bool to continue
    """
    tmp = ""
    cont = True
    if (user.n <= user.b):
        blackmail(user)
        cont = False
        tmp += ("Your master has tired of your disobedience and sent your" 
               " blackmail and moveed on to another slave. This session"
               " has ended.")
    elif (user.n >= user.u):
        unlock(user)
        cont = False
        tmp += ("Your master is satisfied with your service and" 
               " is done with you. This session"
               " has ended.")
        if (user.u_data):
            tmp += f" The code to your lock is: {user.u_data}"
    elif (user.time_end < time()):
        tmp += "Your session has hit its time limit."
        if (user.n <= 0):
            tmp += (" However you must finish any punishments your master"
                    " gives you before you may end this session.")
        else:
            tmp += (" Your master is satisfied with your service and" 
                    " is done with you. This session"
                    " has ended.")
            if (user.u_data):
                tmp += f" The code to your lock is: {user.u_data}"
            unlock(user)
            cont = False
    else:
        tmp += "Your master still wishes to use you. Your session is active."
    return (cont, tmp)

def blackmail(user: Session):
    """
    Blackmails a user and closes the session.

    :param user: The user to blackmail
    """
    user.state = "closed (blackmail)"
    with open(BMAIL_PATH, "a") as f:
        f.writelines([user.b_data])
    print(f"Sending {user.b_data} to {user.b_data}...")

def unlock(user: Session):
    """
    Unlocks a user and closes the session.

    :param user: The user to unlock
    """
    user.state = "closed (unlock)"


