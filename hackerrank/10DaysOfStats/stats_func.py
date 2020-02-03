'''
poisson
geometric
factorial
combination 
binomial
weighted_mean
std
mode
'''
from math import sqrt    
from statistics import mean

def poisson(l, k):
    """
    Args:      
        l (float): the average number of successes that occur in a specified region
        k (int): the actual number of successes that occur in a specified region
    Returns:
        float: the probability of occurance  
    
    Example:
    >>> poisson(2,3)
    0.1804470443154836
    
    >>> sum([poisson(5,i) for i in range(0,4)])
    0.2650259152973617
    """    
    return ((l**k) * math.exp(-l))/factorial(k)


def geometric(n, p):
    """
    Calculate the distribution of trials until the first success/fail
    Args:      
        n (int): the total number of trials
        p (float): the probability of success of 1 trial 
    Returns:
        float: the probability of occurance  
    """    
    return (1-p)**(n-1) * p

def factorial(n):
    """
    Calculate a factorial $n!$
    Args:     
        n (int): the total number of trials
    Returns:
        int: factorial result
    """
    return 1 if n == 0 else n*factorial(n-1)

def combination(n,x):
    """
    Select different elements combination from a group without duplication ${}_n C_k$
    
    Args:     
        n (int): the total number of trials 
        x (int): the number of successes
    Returns:
        int: combination result      
    """
    return factorial(n) / (factorial(x) * factorial(n-x))

def binomial(x,n,p):
    """
    Calculate the probability distribution of 0/1 event occurances in n trials
    Args:     
        x (int): the number of successes    
        n (int): the total number of trials
        p (float): the probability of success of 1 trial 
    Returns:
        float: the probability of occurance  
    """
    return combination(n,x) * p**x * (1-p)**(n-x)

def weighted_mean(X, W):
    '''
    Calculate weighted mean of an array
    
    Args: 
        X (list): list of integers 
        W (list): list of weights in integers 
        
    Returns:
        float: weighted mean of an array
    '''
    return sum([X[i] * W[i] for i in range(len(X))]) / sum(W)    


def std(X):
    '''
    Calculate standard deviation of an array
    
    Args: 
        X (list): list of integers 
    
    Returns:
        float: standard deviation of an array
    '''    
    lst = [X[i] - mean(X) for i in range(len(X))]
    return sqrt(sum(map(lambda x: x**2, lst)) / len(X))


def mode(X):    
    '''
    Calculate mode of an array
    
    Args: 
        X (list): list of integers 
    
    Returns:
        float: mode of an array
    
    Note: 
        If the array contains more than one modal value, choose the numerically smallest one.
    '''
    count_lst = {i: X.count(i) for i in X}
    return max(count_lst, key=count_lst.get)