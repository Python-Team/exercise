'''
Created on May 17, 2013

@author: user
'''

def Score():
    temp = raw_input("please enter your score:")
    score = int(temp)
    if(90 <= score <= 100):
        return "Score is A."
    if(80 <= score <= 89):
        return "Score is B"
    if(70 <= score <= 79):
        return "Score is C."
    if(60 <= score <= 69):
        return "Score is D."
    if(0 <= score <= 59):
        return "Score is F."
    else:
        return "Not valid score."
    
if __name__ == "__main__":
    print Score()