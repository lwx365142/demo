'''
# course 9
days = "Mon Tue Wed Tue Fri Sat Sun "
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days :",days)
print("Here are the months:", months)
print(
There are something going on here.\n
with the three double-quotes.\n
)
# course 10
tabby_cat = "\t I am tabby in."
persian_cat = "I'm spilt\non a line."
backslash_cat = "I'm \\ a \\ cat."
print(tabby_cat)
print(persian_cat)
print(backslash_cat)

# course 11
print("How old are you?"),
age = input()
print("How tail are you?"),
height = input()
print("How much are you weigh?"),
weight = input()
print("So ,you are %r old ,%r tall and %r heavy." % (age,height,weight) )

# course 12
age = input("How old are you?" )
height = input("How tail are you?")
weight = input("How much are you weight")
print("So,you are %r old ,%r talland %r heavy" % (age,height,weight))

# course 13
from sys import argv

script, first, second, third = argv
print("The script is called :", script)
print("Your first var is :", first)
print("Your second var is:", second)
print("Your third var is:", third)

# course 13
from sys import argv

script, user_name = argv
prompt = '>'

print("Hi %s ,I'm the %s script." % (user_name,script))
print("I'd like to ask you a few question.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("Alright,so you said %r about liking me.\nYou live in %r.Not sure where that is.And you have a %r compute.Nice." % (likes , lives, computer)

      )

# course 15
from sys import argv

script, file_name = argv

txt = open(file_name)                         #open the file

print("Here is your file %r" % file_name)
print(txt.read())                             #print the content from read file

print("Type the filename again:")
file_again = input(">")
txt_again = open(file_again)

print(txt_again.read())

# course 16
from sys import argv

script, file_name = argv

print("We are going to erase %r " % file_name)
print("If you don't want that ,hit ctrl C (^C).")
print("If you want that,hit return.")

input("?")

print("Open the file ...")
target = open(file_name,'w')

print("Truncating the file, Goodbye!")
target.truncate()

print("Now,I am going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I am going to write these to the line.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And ,finally ,we close it .")
target.close()

#course 17
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s " % (from_file, to_file))
in_put = open(from_file)
indata = in_put.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exit? %r " % exists(to_file))
print("Ready,hit return to continue ,ctrl c to abort")
input()

out_put = open(to_file,'w')
out_put.write(indata)

print("Alright,all done")

out_put.close()
in_put.close()

# 21 course
def add(a, b):
    print("ADDING %d + %d " % (a, b))
    return a + b

def subtract(a, b):
    print("SUBSTRACT %d - %d " % (a, b))
    return a - b

def mutiply(a, b):
    print("MUTIPLY %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DVIDE %d / %d " % (a, b))
    return a/b

print("Let's do some math with just funtion!")
age = add(30, 5)
height = subtract(78, 4)
weight = mutiply(90, 2)
iq = divide(100, 2)

print("Age %d ,Height %d, Weight %d, Iq %d" % (age, height, weight,iq))

print("Here is a puzzle.")

what = add(age, subtract(height, mutiply(weight, divide(iq, 2))))

print("That's became:", what, "Can you do it by hand?")

# 24 course
print("Let's practice everthing.")
print("You\'d need to know \'bout escapes with \\ that do \n newline and \t tabs.")

poem =
\tThe lovely world
with logic so family planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print("This should be five :%s" % five )

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of %d:" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way!")
print("We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point))
'''
# 25 course
def break_words(stuff):
#    This function will break up words for us
    words = stuff.split(' ')
    return words
#sentence = "All good things."
#words = break_words(sentence)
#words = sentence.split( )
#print (words)
def sort_words(words):
#    Sort the words
    return sorted(words)

def print_first_word(words):
#   Print the first word after poping it off.
    word = words.pop(0)
    print(word)

def print_last_word(words):
#    Print the last word after poping it off.
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
#    Takes in a full sentence and returns the sort the words.
    words = break_words(sentence)
    return sorted(words)

def print_first_and_last(sentence):
#    Print the first and last word in the sentence.
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
#    Sort the words and print the first and last one.
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)












