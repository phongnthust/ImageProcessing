List = [[9, 7, 1, 1, 1, 2, 2, 1],
        [8, 9, 9, 7, 1, 1, 1, 1],
        [7, 8, 9, 7, 1, 2, 1, 1],
        [8, 9, 9, 9, 9, 1, 1, 2],
        [8, 9, 9, 7, 7, 2, 1, 3],
        [9, 9, 9, 9, 8, 2, 2, 1],
        [9, 9, 8, 8, 7, 1, 2, 1],
        [8, 9, 8, 6, 5, 1, 1, 3]
        ];

h = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];


for a in range (10) :
    for i in range(len(List)) :
        for j in range(len(List[0])) :

            if (a == List[i][j]):
                h[a] += 1

for r in h:
    print(r)



