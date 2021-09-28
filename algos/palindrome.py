
def isPalindrome(stringInput):
    stringInput = stringInput.lower()
    reversedVersion = ""
    for i in range(len(stringInput)-1,-1,-1):
        # print(stringInput[i])
        reversedVersion+=stringInput[i]
    # print(reversedVersion)
    if(reversedVersion == stringInput):
        return True
    else:
        return False




# print(isPalindrome("racecar")) #True
# print(isPalindrome("young mula")) #False
# print(isPalindrome("tacocat")) #True



def isPalindrome2(stringInput):
    stringInput = stringInput.lower()
    for i in range(0, int(len(stringInput)/2), 1):
        if(stringInput[i]!= stringInput[len(stringInput)-1-i]):
            return False
    return True


print(isPalindrome2("racecar")) #True
print(isPalindrome2("taacocat")) #False



# i = 0 --> first index
# lastindex = stringInput.length-1 ---> last index

#i = 1 --> second index
#secondtolastindex = stringInput.length-1-i 

#i = 2 --> third index
#thirdtolastindex = stringInput.length-1-i






