# angelo locarini
# 17/04/2024

#print("hello world!")

#2-3. Personal Message: 
#Use a variable to represent a person’s name, 
#and print a message to that person. 
#Your message should be simple,such as, 
#“Hello Eric, would you like to learn some Python today?”


'''
name: str = "Giovanni"
massage: str = f"{name}, ti va di imparare un po di python insieme?"
print(massage)

--list


#2-4. Name Cases: Use a variable to represent a person’s name,
#and then print that person’s name in lowercase, uppercase, and title case.

#name: str = "AnGeLo"
#print(name.upper())
#print(name.lower())
#print(name.title())





#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: Albert Einstein once said, 
#“A person who never made a mistake never tried anything new.”
'''
'''
name: str = "Sora"
print(name)
quote: str = f" once said may your heart be your guiding key"
print(quote)
massage: str = f"{name},{quote}"
print(massage)


Famous Quote 2: Repeat Exercise 2-5, but this time, 
represent the famous person’s name using a variable called famous_person. 
Then compose your message and represent it with a new variable called message. Print your message. 
'''
'''
famous_person: str = "Sora"
print(famous_person)
quote: str = f" once said may your heart be your guiding key"
print(quote)
massage: str = f"{famous_person},{quote}"
print(massage)
'''

'''
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix()
method to display the filename without the file extension, like some file browsers do.


filename: str = "python_notes.txt"
print(filename.removesuffix(".txt"))


3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.

'''
'''
names: list = ["ancielo", "gabriele", "giuseppe"]
print(names)
print(names [0])
print(names [1])
print(names [2])

3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing 
each person’s name, print a message to them. 
The text of each message should be the same, 
but each message should be personalized with the person’s name.

print("ciao", names[0], "spero ti venga un colpo")
print("ciao", names[1], "spero ti venga un colpo")
print("ciao", names[2], "spero ti venga un colpo")
'''
'''
3-3. Your Own List: Think of your favorite mode of transportation, 
such as a motorcycle or a car, and make a list that stores several examples.
Use your list to print a series of statements about these items, such as 
“I would like to own a Honda motorcycle.”

names: list = ["Rx7", "camioncino dei gelati", "carroarmato"]
print(names)

print(names [1])
print("vorrei guidare una", names [0], "in un circuito")
print("vorrei guidare un", names [1], "per rubare tutto il gelato")
print("vorrei guidare un", names [2], "per schiacciare le auto in autostrada")


3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner.

'''
'''
names: list = ["Walter White", "Caparezza", "Christian de Sica"]
print(names)

print(names [1])
print("hey", names [0], "mi raccomando porta la droga")
print( names [1], "Ci vediamo fuori dal tunnel alle 22")
print( names [2], "facciamo un fossato")
'''
'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
'''
'''
names: list = ["Walter White", "Caparezza", "Christian de Sica"]
print(f"ciao {names}, siete invitati a cena")
print(f"ciao a tutti, {names[:1]} non verrà sta sera")
'''
'''
3-6. More Guests: You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.

names: list = ["Walter White", "Caparezza", "Christian de Sica"]
print( f"ragazzi {names[0]} {names[1]} {names[2]}) questa sera ci saranno altre 3 persone con noi")

names.insert(0, "Paolo Bonolis")
names.insert(2, "Luca Laurenti")
names.append( "Maria Sofia Federico")
print(names)

print( f"{names[0]} sei invitato a cena questa sera")
print( f"{names[2]} sei invitato a cena questa sera")
print( f" sei invitata a cena questa sera")
'''
'''
3-7. Shrinking Guest List: You just found out that your new dinner 
table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying 
that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know 
you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.
'''
'''
names: list = ["Paolo Bonolis", "Walter White", "Luca Laurenti", "Caparezza", "Christian de Sica", "Maria Sofia Federico"]

print( f"ragazzi questa sera c'è stato un piccolo problema quindi {names[-1]}, {names[3]}, {names[4]}, {names[-5]} non potete più venire ")
names.pop(-1)
names.pop(3)
names.pop(2)
print(names)
''

3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly;
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing 
the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again.
Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. 
Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
'''
'''
luoghi: list = ["Albero Bello", "Vicolo Di Napoli", "Doganella", "Valle d'Aosta", "Garbatella"]
print(sorted(luoghi))
print(luoghi)
print(sorted(luoghi)[::-1])
print(luoghi)
luoghi.reverse()
print(luoghi)
luoghi.reverse()
print(luoghi)
luoghi.sort()
print(luoghi)
luoghi.sort(reverse=True
print(luoghi)
'''
'''
3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.
'''
'''
names: list = ["Walter White", "Caparezza", "Christian de Sica"]
len(names)
print(len(names))
'''
'''
3-10. Every Function: Think of things you could store in a list.
For example, you could make a list of mountains, rivers, countries, cities, languages,
or anything else you’d like. Write a program that creates a list containing these items 
and then uses each function introduced in this chapter at least once.
'''
'''
names: list = ["Walter White", "Caparezza", "Christian de Sica"]
luoghi:list = ["Albero Bello", "Vicolo Di Napoli", "Doganella", "Valle d'Aosta", "Garbatella"]
lingue:list = ["Italiano", "albanese", "Arabo"]
continenti:list = ["europa", "america", "oceania"]
print(luoghi)
print(names)
print(lingue)
print(continenti)

print( f"ragazzi questa sera io e {names[1]} andiamo a {luoghi[2]} chi vuole aggiungersi? volevamo approfittarne per imparare un po di {lingue[1]} dalle persone del posto ")


6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

names: list = ["Pierfranco"]
last_name:list = ["Carciofo"]
anni:list = ["8"]
città:list = ["Doganella"]
print(names)
print(last_name)
print(anni)
print(città)
'''

