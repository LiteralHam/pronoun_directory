#the purpose is to create a dictionary of multiple users that could theoretically be called on
#to check what a user's preferred pronouns are

#define a function for the user input
#create dictionaries
    #1 grammer dictionary per set of pronouns
        #eg they = {subj: they, obj: them, etc...}


#each user inputs one pronoun and it calls the associated dictionary from the set
    #user inputs 'them', it goes to read_dict, and is keyed to dict they

#allow user to double check that they like their assigned pronouns
    #create a sentence or two that use all the pronouns in the pronoun dict.
    #**need a separate sentence if user chooses they dictionary, need different
    #allow user to reject their choice and start over

#allow user to create a custom pronoun dictionary using the sentence for reference

#if possible to assign one user multiple dictionaries

#create a dictionary of all students names keyed to the dictionary of their pronouns

import sys

they_set = {'subject': 'they', 'object': 'them', 'possessive': 'theirs', 'possessive detirminer': 'their', 'reflexive': 'themself'}
she_set = {'subject': 'she', 'object': 'her', 'possessive': 'hers', 'possessive detirminer': 'her', 'reflexive': 'herself'}
he_set = {'subject': 'he', 'object': 'him', 'possessive': 'his', 'possessive detirminer': 'his', 'reflexive': 'himself'}
pronoun_set = {'they': they_set, 'she': she_set, 'he': he_set}
user_pronouns = {'Jake': [{'subject': 'fae', 'object': 'fae', 'possessive': 'faers', 'possessive detirminer': 'fae', 'reflexive': 'faeself'},
                          {'subject': 'they', 'object': 'them', 'possessive': 'theirs', 'possessive detirminer': 'their', 'reflexive': 'themself'}],
                 'Ham': {'subject': 'they', 'object': 'them', 'possessive': 'theirs', 'possessive detirminer': 'their', 'reflexive': 'themself'},
                 'Leeta': {'subject': 'she', 'object': 'her', 'possessive': 'hers', 'possessive detirminer': 'her', 'reflexive': 'herself'},
                 'Payton': {'subject': 'xe', 'object': 'xer', 'possessive': 'hirs', 'possessive detirminer': 'hir', 'reflexive': 'xerself'},
                 'Yael': {'subject': 'she', 'object': 'her', 'possessive': 'hers', 'possessive detirminer': 'her', 'reflexive': 'herself'},
                 'James': [{'subject': 'they', 'object': 'them', 'possessive': 'theirs', 'possessive detirminer': 'their', 'reflexive': 'themself'},
                           {'subject': 'she', 'object': 'her', 'possessive': 'hers', 'possessive detirminer': 'her', 'reflexive': 'herself'},
                           {'subject': 'xe', 'object': 'xer', 'possessive': 'xers', 'possessive detirminer': 'hir', 'reflexive': 'hirself'}]}
def printPronouns(nouns):
    for item in nouns:
        print(nouns[item])

def testPronouns(nouns, name):
    print(name + ' went to the store')
    print(str.title(nouns['subject']) + ' bought some dry food for ' + nouns['possessive detirminer'] + ' cat and chocolate for ' + nouns['reflexive'])
    print('This book is ' + nouns['possessive'] + '; it belongs to ' + nouns['object'])


def enterPronouns(track):
    if track == 'custom':
        custom_set = dict.copy(they_set)
        print('Please enter the pronoun you would like for each use case')
        for part in custom_set:
            custom_set[part] = input(part + ': ')
        return custom_set
    else:
        noun_set = pronoun_set[track]
        return noun_set


def pronounCollector():
    print("Please add your name and pronouns")
    print()
    name = input('Name: ')
    print('Please enter your pronouns')
    print()
    print('Type "they", "he", "she", "custom", or "multi"')
    track = input()
    if track == 'multi':
        user_pronouns[name] = []
        print('Got it, multiple sets of pronouns. How many do you have?')
        count = int(input())
        print('Great, what would you like to start with?')
        print()
        while count > 0:
            print('Type "they", "he", "she", or "custom"')
            track = input()
            nouns = enterPronouns(track)
            printPronouns(nouns)
            print()
            print('Here are your pronouns used in a sentence')
            testPronouns(nouns, name)
            print('Is this correct? y/n')
            ans = input()
            if ans == 'y':
                user_pronouns[name].append(nouns)
                count = count - 1
            else:
                print('Ok, you can choose another set or make your own custom pronoun list')
                continue
    else:
        while True:
            nouns = enterPronouns(track)
            printPronouns(nouns)
            print()
            print('Here are your pronouns used in a sentence')
            testPronouns(nouns, name)
            print('Is this correct? y/n')
            ans = input()
            if ans == 'y':
                user_pronouns[name] = nouns
                break
            else:
                print('Ok, you can choose another set or make your own custom pronoun list')
                print('Please type "they", "he", "she", or "custom"')
                track = input()
                continue
    print('Your pronouns are now saved in the user_pronouns dictionary')
    return(name, nouns)

def pronounFinder():
    print("Please enter the name of the user who's pronouns you want to look up")
    name_query = input()
    try:
        queried_nouns = user_pronouns[name_query]
        if type(queried_nouns) == dict:
            for thing in queried_nouns:
                print(queried_nouns[thing])
            print()
            testPronouns(queried_nouns, name_query)
        elif type(queried_nouns) == list:
            for i in range(len(queried_nouns)):
                new = queried_nouns[i]
                for thing in new:
                    print(new[thing])
                print()
                testPronouns(new, name_query)
                print()
        return(queried_name, queried_nouns)
    except KeyError:
        print("Sorry, that user is not in the system")
        return(queried_name, False)
    


def pronounEditor():
    print("Welcome to Pronoun Editor")
    your_name, your_pronouns = pronounFinder()
    if your_pronouns != False:
        print()
        print("Would you like to change your name? \
Your current name and pronoun entry will be deleted. y/n")
        ans = input()
        while ans == 'y':
            print("You will be redirected to the pronoun collector \
and your current entry in user_pronouns will be deleted")
            print()
            ans = input("Are you sure you want to delete your pronouns? y/n: ")
            if ans == 'y':
                del user_pronouns[your_name]
                pronounCollector()
                break
        else:
            pass
            
                
            
        

def pronounProgram():
    print("Welcome to pronoun collector")
    while True:
        print("Please type 'p' to add your pronouns, 'e' to edit your name or pronouns, 'f' to find someone's pronouns, or 'q' to quit")
        print()
        enter = input()
        print("Note: please only add or edit your own pronouns")
        if enter == 'p':
            print()
            pronounCollector()
            continue
        elif enter == 'e':
            print("Pronoun editor coming soon")
            name = input("Please enter your name: ")
            pronounFinder()
        elif enter == 'f':
            pronounFinder()
            continue
        elif enter == 'q':
            print("Thank you for using the pronoun collector")
            sys.exit()
        else:
            print("Sorry, I didn't understand that")
            continue
            
            
            






            
