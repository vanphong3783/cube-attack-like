'''
Created on Nov 19, 2010

@author: zhuzhuor
'''

def rounds(iv, key, num_rounds):  
    s = list(key) + [0] * 13 + list(iv) + [0] * 112 + [1, 1, 1]
    for i in xrange(num_rounds):
        t1 = s[65]  ^ s[92] ^ (s[90]  & s[91])  ^ s[170]
        t2 = s[161] ^ s[176] ^ (s[174] & s[175]) ^ s[263]
        t3 = s[242] ^ s[287] ^ (s[285] & s[286]) ^ s[68]
        
        s.pop()
        s.insert(0, t3)
        s[93] = t1
        s[177] = t2
    
    return s[65]  ^ s[92] ^ s[161] ^ s[176] ^ s[242] ^ s[287]
        
    
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
    stream = []
    for i in range(288 * 4, 288 * 4 + 128):
        stream.append(rounds(iv, key, i))
    #print key
    print __stream2str(stream) 
