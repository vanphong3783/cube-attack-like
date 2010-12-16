#!/bin/sh python

'''
Created on Dec 8, 2010
'''

__author__ = 'Bo Zhu, bo.zhu@uwaterloo.ca'
__copyright__ = 'Copyright 2010, University of Waterloo'
__license__ = 'GPL, http://www.gnu.org/licenses/gpl.txt'

DEBUG = True

from ciphers import trivium as cipher
cipher.iv_len = 80
cipher.key_len = 80

from hod.aida import mapping
#from hod.cube import mapping

from properties.linearity import testing

from data import cube_attack_table1 as table

import time

if __name__ == '__main__':  
    for entry in table:
        key_indices = entry[0]
        iv_hod = entry[1]
        num_rounds = entry[2]
        
        if 3 == len(entry):
            iv_one = []
        else:
            iv_one = entry[3]
    
        function = lambda iv, key: cipher.rounds(iv, key, num_rounds)
        
        mapped_fun = lambda input: mapping(function, input, cipher.iv_len, iv_hod, iv_one)
        
        if DEBUG:
            print key_indices,
#            pass
        else:
            log = open('log.txt', 'a')
            log.write(str(key_indices))
            log.close()
        times = testing(mapped_fun, key_indices, cipher.key_len, 100)
        if times:
            if DEBUG:
                print 'failed', times, 'times',
#                print str(times) + ',',
            else:
                log = open('log.txt', 'a')
                log.write('failed %d times' % times)
                log.close()
        else:
            if DEBUG:
                print 'passed',
            else:
                log = open('log.txt', 'a')
                log.write('passed')
                log.close()
        if DEBUG:
            print '\t(' + str(time.ctime()) + ')\n'
#            pass
        else:
            log = open('log.txt', 'a')
            log.write('\t(' + str(time.ctime()) + ')\n\n')
            log.close()
            
    print 
    print 'Done!'
