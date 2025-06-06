def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#main logic of the program
def is_valid(s) 
    #making sure ALL condition are satisified
    if cond_1(s) and cond_2(s) and cond_3(s) and cond_4(s) and cond_5(s): 
        return True
    else:
        return False

def cond_1(s): #first condition
    while len(s) > 1:
        #making sure 1st 2nd letter are always letters
        if s[0].isalpha() and s[1].isalpha():
              return True
        else:
            return False

def cond_2(s): #second condition
    if  1 < len(s) < 7: #making sure the length is between 1 and 7
        return True

def cond_3(s): #third condition
    if s.isalpha(): #s can be made up of letters only
        return True
    elif s.isalnum(): #letters and numbers
        while len(s) >= 4: #while length >= 4
            if (s[-1].isdigit() and s[-2].isdigit()): #true if last and penultimate are numbers
                return True
            else:
                return False


def cond_4(s):#4th condition
    #checking if first number is 0
    if  s[2] == "0": 
        return False
    if not (s[2].isalpha() and s[3] == 0):
        return True
    elif not (s[3].isalpha() and s[4] == 0):
        return True
    elif not (s[4].isalpha() and s[5] == 0):
        return True
    elif not (s[5].isalpha() and s[6] == 0):
        return True
    else:
        return False


def cond_5(s): #5th condition
    #checking if any punctuation in s
    puncs = ".?,&'`" 
    if not any(punc in s for punc in puncs):
        return True

main()
