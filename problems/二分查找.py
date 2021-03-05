def binary_search(a:list,target:int):
    a = sorted(a)
    Left = 0
    right = len(a)
    index = int((Left+right)/2)
    while a[index]!=target and abs(right-Left)>1:
        if a[index]>target:
            right = index
            index = int((index+Left)/2)
            
        else:
            left = index
            index = int((index+right)/2)

    if a[index]!=target:
        print("target was not found")
    else:        
        return index

if __name__ == "__main__":
    index = binary_search(a=[1,2,4,234,588,6000],target = 234)
    print(index)