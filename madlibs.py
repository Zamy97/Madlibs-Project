# #This is the madlibs project that I have to create where the users will type in words to write their story.

your_name = input("Enter your name: ")
continuous_verb = input("Enter a continus verb: ")
scared_not_scared = input("Are you scared or not scared: ")
kitchen_item = input("Enter a kitchen equipment name:")
country_name = input("Enter a country name: ")
celebraity = input("Enter a celebraity name: ")
he_or_she = input("are you he or she? ")


story_madlibs = your_name + "loves everything about " +  continuous_verb + he_or_she +  " runs evryday to stay healthy." + he_or_she + scared_not_scared  + " of lions at all. " + he_or_she + " loves everything about " + kitchen_item + he_or_she " wants to go to" + country_name + " to meet " + celebraity + "in person". "overall " + he_or_she + "is really happy with " + he_or_she +  " life, but deep down inside" + he_or_she + "will be upset if" + he_or_she + "doesn't get to meet " + celebraity + "in person"

print(story_madlibs)

# If this doesn't work then try the following to see if that works.

first_Verb = input("Enter a Verb: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a Celebrity Name: ")
country = input("Enter a Country Name: ")
your_name = input("Enter your name: ")

print( your_name +  " is good at " + first_Verb )
print("She loves everything about " + plural_noun )
print("She kinda wants to go to " + country + " to meet " + celebrity)
