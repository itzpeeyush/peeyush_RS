1.
from collections import deque

def deepest_nesting(lst):
    queue = deque([(lst, 1)])  
    max_depth = 1

    while queue:
        current_list, depth = queue.popleft()
        max_depth = max(max_depth, depth)

        for i in current_list:
            if isinstance(i, list):  
                queue.append((i, depth + 1))

    return max_depth

nested_list =  [35, [48,[78,[99,[67,[],],],],82],58]
print(deepest_nesting(nested_list))  




3.
L = [('a', 1), ('b', 2), ('a', 3)]
result = {}

for key, value in L:
    if key in result:
        result[key].append(value)  
    else:
        result[key] = [value]  

print(result)


6.
def list_intersection(l1, l2):
    return list(set(l1) & set(l2))  


list1 = [1, 2, 3, 4, 5, 6,7,99,14]
list2 = [4, 5, 6, 7, 8, 9,7,99,13]

print(list_intersection(list1, list2)) 



8.
def to_acronym(words):
    return " ".join(word[0].upper() for word in words)

words = ["peeyush", "priyadarshan", "Irana"]
print(to_acronym(words))  




9.
from collections import Counter

def are_anagrams(s1, s2):
    if len(s1) != len(s2): 
        return False
    
    l1 = Counter(s1)  
    l2 = Counter(s2) 
    
    return l1 == l2  


print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "lleoh"))   


10.
def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(lst)  
    return expected_sum - actual_sum 


n = 5 
lst = [1, 2, 3, 4]  
print(find_missing_number(lst, n)) 
