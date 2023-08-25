from collections import deque

def solution(begin_word, target_word, word_list):
    answer = 0
    queue = deque()
    queue.append([begin_word, 0])
    visited = [0 for _ in range(len(word_list))]
    
    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == target_word:
            answer = steps
            break
        
        for i in range(len(word_list)):
            diff_count = 0 
            
            if not visited[i]:
                for j in range(len(current_word)):
                    if current_word[j] != word_list[i][j]:
                        diff_count += 1  
                
                if diff_count == 1: 
                    queue.append([word_list[i], steps + 1])
                    visited[i] = 1
    
    return answer
