"""
Represents the session object
"""

from dataclasses import asdict, dataclass, field
from time import time
from typing import Dict, List
from pathlib import Path
from random import choices
from json import dump, load

# List of words that can be used in validation_code
VALIDATION_WORDS: List[str] = """
By Tuesday though she was feeling well enough and starting to miss Bill's touch so she tried snuggling up to him Kissing his neck slowly running her hands along his body He didn't react nearly as much as Becky wanted him to but he didn't pull away For a night or two she tried to get him to show some interest even going so far as to buy a new nightie and wear it for him Of course it was nothing like the clothes Charlotte or Peter had made her wear but it was soft pale pink and frilly and see through enough that her dark nipples and neatly trimmed bush could just be seen through it
""".split()

# Location of saved sessions
DATA_PATH = Path("./data.json")

@dataclass
class Session():
    """
    The session object in python form.

    :param n: An int representing how good the player has been. If this drops negative
      punishments will be given
    :param b: A negative int representing that if equal to n, will trigger the blackmail
      sequence
    :param u: A positive int representing that if equal to n, will trigger the unlock
      sequence
    :param uuid: A uuid for the session
    :param b_data: The data to send to b_addr
    :param b_addr: The address to send the b_data to b_addr
    :param u_data: The unlock code
    :param time_start: The start of the session
    :param time_end: The time of the hard end of the session
    :param task_time: Time to wait before punishing for slowness by the user
    :param do_validation: Ask for validation media
    :param validation_code: The code required for validation
    :param kinks: List of kinks
    :param final_kinks: Kinks to add in on the final loop
    :param punishments: Kinks to add in on the final loop
    :param state: The session state
    :param difficulty: The session difficulty
    :param trace: A debug log
    :param task_count: The curent task id
    :param hard_limits: The users hard limits
    """
    n: int = 1
    b: int = -15
    u: int = 30
    uuid: str = field(default_factory=lambda :str(time()))
    b_data: str = ""
    b_addr: str = ""
    u_data: str = ""
    time_start: float = field(default_factory=lambda :time())
    time_end: float = field(default_factory=lambda :time() + 60*60)
    task_time: float = field(default_factory=lambda :time() + 60*4)
    do_validation: bool = False
    validation_code: str = field(default_factory=lambda :"-".join(choices(VALIDATION_WORDS, k=5)))
    kinks: str = "debug"
    final_kinks: str = "cum"
    punishments: str = "debug"
    state: str = "open"
    difficulty: int = 2
    trace: str = "Pledge your obedience to your master"
    task_count: int = 1
    hard_limits: str = "No Hard Limits"


@dataclass
class Users:
    """
    Represents the active users in the game.

    :param data: A list of session objects
    """
    data: Dict[str, Session] = field(default_factory=dict)

    def __post_init__(self):
        with open(DATA_PATH) as f:
            tmp = load(f)
            for x in tmp:
                s = Session(**x) 
                self.data[s.uuid] = s


    def update(self):
        """
        Updates the session record on disk
        """
        tmp = list()
        for x in self.data:
            tmp.append(asdict(self.data[x]))
        with open(DATA_PATH, "w") as f:
            dump(tmp, f)

# Auto load in users
U = Users()
