'''
Created on Dec 8, 2010
'''

__author__ = 'Bo Zhu, bo.zhu@uwaterloo.ca'
__copyright__ = 'Copyright 2010, University of Waterloo'
__license__ = 'GPL, http://www.gnu.org/licenses/gpl.txt'

DEBUG = True

import random

def testing(function, linear_vars, input_dimension, num_testings):
    all_zero = function([0] * input_dimension)
    
    num_failures = 0
    ###
    if DEBUG:
        print
        print '(testing',
    else:
        pass
        log = open('log.txt', 'a')
        log.write('\n(testing ')
        log.close()
    ###
    for i in xrange(num_testings):
        ###
        if DEBUG:
            print i,
        else:
            pass
            log = open('log.txt', 'a')
            log.write(str(i) + ', ')
            log.close()
        ### 
        random_input = [None] * input_dimension
        for j in xrange(input_dimension):
            random_input[j] = random.randrange(2)
        
        for var in linear_vars:
            random_input[var] = 0
        
        if all_zero ^ function(random_input):
            num_failures += 1
            continue
        
        hw_lsb = 0
        for j in xrange(1, 1 << len(linear_vars)):
            for var in linear_vars:
                if random_input[var]:
                    random_input[var] = 0
                    hw_lsb ^= 1
                else:
                    random_input[var] = 1
                    hw_lsb ^= 1
                    break
            if all_zero ^ hw_lsb ^ function(random_input):
                num_failures += 1
                break
    
    ###
    if DEBUG:
        print ')'
    else:
        pass
        log = open('log.txt', 'a')
        log.write(')\n')
        log.close()
    ###
    return num_failures


if __name__ == '__main__':
    pass