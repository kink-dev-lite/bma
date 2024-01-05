# Blackmail Academy 

This repo contains the code needed to run the Blackmail Academy game site and
this document contains the respective documentation for the project.

## UI Flow

The flow of the game is as such.

### 1. Session 

A user is asked to create a session or resume a session. A session object is
a json object that represents the users game state and is updated when the user
plays. The key parts of the session include:

- n: An int representing how good the player has been. If this drops negative
  punishments will be given
- b: A negative int representing that if equal to n, will trigger the blackmail
  sequence
- u: A positive int representing that if equal to n, will trigger the unlock
  sequence
- id: A uuid for the session
- b_data: The data to send to b_addr
- b_addr: The address to send the b_data to b_addr
- u_data: The unlock code
- time_start: The start of the session
- time_end: The time of the hard end of the session
- task_time: Time to wait before punishing for slowness by the user
- do_validation: Ask for validation media
- validation_code: The code required for validation
- kinks: List of kinks
- final_kinks: Kinks to add in on the final loop
- punishments: Kinks to add in on the final loop
- state: The session state
- difficulty: The session difficulty
- trace: A debug log
- task_count: The id of the current task

Once a state has been created, the session will start and the user will be
taken to the task loop screen.

### 1. Task Loop

The task loop screen will show the various tasks one at a time, looping when
done or ending when the u/b sequence has been started or max time has been hit.

- 01:reset reset from prior task loops
- 02:humiliation write on body
- 03:pain equip pain equipment
- 04:fuck equip fuck equipment
- 05:bondage equip partial bondage
- 06:crossdressing dress like the opposite gender
- 07:humiliation wear exposing clothes
- 08:hidden wear cover up clothes
- 09:psudo wear cover up clothes
- 10:exposed wear cover up clothes
- 11:piss drink fluids
- 12:rape you must do as told
- 13:public go somewhere physical
- 14:humiliation record / stream
- 15:hidden record / stream
- 16:psudo record / stream
- 17:exposed record / stream
- 18:humiliation do humiliation act
- 19:piss do piss act
- 20:fuck do fuck act
- 21:pain do pain act
- 22:alt do alt cum act
- 23:cum do cum act
- 24:humiliation cleanup
- 25:humiliation post
- 26:hidden post
- 27:psudo post
- 28:exposed post

At each of these tasks the user will have three options to move forward:

- Finished: The user did all required parts (add to n)
- Failed: The user did not do all required parts (subtract from n)
- Error: The user can not do the task or some error has happened (subtract, but
  do not drop below b, send a log message)

## 3. Unlock / Blackmail Sequence

The game ends when u or b is hit. If the time is past the max time and n is
positive the unlock sequence starts.

### Unlock Sequence

The user will be given any provided u_data

### Blackmail Sequence

The user will have the information in b_data posted to b_addr.

## 4. Wiki / Discord

At any time the user can view the wiki / discord links.

