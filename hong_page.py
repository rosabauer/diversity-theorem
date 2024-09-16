import random
import itertools as it


'''
CREATING OUR SOLUTION SPACE
Random value function with specified scope of ints
    Thompson add on for consistency: ONe to one
'''



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

    def __init__(self, k,l, n):
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
    def performance(self, ll_1, ll_2, n):
        stop_l = self.stoppingpoints(ll_1, ll_2)
        stop_l_values = [ll_2[ll_1.index(stop)] for stop in stop_l]

        return sum(stop_l_values) / n

'''__________Testing__________'''
    
# testagent = Agent(3, 6, 10)
# print('Stopping point 1: ', testagent.localsearch(list1, list2, 1))

# print(testagent.performance(list1, list2))


'''Group class
    Diversity Function:
       as defined in paper

    Attributes: Has two lists that form a landscape together
    Create landscape function: Is the function part of the two lists
    
    
 '''

class AgentGroup():

    def __init__(self, agent_number, n, l, k):
        self.n = n
        self.k = k
        self.l = l
        self.agent_number = agent_number

        # Defining the solution space
        self.list1 = [i for i in range(1,n+1)]
        self.list2 = random.sample(range(1,100+1),n)

        # Create Agents
        self.agents = [Agent(self.k,self.l,self.n) for _ in range(1,agent_number+1)]


    def solution(self, a):
        for i,j in zip(self.list1, self.list2):
            if i == a:
                return j
    
    def diversity(self, agent1, agent2):
        deductions = 0
        for i in range(self.k):
            if agent1.search_tuple[i] != agent2.search_tuple[i]:
                deductions+=1
        
        formula = (self.k - deductions) / self.k
        return formula
    
    def avg_diversity(self):
        individual_scores = []
        i = 0
        j = 0
        for i in range(len(self.agents)):
            for j in range(i+1, len(self.agents)):
                x = self.diversity(self.agents[i], self.agents[j])
                print(x)
                individual_scores.append(x)

        comparisons = (self.agent_number ** (self.agent_number-1))/2
        
        return sum(individual_scores)/comparisons
     
    
'''___________Testing_______'''

testgroup = AgentGroup(agent_number=10, n=10, l=5, k=3)
print(testgroup.avg_diversity())
