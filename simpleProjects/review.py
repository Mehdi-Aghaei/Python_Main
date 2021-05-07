import re
import urllib.request
import os
ad1 = "http://born.nhely.hu/Hamlet_EN.txt"
ad2 = "http://born.nhely.hu/Hamlet_HU_UTF.txt"


class Shakespear:
    def __init__(self, url1, url2):
        self.url1 = url1
        self.url2 = url2

    def read_3_line(self):
        file1 = urllib.request.urlopen(self.url1)
        file2 = urllib.request.urlopen(self.url2)
        message = file1.read()
        message2 = file2.read()
        message = str(message, "utf-8")
        message2 = str(message2, "utf-8")
        """For a one-liner we could split() the string by newlines and then join() first N elements of the resulting list by newlines again."""
        res = os.linesep.join(message.split(os.linesep)[:3])
        res2 = os.linesep.join(message2.split(os.linesep)[:3])
        print(f"{res}{res2}")

    def word_count(self):
        file1 = urllib.request.urlopen(self.url1)
        file2 = urllib.request.urlopen(self.url2)
        message = file1.read()
        message2 = file2.read()
        message = str(message, "utf-8")
        message2 = str(message2, "utf-8")
        final = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in message.split()]
        final2 = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in message2.split()]
        final = [x.strip(' ') for x in final]
        final2 = [x.strip(' ') for x in final2]
        while("" in final):
            final.remove("")
        while("" in final2):
            final2.remove("")
        len_eng = len(final)
        len_hu = len(final2)
        print(
            f"the total word in english is :{len_eng} and for hungarian is :{len_hu}")

    def letter_count(self):
        file1 = urllib.request.urlopen(self.url1)
        file2 = urllib.request.urlopen(self.url2)
        message = file1.read()
        message2 = file2.read()
        message = str(message, "utf-8")
        message2 = str(message2, "utf-8")
        number_of_letters = len(message) - message.count(" ")
        number_of_letters2 = len(message2) - message2.count(" ")
        print(
            f"total leter for English is:{number_of_letters} and for hungarian is : {number_of_letters2}")

    def number_of_vowels(self):
        file1 = urllib.request.urlopen(self.url1)
        file2 = urllib.request.urlopen(self.url2)
        message = file1.read()
        message2 = file2.read()
        message = str(message, "utf-8").lower()
        message2 = str(message2, "utf-8").lower()
        a_char = len(re.findall('a', message))
        e_char = len(re.findall('e', message))    
        i_char = len(re.findall('i', message))
        o_char = len(re.findall('o', message))
        u_char = len(re.findall('u', message))
        
        a_char2 = len(re.findall('a', message2))
        e_char2 = len(re.findall('e', message2))
        i_char2 = len(re.findall('i', message2))
        o_char2= len(re.findall('o', message2))
        u_char2 = len(re.findall('u', message2))
        print(
            f"a vowels in English is :{a_char} \n e vowels in English is :{e_char} \n i vowels in English is :{i_char} \n o vowels in English is :{o_char} \n u vowels in English is :{u_char} \n")
        print(
            f"a vowels in Hungarian is :{a_char2} \n e vowels in Hungarian is :{e_char2} \n i vowels in Hungarian is :{i_char2} \n o vowels in Hungarian is :{o_char2} \n u vowels in Hungarian is :{u_char2}")
        


a = Shakespear(ad1, ad2)
a.read_3_line()
a.word_count()
a.letter_count()
a.number_of_vowels()
