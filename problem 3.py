n = int(input('Enter the elements of list: '))
blist = []
for i in range(1, n+1):
    e = input(f'Element {i}: ')
    blist.append(int(e))    
alist = []
for j in blist:
    if j not in alist:
        alist.append(j)
print(f'Input: {blist}')
print(f'Output: {alist}')