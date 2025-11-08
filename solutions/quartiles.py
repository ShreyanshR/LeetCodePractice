def quartiles(arr, freq):
    

    res = []

    for num, fre in zip(arr, freq):
        #print(num, fre)
        res.extend([num]*fre)

    
    #print(arr)

    q1_med, q2_med, q3_med = 0, 0, 0

    res = sorted(res)
    print(res)
    #print(arr)

    def median(x):
        len_arr = len(x)
        print(len_arr//2)


        if len_arr%2 == 0:
            return (x[len_arr//2] + x[len_arr//2 - 1])/2
        else:
            return x[len_arr//2]

    n = len(res)

    q2_med = median(res)

    if n%2 == 0:
        q1_med = median(res[0:n//2])
        q3_med = median(res[n//2+1:])
    else:
        q1_med = median(res[0:n//2])
        q3_med = median(res[n//2+1:])

    print(f'q1: {q1_med}')
    print(f'q2: {q2_med}')
    print(f'q3: {q3_med}')


def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)/len(arr)
    
    dist_from_mean = 0
    
    for num in arr:
        print(num)
        dist_from_mean += (num - mean) **2
        
    stdev = (dist_from_mean/len(arr))**(1/2)
    
    print(f"{stdev:.1f}")




if __name__ == '__main__':
    arr = [3, 7, 8, 5, 12, 14, 21, 13]
    arr1 = [1,2,3,4]
    freq = [2,2,2,2]

    values = [6, 12, 8, 10, 20, 16]
    freqs = [5, 4, 3, 2, 1, 5]

    quartiles(values, freqs)

    #arr2 =[10, 40, 30, 50, 20]

    #stdDev(arr2)