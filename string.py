def most_frequent(s):
    t=s.split()
    delimiter= ''
    s=delimiter.join(t)
    l=list(s) #['j', 'a', 'n', 'k', 'o', 's', 'i', 'e', 'n', 'a', 'p', 'i', 'v', 'o']
    f=[]
    for i in l:
        f.append(l.count(i)) # [1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2]
    tup=zip(f,l)
    tup.sort(reverse=True)
    res=[]
    for freq,letter in tup:
        if letter not in res:
            res.append(letter)
    print res # ['o', 'n', 'i', 'a', 'v', 's', 'p', 'k', 'j', 'e']


def main():
    s='janko sie na pivo'
    most_frequent(s)

if __name__ == '__main__':
    main()
