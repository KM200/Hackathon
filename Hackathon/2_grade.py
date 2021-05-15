def final_grade(grade):
    mod=0
    modified=[]
    for mark in grade:
        if(mark<38):
            modified.append(mark)
        else:
            mod=mark%5
            if((5-mod)<3):
                modified.append(5+(mark-mod))
            else:
                modified.append(mark)
    
    return modified

n=4
marks=[73,67,38,33]
result=final_grade(marks)
print(result)