import random

def game():
    list_of_scores = []
    list_of_roll = []
    n=5
    counter = 0
    no_of_remaning_chance = 0
    while no_of_remaning_chance<int(n):
      
        if counter <= 12:
            turn = no_of_remaning_chance + 1
            a = random.randint(1,6)
            counter += a 
            list_of_roll.append(a)
            list_of_scores.append(counter)
            no_of_remaning_chance = no_of_remaning_chance + 1
        elif 12 <= counter < 17:
            # can hit 12 at score 17
            # print("counter hit 12 liao")
            # print(no_of_remaning_chance)
            turn = no_of_remaning_chance + 1
            a = random.randint(1,2) 
            counter += a 
            list_of_roll.append(a)
            list_of_scores.append(counter)
            no_of_remaning_chance = no_of_remaning_chance + 1
        elif counter >= 17:
            # can hit 12 at score 18, max score 18 here + 1 + 1 > 20
            # print("counter hit 17 liao")
            turn = no_of_remaning_chance + 1
            a = 1
            counter += a 
            list_of_roll.append(a)
            list_of_scores.append(counter)
            no_of_remaning_chance = no_of_remaning_chance + 1
        
        # print(turn, a,counter, list_of_scores)
           
    return list_of_roll, list_of_scores

