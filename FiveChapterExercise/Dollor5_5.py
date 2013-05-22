'''
Created on May 20, 2013

@author: user
'''

counter = {"25 cent":0,"10 cent":0,"5 cent":0,"1 cent":0}

def display():
    for keyvalue in counter.keys():
        if keyvalue != 0:
            print "%s %s numbers" %(keyvalue,counter[keyvalue])
            
def dollorexchange(value):
    a = divmod(value,25)
    counter["25 cent"] += a[0]
    if a[1] == 0:
        return 
    else:
        b = divmod(a[1],10)
        counter["10 cent"] += b[0]
        if b[1] == 0:
            return
        else:
            c = divmod(b[1],5)
            counter["5 cent"] += c[0]
            if c[1] == 0:
                return 
            else:
                counter["1 cent"] += c[1]
                   
if __name__ == "__main__":
    uservalue = float(raw_input("Please input the exchange value: \n"))
    dollorexchange(uservalue*100)
    display()