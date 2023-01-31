import random

#Initialize some variables to keep track of outcomes
stayAndWin = 0
stayAndLose = 0
switchAndWin = 0
switchAndLose = 0

#Initialize a looping variable
trialNum = 0

#Start the loop
while(trialNum < 1000):

    #We'll need these two lists to keep track of what's going on in our simulation
    doorsContestantCanChoose = [1, 2, 3]
    doorsHostCanReveal = [1,2,3]

    #Randomly place the car
    doorWithCar = random.randint(1,3)

    #The contestant chooses one door
    contestantChooses = random.choice(doorsContestantCanChoose)
    

    #Update our lists to keep track of the choices that have already been made
    doorsContestantCanChoose.remove(contestantChooses)
    doorsHostCanReveal.remove(contestantChooses)
    if doorWithCar in doorsHostCanReveal:
        doorsHostCanReveal.remove(doorWithCar)

    #The host is going to show one of the doors with a goat
    doorWithGoatRevealed = random.choice(doorsHostCanReveal)
    doorsContestantCanChoose.remove(doorWithGoatRevealed)

    #Let the contestant decide whether to stay or switch
    contestantSwitches = random.choice([True, False])

    #Did they win?
    if contestantSwitches:
        contestantChooses = doorsContestantCanChoose[0]
        if contestantChooses == doorWithCar:
            switchAndWin = switchAndWin + 1
        else:
            switchAndLose = switchAndLose + 1

    else:
        if contestantChooses == doorWithCar:
            stayAndWin = stayAndWin + 1
        else:
            stayAndLose = stayAndLose + 1

    #Prepare for the next loop - increase the trial number
    trialNum += 1

#Done: Print the results
print("Total Trials:", trialNum)
print("Total times staying:", stayAndLose + stayAndWin)
print("    - Stay and Win:", stayAndWin)
print("    - Stay and Lose:", stayAndLose)
print("Total times switching:", switchAndLose + switchAndWin)
print("    - Switch and Win:", switchAndWin)
print("    - Switch and Lose:", switchAndLose)

print("So if you keep your choice, your chances of winning are", stayAndWin/(stayAndWin + stayAndLose))
print("And if you switch, your chances of winning are", switchAndWin/(switchAndWin + switchAndLose))