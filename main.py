import time
validInput=False
while not validInput:
    remainingTime=input('Insert time to count down (h:m:s)' )
    if remainingTime.count(':')==2:
        remainingTime=remainingTime.split(':')
        if remainingTime[0].isdigit() and remainingTime[1].isdigit() and remainingTime[2].isdigit():
            for idx in range(len(remainingTime)):
                remainingTime[idx]=int(remainingTime[idx])    
            if remainingTime[0]>=0 and remainingTime[1]>=0 and remainingTime[2]>=0:
                validInput=True

remainingSec=(remainingTime[0]*60+remainingTime[1])*60+remainingTime[2]

while remainingSec>0:
    remainingTime[0]=remainingSec//3600
    remainingTime[1]=(remainingSec%3600)//60
    remainingTime[2]=(remainingSec%3600)%60
    print(f'{remainingTime[0]}:{remainingTime[1]}:{remainingTime[2]}')
    remainingSec-=1
    time.sleep(1)