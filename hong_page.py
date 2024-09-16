import random
import itertools as it


'''
CREATING OUR SOLUTION SPACE
Random value function with specified scope of ints
    Thompson add on for consistency: ONe to one
'''

n = 10 # Predefined no of solution space points

list1 = [i for i in range(1,n+1)]
list2 = random.sample(range(1,100+1),n)

print(list1)
print(list2)

def landscape(a,n=n, range=100):

    for i,j in zip(list1, list2):
        if i == a:
            return j

'''Agent class:
    Local Optimum Search Function: {1,...,n} -> {1,...,n}
    
        k<l<n, 
        k: Check k positions 
        l: within l points to the right 
        n: n points on a circle
    
        How it works:

            1. For all positions i within range k: 
                Check Value function at i-th position, if its value is bigger than the previous one, continue
                If not stop
    
    Performance function:
        Expected value of search
        Assumption of equal distirbution

        Make sure search function satisfies assumptions
'''

class Agent():

    def __init__(self, k,l, n=n):
        self.k = k
        self.n = n
        self.l = l
        self.search_tuple = tuple(random.sample(range(1, l+1), k))
        print('Tuples: ', self.search_tuple)
    
    def localsearch(self, ll_1, ll_2, start_point):
        # Creates an iterable cycle to go through below with the numbers specified in the search tuple
        iter_search_tuple = it.cycle(self.search_tuple)
        
        # Temporary containers for the local maxima

        max1 = ll_1.index(start_point)
        max2 =  (max1 + next(iter_search_tuple)) % n # Returns index of starting point
        print(f'Intitial max2: {max2}')

        while ll_2[max1] < ll_2[max2]:
            max1 = max2
            print(f'New max1: {max1}')
            max2 = (max1 + next(iter_search_tuple)) % n # Goes on step ahead in the solution landscape according to the tuple
            print(f'New max2: {max2}')
        return ll_1[max1] #max1 since stop condition implies max1 >= max2
    
    def stoppingpoints(self, ll_1, ll_2):
        start_l = ll_1
        stop_l = []
        for i in range(n):
            stop_l.append(self.localsearch(ll_1, ll_2, start_l[i]))
        
        return stop_l
    
    # Function to calculate the performance of an agent by taking the expected value of the stopping points of all starting points
    def performance(self, ll_1, ll_2, n=n):
        stop_l = self.stoppingpoints(ll_1, ll_2)
        stop_l_values = [ll_2[ll_1.index(stop)] for stop in stop_l]
        sum_hehe = sum(stop_l_values)

        return sum_hehe / n

'''__________Testing__________'''
    
testagent = Agent(3, 6)
print('Stopping point 1: ', testagent.localsearch(list1, list2, 1))

print(testagent.performance(list1, list2))


'''Group class
    Diversity Function:
       as defined in paper

    Attributes: Has two lists that form a landscape together
    Create landscape function: Is the function part of the two lists
    
    
 '''