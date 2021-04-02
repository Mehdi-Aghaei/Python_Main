import urllib.request
import re
import random
'''
name = AGHAEI HOSSEIN ABADI MOHAMMAD MEHDI
neptun = L2MRA1
date = 30/03/2021
Hi dear Professor:
I'm really sorry for latency on Friday I was on the way of Hungary , and I couldn't be present
Regards
'''
# we will use Regular expressions to find and counting
# we will import urllib to open file from net
ad = 'http://www.born.nhely.hu/Monthy_Python_Dead_Parrot.txt'


class Counter:
    def __init__(self, url):
        self.url = url
        # print(message) to check we did every thing right
    def check_content(self):
        # we will open the file from net
        file = urllib.request.urlopen(self.url)
        # and with read method we will read it
        message = file.read()
        message = str(message, 'utf-8')
        return message

    def parrot_count(self):
        file = urllib.request.urlopen(self.url)
        message = file.read()
        message = str(message, 'utf-8')
        p_char = len(re.findall('parrot', message))
        P_char = len(re.findall('Parrot', message))
        tot = int(p_char) + int(P_char)
        # we use findall method from re to find all c and o characters
        return f"we have {int(p_char)} parrot and {int(P_char)} Parrot and total is {tot} in text "

    def line_begin(self):
        file = urllib.request.urlopen(self.url)
        message = file.read()
        message = str(message, 'utf-8')
        c_char = len(re.findall('^C', message, re.MULTILINE))
        o_char = len(re.findall('^O', message, re.MULTILINE))
        # we use findall method from re to find all c and o characters
        # and multuline method to go through all lines
        return f"we have {int(c_char)} line start with 'C' and {int(o_char)} line start with 'O' in text"

    def largest_line(self):
        file = urllib.request.urlopen(self.url)
        ''' for finding age largest line we have to define 2 var one for handel len and one to handle len of line then we will use for loop to loop through the file and we will say if the len of the line was larger than our default make it as a default and counting and also make that line as new default too
        then we will return it with utf-8 encoding
        '''
        max_len = 0
        max_len_line = ''
        for line in file:
            if(len(line) > max_len):
                max_len = len(line)
                max_len_line = line
        longest = str(max_len_line, 'utf-8')
        # to write a output in a file we will open that file and then we will write and close it
        f = open("/tmp/L2MRA1_long_parrot.txt ", "w")
        f.write(longest)
        f.close()
        return longest

    def longest_word(self):
        file = urllib.request.urlopen(self.url)
        message = file.read()
        message = str(message, 'utf-8')
        word_by_word_list = message.split()
        # we split our string to get list of our text word by word in a list
        longest_word = max(word_by_word_list, key=len)
        # we use max function wich return a highest value and its also have key that we set it to length
        len_the_word = len(longest_word)
        return f'The longest word is "{longest_word}" and length is {len_the_word}. '

    def game_parrot_to_elephant(self):
        file = urllib.request.urlopen(self.url)
        user_input = 0
        our_random_choice = random.randint(20, 40)
        # generate random number with randint in given range
        # print(our_random_choice)
        # uncomment for cheating ;)
        while (user_input != our_random_choice):
            '''
            create while loop because we will have more than one attempt from user input
            then we will write some if statements to help user to find a number
            after when he found that we will read that lines and loop through it and encoded and remove extra white spaces and finaly print it and append it to a text file 
            '''
            user_input = int(
                input("Please enter a number in range 20 until 40 : "))
            if (user_input < our_random_choice):
                print("your number is less than our random choice")
            if(user_input > our_random_choice):
                print("your number is greater than our random choice")
            if(user_input == our_random_choice):
                for i in range(our_random_choice):
                    message = file.readline()
                    message = str(message, 'utf-8')
                    message = " ".join(message.split())
                    line = message.replace('parrot', 'elephant')
                    line = line.replace('Parrot', 'Elephant')
                    print(line)
                    f = open("/tmp/L2MRA1_long_parrot.txt ", mode="a")
                    f.writelines(line)
                    f.close()
                return "Thanks for playing :)"


# c = Counter(ad)
# print(c.largest_line())
#c.check_content() or Counter.check_content(c)
