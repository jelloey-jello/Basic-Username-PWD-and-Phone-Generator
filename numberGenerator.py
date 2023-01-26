#COPYRIGHT Josiah Thompson and NeuralNine, 2022
#add feature to where same # numbers aren't generated twice, username and password
#add feature to where after state is inputted, the program asks for users county
#add feature where the case (lower, upper, or mix) of the state is ignored

#Phone Number Generator w/built-in secure password feature

#lines 3-7: Importing libaraies used in the script
from random import *
import random
import re

def username():
#lines 17-41 are ©CodeVsColor via https://www.codevscolor.com/python-check-validity-password
#setting parameters for a secure password, i.e. between 6 to 13 characters, including symbols/numbers, etc.
    while True:
        user_input = input("""\nCreate a username below. Note that:

        -Total characters should be between 6 and 13.
        -Username should contain one letter between [a-z].
        -Username should contain one letter between [A-Z].
        -Username should contain one letter between [0-9].
        -Username should contain a character(s) in [~!@#$%^&*()-+].
        -Username should not contain any spaces.
        
        Enter your username here: """)
        is_valid = False
        if (len(user_input) < 6 or len(user_input) > 13):
            print("\nInvalid username. Total characters should be between 6 and 13.")
            continue
        elif not re.search("[A-Z]", user_input):
            print("\nInvalid! Username should contain one letter between [A-Z].")
            continue
        elif not re.search("[a-z]", user_input):
            print("\nInvalid! Username should contain one letter between [a-z].")
            continue
        elif not re.search("[0-9]", user_input):
            print("\nInvalid! Username should contain one letter between [0-9].")
            continue
        elif not re.search("[~!@#$%^&*()-+]", user_input):
            print("\nInvalid! Username should contain a character(s) in [~!@#$%^&*()-+].")
            continue
        elif re.search ("[\s]", user_input):
            print("\nInvalid! Username should not contain any spaces.")
            continue
        else:
            is_valid = True
            break

"""lines 55-79 were taken from NeuralNine (link: https://www.youtube.com/watch?v=rHTwjV1ORUQimport)
lines 75-77 mean that for each password in the range of amount, we're selecting items from the
possible list of passcode inputs and "joining" them with the empty string
random.sample means that we're going to take anything out of the full string we have
(all, length)/(all2, length2) means we're using the all string, the complete string, with all 
the characters we'll be using and define the length of the string to be the amount of characters, so 
we're taking that amount of samples out of that string
sample also means that we CANNOT reuse characters
"""

def password():
    #length and amount take the integer input of the passwords length and how many passwords are generated respectively
    length = int(input("\nOkay! Now for your password. How many characters would you like? "))
    amount = 1
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------")
    uppercase_Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_Letters = uppercase_Letters.lower()
    digits = "0123456789"
    upper, lower, nums, nums2, nums3 = True, True, True, True, True
    all = ""
    if upper == True: 
        all += uppercase_Letters
    if lower == True:
        all += lowercase_Letters
    if nums == True:
        all += digits
    if nums2 == True:
        all += digits
    if nums3 == True:
        all += digits
    for i in range(amount):
        password = "".join(random.sample(all, length))
        print (f"\nYour password is {password}. Please go to www.myWebsite.com to register your phone number via your username/password and your phone number. Thank you, and have a great one!\n")

#predefined lists containing all regional states so that I can access them when calling customerPhoneNum()
s = ["Delaware:", "District of Columbia", "Maryland", "Virginia", "West Virginia", "Kentucky", "North Carolina", "South Carolina", "Tennessee",
"Georgia", "Florida", "Alabama", "Mississippi", "Arkansas", "Louisiana", "Texas", "Oklahoma"]
ne = ["Maine", "New Hampshire", "Vermont", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Pennsylvania"]
mw = ["Ohio", "Michigan", "Indiana", "Wisconsin", "Illinois", "Minnesota", "Iowa", "Missouri", "North Dakota", "South Dakota", "Nebraska",
"Kansas"]
w = ["Montana", "Idaho", "Wyoming", "Colorado", "New Mexico", "Arizona", "Utah", "Nevada", "California", "Oregon", "Washington", "Alaska",
"Hawaii"]
aT = ["American Samoa", "Guam", "Northern Mariana Islands", "Puerto Rico", "US Virgin Islands"]

#all busines area codes
bTFACs = [800, 833, 844, 855, 866, 877, 888] #businessTollFreeAreaCodes
bop = "" #business or person; False = business & True = person

#function called phoneNum() that sets bop = False or True, then prints bop and the business/customer phone number. The parameters passed is a random business area code and
#two randomly generated numbers

def phoneNum(a, b, c):
    x = [1]
    for i in x:
        if bop == False:
            print ("\n" + "***** bop = " + str(bop))
            print(f"\nYour business' phone number is ({a}) {b}-{c}.\n")
        if bop == True: #customer phone number
            if str(in2) in allACs.keys():
                print(f"\nOkay, your phone number is: ({a}) {b}-{c}.\n")

#function called customerPhoneNum() that print the customer's phone number if the state they enter is in the list of US states & territories. The parameters passed are the
#area code and two randomly generated numbers

#def customerPhoneNum(d, e, f):
    #if str(in2) in allACs.keys():
        #print(f"\nOkay, your phone number is: ({a}) {b}-{c}.\n")

#asking if you're a business or customer
userInput = input("\nHi! Welcome to Your Phone Number Generator (version 1.0.2). Are you a business or a regular person? Type F for business & T for customer. ")

#bop = False, i.e. it's a business, so print a business phone number via a random business area code and two randomly generated numbers
if userInput == "F":
    bop = False
    phoneNum(random.choice(bTFACs), randint(100, 999), randint(1000, 9999))
    #else, it's a person
else:
    bop = True
    print ("\n" + "***** bop = " + str(bop)) #print to the terminal to let debugger know it's a person
    #gives person list of US states & territories to choose from
    in2 = input("""\nNo problem! What state/territory are you from? Please choose from the list below:

    Delaware, District of Columbia, Maryland, Virginia, West Virginia, Kentucky,
    North Carolina, South Carolina, Tennessee, Georgia, Florida, Alabama,
    Mississippi, Arkansas, Louisiana, Texas, Oklahoma, Maine, New Hampshire,
    Vermont, Massachusetts, Rhode Island, Connecticut, New York, New Jersey,
    Pennsylvania, Ohio, Michigan, Indiana, Wisconsin, Illinois,
    Minnesota, Iowa, Missouri, North Dakota, South Dakota, Nebraska,
    Kansas, Montana, Idaho, Wyoming, Colorado, New Mexico,
    Arizona, Utah, Nevada, California, Oregon, Washington,
    Alaska, Hawaii, American Samoa, Guam, Northern Mariana Islands,
    Puerto Rico, US Virgin Islands

    Type your state/territory here: """)
    if in2 in str(s): 
        print(f"\nOkay, {in2} it is!\n") #if input is in the dictionary below (i.e. allACs), 1st print the state/territory they chose
    allACs = {str("Alabama"):[205, 251, 256, 334, 938], str("American Samoa"):[684], str("Alaska"):[250, 907],
          str("Arizona"):[480, 520, 602, 623, 928], str("Arkansas"):[479, 501, 870], str("California"):[209, 213, 310, 323, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 650, 657, 661, 707, 714, 747, 760, 805, 818, 820, 831, 840, 858, 909, 916, 925, 949, 951],
          str("Colorado"):[303, 719, 720, 970, 983], str("Connecticut"):[203, 457, 860, 959], str("District of Columbia"):[202],
          str("Delaware"):[302], str("Florida"):[229, 239, 251, 305, 321, 334, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954],
          str("Georgia"):[229, 404, 470, 478, 678, 706, 762, 912], str("Guam"):[671], str("Hawaii"):[808], str("Idaho"):[208, 986],
          str("Illinois"):[217, 224, 309, 312, 331, 447, 618, 630, 708, 773, 779, 815, 847, 872],
          str("Indiana"):[219, 260, 317, 463, 574, 765, 812, 930], str("Iowa"):[219, 260, 317, 463, 574, 765, 812, 930],
          str("Kansas"):[316, 620, 785, 913], str("Kentucky"):[270, 364, 502, 606, 859], str("Louisiana"):[225, 318, 337, 504, 985],
          str("Maine"):[207], str("Maryland"):[240, 301, 410, 443, 667], str("Massachusetts"):[339, 351, 413, 508, 617, 774, 789, 857, 978],
          str("Michigan"):[231, 248, 269, 313, 517, 586, 616, 679, 734, 810, 906, 947, 989], str("Minnesota"):[218, 320, 507, 612, 651, 763, 952],
          str("Mississippi"):[228, 601, 622, 769], str("Missouri"):[314, 417, 573, 636, 660, 816], str("Montana"):[406],
          str("Nebraska"):[308, 402, 531], str("Northern Mariana Islands"):[670], str("Nevada"):[702, 725, 775],
          str("New Hampshire"):[603], str("New Jersey"):[201, 551, 609, 640, 732, 848, 856, 862, 908, 973],
          str("New Mexico"):[505, 575], str("New York"):[212, 315, 332, 347, 516, 518, 585, 607, 631, 646, 680, 716, 718, 838, 845, 814, 917, 929, 934],
          str("North Carolina"):[252, 336, 704, 743, 828, 910, 919, 980, 984], str("North Dakota"):[701], str("Ohio"):[216, 220, 234, 326, 330, 380, 419, 440, 513, 567, 614, 740, 937],
          str("Oklahoma"):[405, 539, 572, 580, 918], str("Oregon"):[458, 503, 541, 971], str("Pennsylvania"):[215, 223, 267, 272, 412, 484, 570, 582, 610, 717, 724, 814, 878],
          str("Puerto Rico"):[787, 939], str("Rhode Island"):[401], str("South Carolina"):[803, 839, 843, 854, 864],
          str("South Dakaota"):[605], str("Tenessee"):[423, 456, 615, 629, 731, 865, 901, 931], str("Texas"):[210, 254, 281, 325, 361, 409, 430, 432, 512, 682, 713, 806, 817, 830, 903, 915, 936, 940, 956, 979],
          str("Utah"):[385, 435, 801], str("US Virgin Islands"):[340], str("Vermont"):[802], str("Virginia"):[276, 434, 540, 571, 703, 757, 804, 826],
          str("Washington"):[206, 253, 360, 425, 509, 564], str("West Virginia"):[304, 861], str("Wisconsin"):[262, 414, 534, 608, 715, 920], str("Wyoming"):[307]}
    phoneNum(random.choice(allACs[in2]), randint(100, 999), randint(1000, 9999)) #then, print the phone number via a randomly chosen area code from that state/territory and
    #two randomly generated numbers

in3 = input("Would you like a username and password for your phone number? ") #asking if they would like to secure their new number with a username and password

if in3 == "No":
    print("\nThat's fine, please go to www.myWebsite.com to register your phone number via your business' information. Have a great rest of your day!\n") #if not, then print this message
else:
    username(), password() #else, run the username and password functions above