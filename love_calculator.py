check1 = "true"
check2 = "love"

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

def calculate_love_score(name1, name2):
    
    c1_score = 0
    c2_score = 0
    
    for i in name1:
        for j in check1:
            if i == j:
              c1_score += 1
              
    for i in name2:
        for j in check1:
            if i == j:
              c1_score += 1
    
    for i in name1:
        for j in check2:
            if i == j:
              c2_score += 1
    
    for i in name2:
        for j in check2:
            if i == j:
              c2_score += 1
    
    love_score = str(c1_score) + str(c2_score)
    print("Love Score =",love_score)
    
calculate_love_score(name1, name2)
