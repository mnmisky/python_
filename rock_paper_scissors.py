def calculate_score(list):
    counter = []
    for item in list:
        if item[0] == item[1]:
            counter.append('T')
        if item[0] == 'R' :
            if item[1] == 'P':
                counter.append('B')
            elif item[1] == 'S':
                counter.append('A')

        if item[0] == 'P':
            if item[1] == 'S':
                counter.append('B')
            elif item[1] == 'R':
                counter.append('A')
        
        if item[0] == 'S':
            if item[1] == 'R':
                counter.append('B')
            elif item[1] == 'P':
                counter.append('A')

    abigail = counter.count('A')
    benson = counter.count('B')
    tie = counter.count('T')

    if abigail > benson and abigail > tie:
        return 'Abigail'
    elif benson > abigail and benson > tie:
        return 'Benson'
    else:
        return 'Tie'

    # return counter

mylist = [["R", "P"], ["R", "S"], ["S", "P"]]

result = calculate_score(mylist)

result2 = calculate_score([["R", "S"], ["S", "S"]]) #➞ "Tie"

result3 = calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) #➞ "Tie"



print(result)
print(result2)
print(result3)
