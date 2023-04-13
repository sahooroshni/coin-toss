# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 19:04:37 2021

@author: roshn
"""
# COIN TOSS SIMULATION 
import random 
import numpy as np 
import matplotlib.pyplot as plt 

print('Welcome to my Coin Toss Simulation')
print('This programs simulates M trials of N coin tosses.')
input('To begin press ENTER')
N = int(input('Enter the number of tosses per trial:'))
M = int(input("Enter the number of trials to be carried out:"))
#counting number of heads in 1 trial of tossing 20 coins 

def coin_trial(N):
    heads = 0 
    tails = 0 
    total = 0
    while (total<N):
        outcome = random.choice([0,1])
        if outcome == 0:    
            heads += 1                  #counter for number of heads 
        elif outcome == 1: 
            tails += 1                  #counter for number of tails 
        total = heads + tails           #counter for total tosses 
    return{'H':heads,'T':tails}         #returns no. of heads and tails per outcome 

        

#***************** IGNORE SECTION **************
def coin_trials(M):
    heads_tot = 0 
    tails_tot = 0 
    tot = 0 
    output = [heads_tot,tails_tot]          #empty list of total heads and tails at end of M trials 
    output = np.array(output)               #converting list to array for 
    while (tot<M):
        output += coin_trial(N)             #adding total heads and tails per outcome 
        tot += 1 
    return output 
    # output[0] = sum of all heads at end of M trials 
    # output[1] = sum of all tails at end of M trials 
#print(coin_trials(M)[0]/M)
#**************************************************8

#function for probability of number of heads/tails in M trials 
def prob(x):
    freq = dict()
    prob = dict()
    for number in range(0,N+1):
        count = 0 
        for element in x:
            if (element == number):
                count += 1 
                freq[number] = count 
            prob[number] = count/M
        if count==0:
            freq[number] = 0
            prob[number] = 0 
    return prob   

#function for findind sum of all elements in a list 
def add(x):
    tot = 0 
    for element in x: 
        tot += element 
    return tot

#Function for calculating the probability distribution of heads in M trials of N coin tosses 
def prob_dist(M):
    outcome_h = []
    outcome_t =[]
    tot =  0
    while (tot<M):
        outcome = coin_trial(N)        #act of tossing coin 20 times 
        heads = outcome['H']            #number of heads per toss 
        outcome_h.append(heads)         #appending list of heads per toss  
        tails = outcome['T']            #number of tails per toss 
        outcome_t.append(tails)         #appending list of tails per toss 
        tot += 1                        #counter for total trials 
    prob_h = prob(outcome_h)
    avg_h = add(outcome_h)/M
    avg_t = add(outcome_t)/M
    m = avg_h - avg_t
    return {'heads':outcome_h, 'tails':outcome_t, 'probability':prob_h, 'average heads':avg_h, 'average tails':avg_t, 'displacement':m}
result = prob_dist(M)
#print(result['heads'])
#print(result['tails'])
#print(result['probability'])
print('Average number of heads in a trial:',result['average heads'])
print('Average number of tails in a trial:',result['average tails'])
print('Displacement/position:',result['displacement'])


#Plotting the Probability distribution of number of heads 
fig = plt.figure()
ax1 = fig.add_subplot(111)

x,y = zip(*result['probability'].items())
ax1.plot(x,y)

ax1.set_xlim(0, N)
ax1.set_xticks(np.arange(0,N+1))
ax1.set_xlabel("Number of heads")
ax1.set_ylabel("Probability of heads")
ax1.set_title('Probability distribution of heads')

ax2 = ax1.twiny()
ax2.set_xlim(0, N)
ax2.set_xticks(np.arange(-N,N+1,2))
ax2.set_title('Probability distribution of heads')
plt.show()

    
