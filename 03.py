import math

def solve_ndrome(path):
    with open(path, 'r') as f:
        a = f.read()

    a = a.splitlines()

    for line in a:
        check_ndrome(line)

def check_ndrome(line):
    l = line.split('|')

    word = l[0]
    ndrome = int(l[1])

    sections = int(math.ceil(len(word) / ndrome))

    sword = []
    
    for section in range(0, sections):
        sword.append(word[section*ndrome:section*ndrome+ndrome])

    n = True
    for k,v in enumerate(sword):
        if sword[k] != sword[-k-1]:
            n = False

    if n:
        print "%s|%d|1" % (word, ndrome)
    else:
        print "%s|%d|0" % (word, ndrome)

if __name__ == '__main__':
    solve_ndrome('ActualInput.txt')
