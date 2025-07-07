def mario_from_num(base_size):
    for i in range(1, base_size + 1):
        print(' ' * (base_size - i), end='')
        print('*' * i)
        
        
def mario_from_list(l):
    '''
    print the mario pyramid based on a list of empty string
    Args:
        lst (list): list of empty strings
    Returns:
        None
    '''
    for i in range(1, len(l) + 1):
        l[-i] = '*'
        print(''.join(l))