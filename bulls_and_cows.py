import random
class Generator:
    genlist = []
    errortext = ''
    isWIn = False
    turncount = 0
    def __init__(self,):
        self.__generator(4)
    def __generator(self, num):
        if num > 10:
            return False
        numlist = list('0123456789')
        for i in range(0,num):
            self.genlist.append(numlist.pop(numlist.index((random.choice(numlist)))))
    def inn(self, INNLIST):
        if len(INNLIST) != len(self.genlist):
            self.errortext = 'your number must be ' + str(len(self.genlist)) + ' in length'
            return False
        elif any([INNLIST[i] not in '1234567890' for i in range(len(INNLIST))]):
            self.errortext = 'you must write only numbers'
            return False
        elif any([list(INNLIST).count(list(INNLIST)[i]) > 1 for i in range(len(INNLIST))]):
            self.errortext = 'numbers should not be repeated'
            return False
        return True 
    def checkIt(self, innlist):
        if self.inn(innlist) == False:
            return 'Your ask is incorrect, becouse: ' + self.errortext 
        answer = innlist
        innlist = list(innlist)
        bullcount = self.__findBull(innlist)
        cowcount = self.__findCow(innlist)
        self.turncount += 1
        if bullcount == len(self.genlist):
            self.isWIn = True
            return 'You WIN in: ' + str(self.turncount) + ' turn !!!!'
        return 'In: ' + answer + ' Bulls: ' + str(bullcount) + ' Cow: ' + str(cowcount)
    def __findCow(self, innlist):
        count = 0
        for i in range(len(innlist)):
            if innlist[i] in self.genlist:
                count += 1
        return count
    def __findBull(self, innlist):
        count = 0
        checklist = innlist.copy()
        for i in range(len(innlist)):
            if checklist[i] == self.genlist[i]:
                count += 1
                innlist.pop(innlist.index(checklist[i]))
        del checklist
        return count

test = Generator()
#print(test.genlist)
while test.isWIn == False:
    print(test.checkIt(input()))