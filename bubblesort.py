def bubblesort(a):
    j = 1
    while j <= len(a):
        for i in range(0,len(a)-1):
            if a[i+1]<a[i]:
                a[i+1],a[i] = a[i],a[i+1] # swap
        j +=1
        print a

alist = [6,5,4,3,2,1]
bubblesort(alist)