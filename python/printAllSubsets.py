def subSets(input, sofar):
    if len(input) == 0:
        print sofar
        return
    else:
        temp = input.pop()

        subSets(input,sofar)
        sofar.append(temp)
        subSets(input, sofar)
        sofar.remove(temp)

        input.append(temp)

if __name__ == '__main__':
    l = '123'
    li = list(l)
    s = set(li)
    userin = list(s)
    print subSets(userin,[])
    
    
# Answer:
# 
# []
# ['1']
# ['3']
# ['3', '1']
# ['2']
# ['2', '1']
# ['2', '3']
# ['2', '3', '1']
