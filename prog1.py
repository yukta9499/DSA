a = [10,8,9,5,22,29,15,19,27]
min=max= a[0]
smax=smin=a[0]
for i in a:
    if i >max:
        smax=max
        max=i
    elif (i>smax and i!=max):
        smax = i
    if i<min:
        smin=min
        min=i
    elif(i<smin and i!=min):
        smin=i
print("Maximum: ",max)
print("Minimum:",min)
print("Second Minimum:",smin)
print("Second Maximum:",smax)
