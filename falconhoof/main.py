from cmd import Cmd
import random

from termcolor import colored


chaser = 0


class Room(object):

    completed = False

    def __init__(self, description):
        self.description = description

    def describe(self, line):
        print self.description



class OpenSesame(Room):

    def OPEN(self, line):
        if line == 'SESAME':
            self.completed = True

    def open(self, line):
        print "what's that sonny?"


class ButtonRoom(Room):

    def push(self, line):
        if line == 'button':
            self.completed = True
            return True
        return False


class PurpleButtonsRoom(Room):

    red_button = False
    green_button = False
    blue_button = False

    def push(self, line):
        if line == 'red button':
            self.red_button = not self.red_button
        elif line == 'green button':
            self.green_button = not self.green_button
        elif line == 'blue button':
            self.blue_button = not self.blue_button

        if (self.red_button, self.green_button, self.blue_button) == (True, False, True, ):
            self.completed = True
            return True
        return False


class JumpRoom(Room):

    def __init__(self, description, thing_to_jump):
        super(JumpRoom, self).__init__(description)
        self.thing_to_jump = thing_to_jump

    def jump(self, line):
        if line == self.thing_to_jump:
            self.completed = True
            return True
        return False


class HoldRoom(Room):

    def __init__(self, description, thing_to_jump):
        super(HoldRoom, self).__init__(description)
        self.thing_to_jump = thing_to_jump

    def hold(self, line):
        if line == self.thing_to_jump:
            self.completed = True
            return True
        return False


class CodeRoom(Room):
    def Hello(self, line):
        if line == 'World!':
            self.completed = True
            return True
        return False


class TPSRoom(Room):
    def attach(self, line):
        if line.lower() == 'a tps cover sheet':
            self.completed = True
            return True
        return False


class Game(Cmd):

    prompt = '> '

    index = 0
    chaserIndex = -2
    rooms = (
        CodeRoom(colored("print ", 'green') + colored("\"", 'blue') + "Hello World!" + colored("\"", 'blue')),
        TPSRoom("You didn't attach a TPS cover sheet to your TPS report"),
        ButtonRoom("A simple room with a button on a panel"),
        HoldRoom("Hold the line", 'the line'),
        JumpRoom("YOU SEE A CHASM, YOU CAN'T SEE THE OTHER SIDE!", 'the chasm'),
        PurpleButtonsRoom("Make " + colored('purple', 'magenta') + " from " + colored("red", "red") + ", " + colored("green", "green") + ", and " + colored("blue", "blue") + " buttons"),
        OpenSesame("I'm hard of hearing, but something something open sesame"),
    )

    @property
    def room(self):
        return self.rooms[self.index]

    def default(self, line):
        parts = line.split(" ", 1)

        if len(parts) > 1:
            command, rest = parts
        else:
            command, rest = parts[0], None

        action_method = getattr(self.room, command, None)

        if action_method:
            action_method(rest)

    def postcmd(self, stop, line):
        if self.room.completed:
            self.index += 1
            print 'Well done, you have completed the room!'
            if self.index < len(self.rooms):
                self.room.describe(None)

        self.chaserIndex += random.random() < 0.4

        if (self.chaserIndex == self.index -1):
            print 'Project manager is just behind you'
        elif (self.chaserIndex == self.index):
            print 'Project manager caught you, you have to work the weekend'
            return True

        if self.index >= len(self.rooms):
            print "You Win"
            return True


game = Game()
print colored("You have been kidnapped, you hear something behind you ... it's a project manager", 'grey')
game.room.describe(None)
game.cmdloop()