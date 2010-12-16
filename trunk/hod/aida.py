'''
Created on Dec 8, 2010
'''

__author__ = 'Bo Zhu, bo.zhu@uwaterloo.ca'
__copyright__ = 'Copyright 2010, University of Waterloo'
__license__ = 'GPL, http://www.gnu.org/licenses/gpl.txt'

def mapping(function, key, iv_len, vars_hod, vars_one = ()): 
    iv = [0] * iv_len
    res = 0
    
    for var in vars_one:
        iv[var] = 1

    for i in xrange(1 << len(vars_hod)):
        for index in vars_hod:
            if iv[index]:
                iv[index] = 0
            else:
                iv[index] = 1
                break
        res ^= function(iv, key)
        
    return res

if __name__ == '__main__':
    pass