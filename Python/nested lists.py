if __name__ == '__main__':
    name_score_list = []

    # n = input()
    # name_score_list = [input(), float(input()) for _ in range(n)]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score_list.append([name,score])
    
    score_list = sorted(set([score[1] for score in name_score_list]))
    second_low = score_list[1]
    
    second_low_name_list = [row[0] for row in name_score_list if row[1] == second_low]
    print('\n'.join(sorted(second_low_name_list)))