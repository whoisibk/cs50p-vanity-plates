def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if cond_1(s) and cond_2(s) and cond_3(s) and cond_4(s) and cond_5(s):
        return True
    else:
        return False

def cond_1(s):
    while len(s) > 1:
        if s[0].isalpha() and s[1].isalpha():
              return True
        else:
            return False

def cond_2(s):
    if  1 < len(s) < 7:
        return True

def cond_3(s):
    if s.isalpha():
        return True
    elif s.isalnum():
        while len(s) >= 4:
            if (s[-1].isdigit() and s[-2].isdigit()):
                return True
            else:
                return False


def cond_4(s):
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


def cond_5(s):
    puncs = ".?,&'`"
    if not any(punc in s for punc in puncs):
        return True

main()
