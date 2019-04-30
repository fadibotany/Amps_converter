# this function converts milliamps to amps
def milliA_to_A(x):
    total = float(x)/float(1000)
    print(str(total) + " amps")
    # remember 1 milliamp is 0.001 amp


# this function converts amps to milliamps
def A_to_milliA(x):
    total = x * 1000
    print(str(total) + " milliamps")
    #remember 0.001 amp is 1 milliamp

#-----------------------------------------------------


# this functions converts microamps to amps
def microA_to_A(x):
    total = float(x)/float(1000000)
    print(str(total) + " amps")

def A_to_microA(x):
    total = x * 1000000
    print(str(total)+ " microamps")

#------------------------------------------------------


#milliA_to_A(2500) # remove the hashtag at the begining and change the number inside the parenthesise to get the amps

#A_to_milliA(2.5)  # remove the hashtag at the begining and change the number inside the parenthesise to get the milliamps

#microA_to_A(1000000) # remove the hashtag at the begining and change the number inside the parenthesise to get the amps

#A_to_microA(1) # remove the hashtag at the begining and change the number inside the parenthesise to get the microamps