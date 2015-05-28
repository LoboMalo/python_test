#correct function
def find_tup_length(*tuples):
    '''A functipn that takes in an aribtrary amount of tuples and returns their lengths in a list'''
    
    
    list = []
    for i in tuples:
           list+= [len(i)]
    print list        
    ''' Several useful functions for doing things with tuples'''

def tup_value_w_kwargs( a_tup=(1,2,3), a_int=5 ):
    '''This returns the input tuple with a_int as the first item'''
    r = (a_int,) +  a_tup[1:]
    
    return r



