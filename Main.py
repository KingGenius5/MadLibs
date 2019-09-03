#color formatting for output in the terminal - just type in 'pip3 install termcolor' and you're set
from termcolor import colored

#these empty lists will be appended with the user input later on for each part of speech
nouns = []
verbs = []
adjectives = []
adverbs = []

#Here's the formatting to make the output look a little cleaner and more presentable
print(70*"*")
print(70*"-")
print(23*" " + "WELCOME TO " + colored('MADLIBS!!!','yellow',attrs=['underline','blink','bold']))
print(70*"*")

#Little additions that make the UX a bit more enjoyable
users_name = input("\nBut how rude, I didn't get your name...")
print("Nice to meet you " + colored(users_name,'blue') + ", shall we begin?")
print('''\nBelow is the full version of the American National anthem. 
At the end of this game, that will no longer be the case.\n''')

print(11*" " + colored("The Star-Spangled Banner",attrs=['underline']) + 20*" ")
print('''          ============;===========;()
                               # # # #::::::
                               # # # #::::::
                               # # # #::::::
                               # # # #::::::
                               # # # # # # #
                               # # # # # # #
                               # # # # # # #
                               # # # # # # #
                               # # # # # # #
                               # # # # # # #''')

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

def noun_func():
    for i in range (10):
        nounsInputted = input("Enter a(n) nouns: ")
        nouns.append(nounsInputted)
        i+=1
        if(nounsInputted.isalpha() == False):#from Python documentation, returns true if all characters in the string are alphabetical.
            #So if we set it to false, we can weed out integers and symbols as invalid input.
            print("Invalid input!!! You want to try entering some real nouns next time?")
            break

def verb_func():
    for j in range (8):
        verbsInputted = input("Enter a(n) verb: ")
        verbs.append(verbsInputted)
        j+=1
        if(verbsInputted.isalpha() == False):
            print("Invalid input!!! You want to try entering some real verbs next time?")
            break

def adj_func():
    for k in range (8):
        adjInputted = input("Enter a(n) adjective: ")
        adjectives.append(adjInputted)
        k+=1
        if(adjInputted.isalpha() == False):
            print("Invalid input!!! You want to try entering some real adjectives next time?")
            break

def adv_func():
    for l in range (5):
        adverbsInputted = input("Enter a(n) adverb: ")
        adverbs.append(adverbsInputted)
        l+=1
        if(adverbsInputted.isalpha() == False):
            print("Invalid input!!! You want to try entering some real adverbs next time?")
            break

#calling functions
noun_func()
verb_func()
adj_func()
adv_func()

#Display the final story to the user with formatting and color
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

#Site where I got both wonderful flag artwork from: https://www.oocities.org/spunk1111/flag.htm
print('''
     (_)
    <___>
     | |______
     | |* * * )
     | | * * (_________
     | |* * * |* *|####)
     | | * * *| * |   (________________
     | |* * * |* *|####|##############|
     | | * * *| * |    |              |
     | |* * * |* *|####|##############|
     | |~~~~~~| * |    |              |
     | |######|* *|####|##############|
     | |      |~~~'    |              |
     | |######|########|##############|
     | |      |        |              |
     | |######|########|##############|
     | |~~~~~~|        |              |
     | |      |########|##############|
     | |      '~~~~~~~~|              |
     | |               |##############|
     | |               '~~~~~~~~~~~~~~~
     | |
     | |
     | |
     ''')
