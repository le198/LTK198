n = int(input('Enter the elements of list: '))
blist = []
for i in range(1, n+1):
    e = input(f'Element {i}: ')
    blist.append(int(e))    
s = 0
for j in blist:
    s += j
avg = s/len(blist)
alist = []
for k in blist:
    v = k - avg
    if v >= 0:
        alist.append(v)
    else:
        alist.append(-v)
position = alist.index(min(alist))
print(f'The average value of list is: {avg}')
print(f'The position of the element which has value nearest to the average of the array is: {position}')