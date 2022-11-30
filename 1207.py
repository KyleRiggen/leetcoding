from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        
        cnt_list = [item[1] for item in cnt.items()]
        
        set_list = list(set(cnt_list))
        
        print(set_list)
        
        if len(cnt_list) != len(set_list):
            return False
        
        return True