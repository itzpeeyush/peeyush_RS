1.
from collections import deque

def deepest_nesting(lst):
    queue = deque([(lst, 1)])  
    max_depth = 1

    while queue:
        current_list, depth = queue.popleft()
        max_depth = max(max_depth, depth)

        for item in current_list:
            if isinstance(item, list):  
                queue.append((item, depth + 1))

    return max_depth

nested_list =  [35, [48,[78,[99,[67,[],],],],82],58]
print(deepest_nesting(nested_list))  




2.
def split_list(nums, k):
    left, right = max(nums), sum(nums)  
    best_max_sum = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_partition(nums, k, mid):
            best_max_sum = mid 
            right = mid - 1
        else:
            left = mid + 1
    
   
    sublists = []
    current_sublist = []
    current_sum = 0
    
    for num in nums:
        if current_sum + num > best_max_sum:
            sublists.append(current_sublist)
            current_sublist = [num]
            current_sum = num
        else:
            current_sublist.append(num)
            current_sum += num
            
    sublists.append(current_sublist)  
    
    return sublists


nums = [777, 20, 55, 81,94,10,22,33,44,82,56,78,98,54]
k = 5
print(split_list(nums, k))  


3.
lst = [('a', 1), ('b', 2), ('a', 3)]
result = {}

for key, value in lst:
    if key in result:
        result[key].append(value)  
    else:
        result[key] = [value]  

print(result)


4.
import random

def shuffle_restricted(lst):
    n = len(lst)
    shuffled = lst[:]

   
    for i in range(n):
        swap_idx = random.randint(0, n - 1)
        shuffled[i], shuffled[swap_idx] = shuffled[swap_idx], shuffled[i]

    
    for i in range(n):
        if shuffled[i] == lst[i]:  
            
            swap_idx = (i + 1) % n  
            shuffled[i], shuffled[swap_idx] = shuffled[swap_idx], shuffled[i]

    return shuffled


lst = [11, 22, 34, 48, 59]
print(shuffle_restricted(lst))


5.
def encode_string(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        
        if count >= 3:
            result.append(f"{s[i]}{count}")  
        else:
            result.extend([s[i]] * count)  
        
        i += 1 
    
    return "".join(result)


print(encode_string("pppeeeyyyuuussshhh")) 
print(encode_string("rrraaannnaaa"))    
 


6.
def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))  


list1 = [1, 2, 3, 4, 5, 6,7,99,14]
list2 = [4, 5, 6, 7, 8, 9,7,99,13]

print(list_intersection(list1, list2)) 



7.
def flatten_to_chars(lst):
    result = []
    queue = list(lst) 
    
    while queue:
        item = queue.pop(0)  
        if isinstance(item, list):  
            queue = item + queue  
        else:
            result.extend(item)  
    
    return result


nested_list = ["pee", "yush", ["ra", "na"]]
print(flatten_to_chars(nested_list))  


8.
def to_acronym(words):
    return "".join(word[0].upper() for word in words)

words = ["peeyush", "priyadarshan", "Irana"]
print(to_acronym(words))  




9.
from collections import Counter

def are_anagrams(s1, s2):
    if len(s1) != len(s2): 
        return False
    
    freq1 = Counter(s1)  
    freq2 = Counter(s2) 
    
    return freq1 == freq2  


print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))   


10.
def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(lst)  
    return expected_sum - actual_sum 


n = 5 
lst = [1, 2, 3, 4]  
print(find_missing_number(lst, n)) 
