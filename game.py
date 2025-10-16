#!/usr/bin/python3
# -- coding: utf-8 --

# 12/10/25

__author__ = 'Clara Sedes'

from map import g_rooms
from player import *
from items import *
from gameparser import *

# Start game at the reception
g_current_room = g_rooms["Reception"]


def list_of_items(p_items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([g_item_pen, g_item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([g_item_identity_card])
    'identity card'

    >>> list_of_items([])
    ''

    >>> list_of_items([g_item_money, g_item_handbook, g_item_laptop])
    'money, a student handbook, laptop'

    """

    return ', '.join(l_item["name"] for l_item in p_items)


def print_room_items(p_room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(g_rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(g_rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(g_rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if list_of_items(p_room["items"]):
        print('There is', list_of_items(p_room["items"]), 'here.')
        print()


def print_inventory_items(p_items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(g_inventory)
    You have identity card, laptop, money.
    <BLANKLINE>

    """
    print('You have',  list_of_items(p_items) + '.')
    print()


def print_room(p_room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(g_rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(g_rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(g_rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(p_room["name"].upper())
    print()
    # Display room description
    print(p_room["description"])
    print()
    print_room_items(p_room)


def exit_leads_to(p_exits, p_direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(g_rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(g_rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(g_rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return g_rooms[p_exits[p_direction]]["name"]


def print_exit(p_direction, p_leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + p_direction.upper() + " to " + p_leads_to + ".")


def print_menu(p_exits, p_room_items, p_inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for l_direction in p_exits:
        # Print the exit name and where it leads to
        print_exit(l_direction, exit_leads_to(p_exits, l_direction))

    for l_item in p_room_items:
        print('TAKE', l_item["id"].upper(), 'to take', l_item["name"] + '.')

    for l_item in p_inv_items:
        print('DROP', l_item["id"].upper(), 'to drop your', l_item["name"] + '.')

    print("What do you want to do?")


def is_valid_exit(p_exits, p_chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(g_rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(g_rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(g_rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(g_rooms["Parking"]["exits"], "east")
    True
    """
    return p_chosen_exit in p_exits


def execute_go(p_direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global g_current_room

    l_possible_directions = g_current_room["exits"]
    if is_valid_exit(l_possible_directions, p_direction):
        # Update the value of g_current_room by assigning move's return value to it
        g_current_room = move(l_possible_directions, p_direction)
        return g_current_room["name"]
    else:
        return "You cannot go there."


def execute_take(p_item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    l_found_item = None
    for l_item in g_current_room["items"]:
        if l_item["id"] == p_item_id:
            l_found_item = l_item
            g_current_room["items"].remove(l_found_item)
            g_inventory.append(l_found_item)
            break
    if l_found_item is None:
        print("You cannot take that.")


def execute_drop(p_item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    l_found_item = None
    for l_item in g_inventory:
        if l_item["id"] == p_item_id:
            l_found_item = l_item
            g_inventory.remove(l_found_item)
            # print('Inventory:', g_inventory)
            g_current_room["items"].append(l_found_item)
            # print('Current room items:', g_current_room["items"])
            break
    if l_found_item is None:
        print("You cannot drop that.")
    

def execute_command(p_command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(p_command):
        return

    if p_command[0] == "go":
        if len(p_command) > 1:
            execute_go(p_command[1])
        else:
            print("Go where?")

    elif p_command[0] == "take":
        if len(p_command) > 1:
            execute_take(p_command[1])
        else:
            print("Take what?")

    elif p_command[0] == "drop":
        if len(p_command) > 1:
            execute_drop(p_command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(p_exits, p_room_items, p_inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(p_exits, p_room_items, p_inv_items)

    # Read player's input
    l_user_input = input("> ")

    # Normalise the input
    l_normalised_user_input = normalise_input(l_user_input)
    return l_normalised_user_input


def move(p_exits, p_direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(g_rooms["Reception"]["exits"], "south") == g_rooms["Admins"]
    True
    >>> move(g_rooms["Reception"]["exits"], "east") == g_rooms["Tutor"]
    True
    >>> move(g_rooms["Reception"]["exits"], "west") == g_rooms["Office"]
    False
    """

    # Next room to go to
    return g_rooms[p_exits[p_direction]]


def main():
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(g_current_room)
        print_inventory_items(g_inventory)

        # Show the menu with possible actions and ask the player
        l_command = menu(g_current_room["exits"], g_current_room["items"], g_inventory)

        # Execute the player's command
        execute_command(l_command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

