story = '''
A vacation is when you take a trip to some {} place with your {} family.
Usually you go to some place that is near a/an {} or up on a/an {}.
A good vacation place is one where you can ride {} or play {} or go hunting for {}.
I like to spend my time {} or {}. 
When parents go on a vacation, they spend their time eating three {} a day, and fathers play golf, and mothers sit around {}.
Last summer, my little brother fell in a/an {} and got poison {} all over his {}.
My family is going to go to (the) {}, and I will practice {}.
Parents need vacations more than kids because parents are always very {} and because they have to work {} hours every day all year making enough {} to pay for the vacation.
'''

adjective1 = input("Tell me an adjective, and press enter. ")
adjective2 = input("Tell me another adjective, and press enter. ")
noun1 = input("Tell me a noun, and press enter. ")
noun2 = input("Tell me another noun, and press enter. ")
noun3 = input("Tell me a plural noun, and press enter. ")
game1 = input("Tell me a game, and press enter. ")
noun4 = input("Tell me another plural noun, and press enter. ")
verb1 = input("Tell me a verb (ending in -ing), and press enter. ")
verb2 = input("Tell me another verb (ending in -ing), and press enter. ")
noun5 = input("Tell me another plural noun, and press enter. ")
verb3 = input("Tell me another verb (ending in -ing), and press enter. ")
noun6 = input("Tell me another noun, and press enter. ")
plant1 = input("Tell me a type of plant, and press enter. ")
part1 = input("Tell me a part of the body, and press enter. ")
place1 = input("Tell me a name of a place, and press enter. ")
verb4 = input("Tell me another verb (ending in -ing), and press enter. ")
adjective3 = input("Tell me another adjective, and press enter. ")
number1 = input("Tell me a number, and press enter. ")
noun7 = input("Tell me another plural noun, and press enter. ")

mad_lib = story.format(adjective1, adjective2, noun1, noun2, noun3, game1, noun4, verb1, verb2, noun5, verb3, noun6, plant1, part1, place1, verb4, adjective3, number1, noun7)
print(mad_lib)