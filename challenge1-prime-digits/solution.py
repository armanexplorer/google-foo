import math

def solution(i):
    # pre-defined vars
    primes = [2]
    lengths = [1]
    
    # i is between 0 and 10000
    # convert i to 1-index (length-based)
    i += 1
    
    # fill tables
    fill_arrs(primes=primes, lengths=lengths)
    
    # find the first prime number index we use it to fill our ans
    ind = bin_search(lengths, i, 0, len(lengths)-1)
    if lengths[ind] >= i:
        floor_ind = ind-1
    else:
        floor_ind = ind
    
    # init 
    needed_digits = 5
    ans = ""
    
    # set where we should start filling
    dif = i - lengths[floor_ind]
    if dif < 0:
        c = floor_ind
    else:
        c = floor_ind + 1
    
    # fill from middle to end
    x = str(primes[c])
    ans = x[dif-1:dif-1+needed_digits]
    needed_digits -= len(ans)
    c += 1
    
    # fill from start to end
    while needed_digits != 0:
        x = str(primes[c])
        if needed_digits < len(x):
            ans = ans + x[:needed_digits]
            needed_digits = 0
        else:
            ans = ans + x
            needed_digits = needed_digits - len(x)
        c += 1
    
    return ans
    
def fill_arrs(primes, lengths):
    for i in range(3, 20232):
        is_prime = True
        for j in primes:
            if j > math.sqrt(i):
                break
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            lengths.append(lengths[-1]+len(str(i)))

def bin_search(l, x, head, tail):
    if tail <= head:
        return head
    
    mid = (tail+head)//2
    t = l[mid]
    if x == t:
        return mid
    elif x > t:
        return bin_search(l, x, mid+1, tail)
    else:
        return bin_search(l, x, head, mid-1)
