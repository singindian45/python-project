"""
All the functions for the pokemon game are stored here
"""

import sys
import time


def printf(sentence: str):
    # Print one character at a time
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    print()


def inputf(sentence: str):
    # Print one character at a time and take in the output
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)

    choice = input()
    return choice


def dialogue(dialogues: dict):
    for speaker in dialogues:
        space = 13
        if len(speaker) > space:
            space = len(speaker)
        dialogue = dialogues[speaker]

        if isinstance(dialogue, str):
            printf(f"{speaker.ljust(space)}: {dialogue}")
            print()
        elif isinstance(dialogue, list):
            printf(f"{speaker.ljust(space)}: {dialogue[0]}")
            for line in dialogue[1:]:
                printf(" " * (space + 2) + f"{line}")
            print()


def y_or_n(choice: str):
    if choice.lower().strip() == "y" or choice.lower().strip() == "yes" or choice == "":
        return True
    else:
        return False


def confirm(question: str):
    question_response = inputf(question)
    choice = inputf(f"Proceed with '{question_response}'?[Y/n]\t")
    if (
        choice.lower().strip() != "y"
        and choice.lower().strip() != "yes"
        and choice.lower().strip() != ""
    ):
        confirm_decision = inputf(f"Do you want to change your choice?[Y/n]\t")
        if (
            confirm_decision.lower().strip() == "y"
            or confirm_decision.lower().strip() == "yes"
            or confirm_decision.lower().strip() == ""
        ):
            return confirm(question)
    else:
        return question_response


def event_choice(events: dict):
    count = len(events)
    choices = [i for i in range(count)]
    for n, event in zip(choices, events.keys()):
        printf(f"[{n}] {event}")

    options = "|".join(
        str(n) for n in choices
    )  # just a string showing possible options
    choice = inputf(f"Enter your choice:[{options}]\t").lower().strip()

    def check_instance(event):
        if isinstance(event, str):
            printf(f"{event}")
        elif isinstance(event, dict):
            event_choice(event)
        elif isinstance(event, list):
            for inner_event in event:
                check_instance(inner_event)

    if choice.isnumeric():
        if int(choice) in choices:
            decision = list(events.keys())[int(choice)]
            check_instance(events[decision])

        else:
            printf("Please choose a valid option.")
            event_choice(events)

    else:
        printf("That is not a valid choice! Try again with a number.")
        event_choice(events)


def game_save(Trainer):
    # to be completed
    with open("savefile.txt", "w") as save:
        save.write()
