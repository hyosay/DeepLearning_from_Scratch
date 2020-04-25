sequence = [1, 3, 2]

def almostIncreasingSequence(sequence):

    droppped = False
    last = prev = min(sequence) - 1#0
    for i in sequence:
        if i <= last:
            if droppped:
                return False
            else:
                droppped = True
            if i <= prev:
                prev = last
            elif i >= prev:
                prev = last = i
        else:
            prev,last = last,i
    return True


