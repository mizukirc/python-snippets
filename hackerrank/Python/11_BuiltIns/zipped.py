in_size = input().split()
in_size = list(map(int, in_size))
scores = list()

for i in range(in_size[1]):
    scores_horizontal = input().split()
    scores_horizontal = list(map(float, scores_horizontal))
    scores.append(scores_horizontal)
    
scores_T = list( zip(*scores) )
scores_list = list(map(sum, scores_T))
result_list = list(map(lambda x: x/in_size[1], scores_list))
result = [round(result_list[i],2) for i in range(len(result_list))]
[print(i) for i in result]
