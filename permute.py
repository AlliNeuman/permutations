f = open("str.txt", "r")
if f.mode == 'r':
    lines = f.read().splitlines()
    # print lines

    # finding and returning all permutations
    # where char are individual string characters, l is the starting index and r is the ending index
    def permute(char, l, r, permute_list):
        if l==r:
            permutation = ''.join(char)
            permute_list.append(permutation)
            permute_list.sort()

        else:
            for j in range(l, r+1):
                char[l], char[j] = char[j], char[l]
                permute(char, l+1, r, permute_list)
                char[l], char[j] = char[j], char[l]

    #line is the original line of the text file
    #n are how many string characters are in i
    #char are the individual strings that make up i
    for line in lines:
        permute_list = []
        n = len(line)
        char = list(line)
        permute(char, 0, n-1, permute_list)
        print(', '.join(permute_list))
