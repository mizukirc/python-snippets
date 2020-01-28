'''
mean, median, weighted_mean, mode, std
'''
from math import sqrt 

def mean(X):
    '''
    Calculate average or mean of an array
    
    Args: 
        X (list): list of integers 
    
    Returns:
        float: mean of an array
    '''    
    return sum(X)/len(X)


def median(X):
    '''
    Calculate median of an array  
    
    Args: 
        X (list): list of integers 
    
    Returns:
        float: median of an array
    
    Note:
        If the length of the array is even, average the two middle elements
    '''
    if len(X) % 2 == 1:
        return X[len(X)//2]
    else:
        return sum(X[len(X)//2-1:len(X)//2+1]) / 2  
    

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
    
