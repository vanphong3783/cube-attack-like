'''
Created on Nov 14, 2010

@author: zhuzhuor
'''

from ctypes import cdll, c_ubyte, c_int
import os
cipher_rounds = cdll.LoadLibrary(os.path.dirname(__file__) + '/Trivium_ctypes.so').rounds

iv_len = 80 #bits
key_len = 80 #bits

def __bits2bytes(bit_stream):
    c_array = c_ubyte * (len(bit_stream) / 8)
    bytes = c_array()
    
    for i in xrange(len(bit_stream) / 8):
        eight_bits = bit_stream[i * 8 : (i + 1) * 8]
        res = 0
        for j in xrange(8):
            res += eight_bits[j] << j
        bytes[i] = res
    
    return bytes
        

def rounds(iv, key, num_rounds):
    assert len(iv) == iv_len
    assert len(key) == key_len
    
    return cipher_rounds(__bits2bytes(iv), __bits2bytes(key), c_int(num_rounds))
    

if __name__ == '__main__':
    def __test2list(s):
        l = []
        while s:
            a = list(bin(int('1' + s[-2:], 16))[3:])
            l += a
            s = s[:-2]
        for i in range(len(l)):
            l[i] = int(l[i])
        return l
        
    def __stream2str(l):
        "is not the inverse of __test2list()"
        s = ''
        while l:
            a = l[:8]
            a.reverse()
            for i in range(8):
                a[i] = str(a[i])
            b = '1' + ''.join(a)
            b = hex(int(b, 2))[3:]
            s += b
            l = l[8:]
        return s
    
    key = __test2list('0F62B5085BAE0154A7FA')
    iv = __test2list('288FF65DC42B92F960C7')
    
    res = []
    for i in range(64):
        res.append(rounds(iv, key, 288*4 + i))
    print __stream2str(res)