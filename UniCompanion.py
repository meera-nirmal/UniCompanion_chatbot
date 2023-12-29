# Start
# Display a welcome message to the chatbot.
# Ask student to enter their credentials and store them in variables called:
# 'student_ID', 'first_name', 'user_age' and 'fave_colour'.
# Depending on the colour the student entered, display the societies the student would like.
# If the input for colour is not recognised:
    # give generic societies the student may enjoy joining.
# Depending on the age of the student, if the student is below the age of 25:
    # give a list of fresher events that they may enjoy taking part in.
# Otherwise:
    # give a list of other fresher, age-appropriate events that the student may enjoy.
# Ask the student to enter any other questions they would like to ask UniCompanion.
# If the student enters 'Q':
    # Display a parting message.
# Display personalised messages using elif statements for the remainder.
# Otherwise, if the input is not recognised:
    # Display a message redirecting the student towards student support.
# End

# Welcome message.
print('''
Welcome! This is UniCompanion. I am Bob and I am here to help you settle in at University. 
I hope I can help you navigate around this new journey of yours!
      
      Please enter your details below to get started: 
''')

student_ID = input("Please enter your Student ID: ").upper()
first_name = input("Please enter your first name: ").capitalize()
user_age = int(input("Please enter your age: "))
fave_colour = input("Please enter your favourite colour: ").capitalize()

print('''
Hi {}! I can see that your favourite colour is {}. Have to say, it is a nice colour!
Hmm, I think I have a few suggestions of what societies may be of interest to you based on your colour preference. :)   
'''.format(first_name, fave_colour))

if fave_colour == "Red":
    
    print("Since you like the colour red, I have a feeling that you may like the following: ")

    print('''
1. The Speed Dating Society
2. The Skydiving Society
3. Salsa Dancing Society
4. The Vampire Society
5. Cupid's Society
    ''')

elif fave_colour == "Orange":
    
    print("Since you like the colour orange, I have a feeling that you may like the following: ")

    print('''
1. The All Things Orange Food Society
2. The Sainsbury's Trip Society
3. The Orange Colour Appreciation Society
4. The Mingle & Orange Juice Sip Society
5. Fire Breathing Society
    ''')

elif fave_colour == "Yellow":

    print("Since you like the colour yellow, I have a feeling that you may like the following: ")

    print('''
1. The Suntan Society
2. The Sunrise Society
3. The Sunset Society
4. The Go Bananas Society
5. Pasta Eating Society
    ''')

elif fave_colour == "Green":

    print("Since you like the colour green, I have a feeling that you may like the following: ")

    print('''
1. The Hiking Society
2. The Mountaineering Club
3. The Fields & Farms Society
4. The Duke of Edinburgh Society
5. Woodland Walk Society
    ''')

elif fave_colour == "Blue":

    print("Since you like the colour blue, I have a feeling that you may like the following: ")

    print('''
1. The Dolphin & Whale Watching Club
2. The Windsurfing Society
3. The Deep Sea Treasure Diving Society
4. Aqua Aerobics (Including Aqua Zumba!)
5. The Swimming Club
    ''')

elif fave_colour == "Purple":

    print("Since you like the colour purple, I have a feeling that you may like the following: ")

    print('''
1. The Flower Exploration Society
2. The Meditation & Zen Society
3. The Tea Society
4. Knitting Society
5. The 'Me' Society
    ''')

elif fave_colour == "Pink":

    print("Since you like the colour purple, I have a feeling that you may like the following: ")

    print('''
1. The Barbie Club
2. The Dressing Up Society
3. The Studio Makeup Club
4. Dinner & Dance Society
5. Ballet Society
    ''')

else:

    print('''
Sorry, I don't recognise the input. However, the most popular societies are listed below:
1. Badminton Society
2. Tennis Society
3. Netball Society
4. Astronomy Society
5. Debate Society
    ''')

# Personalised events depending on the age of the student.
if user_age < 25:

    print("We also have LOTS of exciting fresher events lined up for you this coming week!")

    print('''
Monday - Bubble Foam Party
Tuesday - Techno Music Club Night
Wednesday - Free Pizza and Movie Night
Thursday - Pop Dance Music Club Night
Friday - Bowling Night
Weekend - Time to RELAX from all that partying! XD
    ''')

else:

    print("We have some interesting events lined up for you this coming week!")

    print('''
Monday - Book Reading & Wine Night
Tuesday - Techno Music Club Night
Wednesday - Free Pizza and Movie Night
Thursday - Pop Dance Music Club Night
Friday - Bowling Night
Weekend - Time to RELAX from all that partying! XD
    ''')

# Responses to frequently asked questions (FAQs).
question = input("Please enter any questions that you would like to ask me (otherwise, type Q to exit): ").capitalize()

if question == "Q":
    print(f"Goodbye. Have a great day {first_name}!")

elif question == "How is your day?":
    print("My day is going well, thank you. I hope yours is too :)")

elif question == "Where is the library?":
    print("The library for all subjects can be found opposite the Student Union.")

elif question == "What restaurants are there on campus?":
    print("We have a Wagamamas, Pret, Costa, Vegan Cafe and a Kebab Shop.")

else:
    print("Sorry, I am unable to help you in this instance. You can call student support at 012345678910.")