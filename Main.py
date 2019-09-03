from random import *#For potential stretch challenge

#color formatting for output in the terminal - just type in 'pip3 install termcolor' and you're set
from termcolor import colored

nouns = []
verbs = []
adjectives = []
adverbs = []

#The original version of The Star Spangled Banner before it gets 'MadLibbed'
print('''\nO say can you see, by the dawn's early light,
What so proudly we hail'd at the twiglight's last gleaming,
Whose broad stripes and bright stars through the perilous fight
O'er the ramparts we watch'd we so gallantly streaming?
And the rocket's red glare, the bomb bursting in air,
Gave proof through the night that our flag was still there,
O say does that star-spangled banner yet wave
O'ver the land of the free and the home of the brave?\n
On the shore dimly seen through the mists of the deep
Where the foe's haughty host in dread silence reposes,
What is that which the breeze, o'er the towering steep,
As it fitfully blows, half conceals, half discloses?
Now it catches the gleam of the morning's first beam,
In full glory reflected now shines in the stream,
'Tis the star-spangled banner - O long may it wave
O'er the land of the free and the home of the brave!\n
And where is that band who so vauntingly swore,
That the havoc of war and the battle's confusion
A home and a Country should leave us no more?
Their blood has wash'd out their foul footstep's pollution.
No refuge could save the hireling and slave
From the terror of flight or the gloom of the grave,
And the star-spangled banner in triumph doth wave
O'er the land of the land of the free and the home of the brave.\n
O thus be it ever when freemen shall stand
Between their lov'd home and the war's desolation!
Blest with vict'ry and peace may the the heav'n rescued land
Praised the power that hath made and preserv'd us a nation!
Then conquer we must, when out cause is just,
And this be our motto - "In God is our trust,"
And the star-spangled banner in triumph shall wave
O'ver the land of the free and the home of the brave.\n''')

def noun_func():#will come up with better function names
    for i in range (10):
        nounsInputted = input("Enter some nouns for this MadLibs exercise: ")
        nouns.append(nounsInputted)
        i+=1
        if(nounsInputted.isalpha() == False):
            print("Invalid input!!! You want to try entering some real nouns?")
            break


def verb_func():
    for j in range (8):
        verbsInputted = input("Enter some verbs: ")
        verbs.append(verbsInputted)
        j+=1
        if(verbsInputted.isalpha() == False):
            print("Invalid input!!! You want to try entering some real verbs?")
            break


def adj_func():
    for k in range (8):
        adjInputted = input("Enter some descriptive words: ")
        adjectives.append(adjInputted)
        k+=1
        if(adjInputted.isalpha() == False):
            print("Invalid input!!! You want to try entering some real adjectives?")
            break


def adv_func():
    for l in range (5):
        adverbsInputted = input("Enter some adverbs: ")
        adverbs.append(adverbsInputted)
        l+=1
        if(adverbsInputted.isalpha() == False):
            print("Invalid input!!! You want to try entering some real adverbs?")
            break

noun_func()
adj_func()
adv_func()
verb_func()

print('''\nO say can you see, by the dawn's early ''' + colored(nouns[0],'red') + ''',
What so ''' + colored(adverbs[0],'green') + ''' we hail'd at the twiglight's last gleaming,
Whose ''' + colored(adjectives[0],'magenta') + ''' stripes and bright ''' + colored(nouns[1],'red') + ''' through the ''' + colored(adjectives[1],'magenta') + ''' fight
O'er the ramparts we watch'd we so ''' + colored(adverbs[1],'green') + ''' streaming?
And the rocket's ''' + colored(adjectives[2],'magenta') + ''' glare, the ''' + colored(nouns[2],'red') + ''' bursting in air,
Gave proof through the night that our ''' + colored(nouns[3],'red') + ''' was still there,
O say does that star-spangled banner yet ''' + colored(verbs[0],'cyan') + '''
O'ver the land of the ''' + colored(adjectives[3],'magenta') + ''' and the home of the brave?\n
On the shore ''' + colored(adverbs[2],'green') + ''' seen through the mists of the deep
Where the foe's haughty host in ''' + colored(adjectives[4],'magenta') + ''' silence ''' + colored(verbs[1],'cyan') + ''',
What is that which the ''' + colored(nouns[4],'red') + ''', o'er the towering steep,
As it ''' + colored(adverbs[3],'green') + ''' blows, half conceals, half discloses?
Now it ''' + colored(verbs[2],'cyan') +  ''' the gleam of the morning's first beam,
In full glory reflected now shines in the stream,
'Tis the star-spangled ''' + colored(nouns[5],'red') + ''' - O long may it ''' + colored(verbs[3],'cyan') + ''' 
O'er the land of the free and the home of the brave!\n
And where is that band who so ''' + colored(adverbs[4],'green') + ''' swore,
That the havoc of war and the battle's confusion
A home and a ''' + colored(nouns[6],'red') + ''' should ''' + colored(verbs[4],'cyan') + ''' us no more?
Their blood has ''' + colored(verbs[5],'cyan') + ''' out their foul footstep's pollution.
No refuge could ''' + colored(verbs[6],'cyan') + ''' the hireling and ''' + colored(nouns[7],'red') + '''
From the terror of flight or the ''' + colored(adjectives[5],'magenta') + ''' of the grave,
And the star-spangled banner in triumph doth wave
O'er the land of the land of the free and the home of the brave.\n
O thus be it ever when freemen shall stand
Between their lov'd home and the ''' + colored(nouns[8],'red') + ''' desolation!
Blest with vict'ry and peace may the the heav'n rescued land
Praised the power that hath ''' + colored(verbs[7],'cyan') + ''' and preserv'd us a ''' + colored(nouns[9],'red') +'''!
Then conquer we must, when out cause is ''' + colored(adjectives[6],'magenta') + ''',
And this be our motto - "In God is our trust,"
And the ''' + colored(adjectives[7],'magenta') + ''' banner in triumph shall wave
O'ver the land of the free and the home of the brave.\n''')
