def solution(number):
    number = int(number)
    a = []
    #define a list to pass the selected number in it
    # if statment for handeling negative
    if number >= 0:
        # we will create loop to iterate until input number
        # and choose wich number can pass our rule
        for i in range(number):
            if(i % 5 == 0 or i % 3 == 0):
                # we will add selected  number by append to list
                a.append(i)
                #total = sum(a)
                #sun function is slow
                # we will create new loop to calculate sum of list
        tot = 0
        for val in a:
            tot = tot+val
        return tot

    else:
        return 0
