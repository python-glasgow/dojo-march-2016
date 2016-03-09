# -*- coding: utf-8 -*-
import random

class AdventureStory(object):
    story = [
#0
{'desc': 'You are on the corner looking north along west Nile street and you see a lit building on the left and pizza hut behind you.',
  'options':[
    {'text': 'Do you approach the building', 'next_id': 1},
    {'text': 'Go for Pizza', 'next_id': 998},
    {'text': 'Speak to passer by', 'next_id': 2}
    ]
},
#1
{'desc': 'At the building you see people sitting outside, beyond the people on the left is a disabled entrance and in front of you there is a revolving door. In the lobby there is a man behind a desk.',
  'options':[
    {'text': 'Enter Disabled door', 'next_id': 3},
    {'text': 'Enter revolving door', 'next_id': 3},
    {'text': 'Speak to people', 'next_id': 4},
    {'text': 'Go shopping across the road', 'next_id': 998},
    {'text': 'Carry on up the street', 'next_id': 5}
    ]
},

# 2
{'desc': 'The passer by says. "£5 for a useful surprise?"',
  'options':[
    {'text': 'Ignore the man', 'next_id': 1},
    {'text': 'Haggle with the stranger', 'next_id': 999},
    {'text': 'Give him a fiver', 'next_id': 6},
    ]
},


# 3
{'desc': 'You are stopped by the man behind the desk and he questions you intentions',
  'options':[
    {'text': 'You apologise and leave the building', 'next_id': 1},
    {'text': 'You confront the man agressively', 'next_id': 7},
    {'text': 'You attempt to talk your way past the man', 'next_id': 8},
    {'text': 'Ignore the man and walk past him', 'next_id': 8},
    ]
},

# 4
{'desc': 'They ask "Are you on the night shift?"',
  'options':[
    {'text': 'Say Yes', 'next_id': 10},
    {'text': 'Say No', 'next_id': 9},
    {'text': 'Ignore them', 'next_id': 9},
    {'text': 'Ignore the man and walk past him', 'next_id': 8},
    ]
},

# 5
{'desc': 'You spot a back alley to the left with a half open garage door.',
  'options':[
    {'text': 'You keep walking', 'next_id': 998},
    {'text': 'You enter the door', 'next_id': 11},
    ]
},

# 6
{'desc': 'He gives you a knife and you are on the corner looking north along west Nile street and you see a lit building on the left and pizza hut behind you.',
  'options':[
    {'text': 'Do you approach the building', 'next_id': 1},
    {'text': 'Go for Pizza', 'next_id': 998}
    ]
},

# 7
{'desc': 'He gives you a knife and you are on the corner looking north along west Nile street and you see a lit building on the left and pizza hut behind you.',
  'options':[
    {'text': 'Do you approach the building', 'next_id': 1},
    {'text': 'Go for Pizza', 'next_id': 998}
    ]
},

# 8
{'desc': 'You realise he is a large man as he towers over you.',
  'options':[
    {'text': 'RUN', 'next_id': 998},
    {'text': 'Apologise and leave the building', 'next_id': 998},
    {'text': 'You boot him in the crown jewels', 'next_id': 999},
    {'text': 'You try to bluff your way past him by mentioning a man called Fred', 'next_id': 12},
    {'text': 'I am going to Fanduel', 'next_id': 999},
    ]
}
]

    level=0
    def show_current_level(self):
        print ''
        self.show_room_description(self.story[self.level]['desc'])
        print ''
        self.show_room_options(self.story[self.level]['options'])
        print ''
        self.choose_option()

    def show_room_description(self, desc):
        print desc

    def show_room_options(self, options):
        for index, val in enumerate(options):
            print "{option}: {text}".format(option=index, text=val['text'])

    def choose_option(self):
        option = raw_input('Choose an option: ')
        self.handle_option(int(option))

    def handle_option(self, option):
        next_room = self.story[self.level]['options'][option]['next_id']

        if next_room == 999:
            self.death_list(self.level)
        elif next_room == 998:
            print "You went for some sweet pizza, BYE"
        else:
            self.level = next_room
            self.show_current_level()

    def death_list(self, room):
        death_list = [
            'this', 'random mongoose attack', 'celebrity; Peter Andrea found you and made you their pet. After years in captivity you you tied yourself in to a knot and killed your self', 'stood on by a .net developer', 'a java engineer picked you up and threw you under a car.', 'chainsaw!! rrrrrrrrrrrrr!!!', 'eaten by a badger', 'bottled by a ned', 'Cliff hanger!!'
        ]
        print "You Died in room %s death by %s" % (room, random.choice(death_list))


story = AdventureStory()
story.show_current_level()
