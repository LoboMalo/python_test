''' Several useful functions for doing things with tuples'''
def tup_value_w_kwargs( a_tup=(1,2,3), a_int=5 ):
    '''This returns the input tuple with a_int as the first item'''
    r = (a_int,) +  a_tup[1:]
    
    return r
