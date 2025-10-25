s = input().strip()
row = int(s[:-1])
l = s[-1]
if 1 <= row <= 2:
    if l in ['A', 'D']:
        print('window')
    else:
        print('aisle')
elif 3 <= row <= 20:
    if l in ['A', 'F']:
        print('window')
    elif l in ['B', 'C', 'D', 'E']:
        print('aisle')
    else:
        print('neither')
elif 21 <= row <= 65:
    if l in ['A', 'K']:
        print('window')
    elif l in ['C', 'D', 'G', 'H']:
        print('aisle')
    else:
        print('neither')

else:
    print('neither')
