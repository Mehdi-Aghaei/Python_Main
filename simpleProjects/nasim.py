import random
import numpy as np

class WorkWithRandomNumber:
    # we use this globalvar in second and third function
    endList = []

    def __init__(self, number1, number2):
        self.endList = []
        self.number1 = number1
        self.number2 = number2

    def generate(self):
        # I will create empty list and then in range 26 i Will generate random number and append it to list
        a = []
        for x in range(26):
            x = random.randint(1, 5)
            a.append(x)
        """
        This is called a cumulative sum and there is a function in numpy for the job: which return array and we convert it to list agian and show elements one by one
        """
        b = np.cumsum(a)
        finallList = b.tolist()
        # Uncomment 2 lines below to check that difference between first list and final list
        # print(a)
        # print(finallList)

        # now print every elemnt in new line
        print(*finallList, sep="\n")

    def userRange(self):
        """
        logic is same as first function just we have range from user input
        """
        num1 = int(self.number1)
        num2 = int(self.number2)
        if(1 <= num1 <= 4 and 3 <= num2 <= 5):
            list1 = []
            for i in range(26):
                i = random.randint(self.number1, self.number2)
                list1.append(i)
            # list 1 is ready
            list2 = np.cumsum(list1)
            self.endList = list2.tolist()
            for c in range(len(self.endList)):
                print(f"{self.endList[c]}\n")

        else:
            return("wrong range")

    def draw(self):
        #!to work with this method you have use second method to have list of numbers otherways it will return just  and empty list
        # ? because use did not generate any number and want to work with!!!!
        # assign or global var to local var to work with
        listTowork = self.endList
        for x in range(len(listTowork)):
            a = int(listTowork[x])
            b = "-"
            print(a*b+"\\")

# uncomment to check
# example of how to work firsat inital the class with range and then you can use methods
#a = WorkWithRandomNumber(2,3)
# using first method in range 1,5
#d = a.generate()
# use second method in range that we give
#c = a.userRange()
# use draw function
# q=a.draw()
