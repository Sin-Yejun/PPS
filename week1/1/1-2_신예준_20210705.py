def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        li = []
        for j in i:
            if j in skill:
                li.append(j)
        ct = 0
        if(len(li)==0):
            answer+=1
        else:
            for k in range(len(skill)):
                if skill[k] == li[ct]:
                    ct+=1
                    if(ct == len(li)):
                        answer +=1
                        break
                else:
                    break   
    return answer
