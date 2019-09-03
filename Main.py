from random import *#For potential stretch challenge

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


def verb_func():
    for j in range (5):
        verbsInputted = input("Enter some verbs: ")
        verbs.append(verbsInputted)
        j+=1


def adj_func():
    for k in range (5):
        adjInputted = input("Enter some descriptive words: ")
        adjectives.append(adjInputted)
        k+=1


def adv_func():
    for l in range (5):
        adverbsInputted = input("Enter some adverbs: ")
        adverbs.append(adverbsInputted)
        l+=1

noun_func()
#adj_func()
#adv_func()
#verb_func()

print('''\nO say can you see, by the dawn's early ''' + nouns[0] + ''',
What so proudly we hail'd at the twiglight's last gleaming,
Whose broad stripes and bright ''' + nouns[1] + ''' through the perilous fight
O'er the ramparts we watch'd we so gallantly streaming?
And the rocket's red glare, the''' + nouns[2] + '''bursting in air,
Gave proof through the night that our ''' + nouns[3] + ''' was still there,
O say does that star-spangled banner yet wave
O'ver the land of the free and the home of the brave?\n
On the shore dimly seen through the mists of the deep
Where the foe's haughty host in dread silence reposes,
What is that which the ''' + nouns[4] + ''', o'er the towering steep,
As it fitfully blows, half conceals, half discloses?
Now it catches the gleam of the morning's first beam,
In full glory reflected now shines in the stream,
'Tis the star-spangled ''' + nouns[5] + ''' - O long may it wave
O'er the land of the free and the home of the brave!\n
And where is that band who so vauntingly swore,
That the havoc of war and the battle's confusion
A home and a ''' + nouns[6] + ''' should leave us no more?
Their blood has wash'd out their foul footstep's pollution.
No refuge could save the hireling and ''' + nouns[7] + '''
From the terror of flight or the gloom of the grave,
And the star-spangled banner in triumph doth wave
O'er the land of the land of the free and the home of the brave.\n
O thus be it ever when freemen shall stand
Between their lov'd home and the ''' + nouns[8] + ''' desolation!
Blest with vict'ry and peace may the the heav'n rescued land
Praised the power that hath made and preserv'd us a ''' + nouns[9] +'''!
Then conquer we must, when out cause is just,
And this be our motto - "In God is our trust,"
And the star-spangled banner in triumph shall wave
O'ver the land of the free and the home of the brave.\n''')
