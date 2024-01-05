"""
A simple tui tester
"""

from session import Session, U
from task import get_task


kinks = [
    "error",
    "reset",
    "humiliation",
    "pain",
    "fuck",
    "bondage",
    "crossdressing",
    "humiliation",
    "hidden",
    "psudo",
    "exposed",
    "piss",
    "rape",
    "public",
    "protected",
    "private",
    "humiliation",
    "hidden",
    "psudo",
    "exposed",
    "humiliation",
    "piss",
    "fuck",
    "pain",
    "alt",
    "cum",
    "humiliation",
    "hidden",
    "psudo",
    "exposed",
]

pun = [
    "error"
]

# make a session
user = Session()
user.kinks = " ".join(kinks)
U.data[user.uuid] = user
U.update()
tmp = get_task(user.uuid, "done")
while (True):
    print(f"\n-----\n{tmp}")
    print(f"{user.n} / {user.u} / {user.b}")
    tmp = get_task(user.uuid, input("done|err|fail >"))
