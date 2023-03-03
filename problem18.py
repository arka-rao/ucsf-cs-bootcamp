def main():

    def data(test_data):
        l1 = []
        l2 = test_data.strip().split('>')

        for i in l2:
            if len(i):
                clip = i.split()
                a = clip[0]
                b = ''.join(clip[1:])
                l1.append((a, b))

        return l1


    def graph(test_data, n):
        l2 = []

        dna = data(test_data)

        for a1, b1 in dna:
            for a2, b2 in dna:
                if a1 != a2 and b1.endswith(b2[:n]):
                    l2.append((a1, a2))

        return l2
    
    test_data = open('rosalind_grph.txt').read()

    for edge in graph(test_data, 3):
        print edge[0], edge[1]

main()