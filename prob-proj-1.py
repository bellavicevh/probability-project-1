import math

# vals are still slightly different from what was given
def random_number_generator(x):
    x = x + 999
    a = 9429
    c = 3967
    K = 16384
    x = ((a*x+c)%K)
    return x/K

def get_answer_time(x):
    rand = random_number_generator(x)
    return 12*math.log(12*rand)

def random_var_generator(x):
    time = 0
    for i in range(0, 3):
        rand = random_number_generator(x*4+i)
        # Add 6 seconds every time the rep makes a call
        time = time + 6
        # If there's a busy signal, add 3 seconds + 1 sec to hang up
        if(rand < .2):
            time = time + 3 + 1
        # If they don't answer, add 25 seconds + 1 sec to hang up
        elif(rand < .5):
            time = time + 25 + 1
        # If they answer, determine how long it takes to answer
        else:
            time = time + get_answer_time(x*8+i)
            break
    return time

times = []
for i in range(1, 1000):
    times.append(random_var_generator(i))
    
print(times)