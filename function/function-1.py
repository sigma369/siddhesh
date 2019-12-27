
def computepay (hours,rate):
 
    if hours <= 40:
        pay = (hours * rate)
        print("your totaL pay is ", pay)
    else:
        pay = (40 * rate) + (hours-40)*rate*1.5
        print("your totaL pay is ", pay)
    return "enjoy"

def hoursip():
    string = True
    while string :
        hour=input('please enter no of hours\n')
        try:
            hour=float(hour)
            string=False
        except:
            print('please enter numerical value')
            
    hour=float(hour)
    return hour
    
def rateip():
    string = True
    while string :
        rate=input('please enter rate\n')
        try:
            rate=float(rate)
            string=False
        except:
            print('please enter numerical value')
            
    rate=float(rate)
    return rate        

h=hoursip()
r=rateip()
print(computepay(h,r))




