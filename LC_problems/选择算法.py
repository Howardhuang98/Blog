def selection_sort(a:list):
    for i in range(0,len(a)-1):
        index,min = find_min(a[i+1:len(a)])
        a[i],a[index+i+1] = a[index+i+1],a[i]

    return a




def find_min(a:list):
    min = a[0]
    index = 0
    for i,n in enumerate(a):
        if n < min:
            min = n
            index = i
    return  index,min

if __name__ == '__main__':
    result = selection_sort([31,41,59,26,41,58])
    print(result)