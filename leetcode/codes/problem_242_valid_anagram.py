class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n_s = len(s)
        n_t = len(t)
        if n_s != n_t: return False

        s_dict = {}
        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        
        t_dict = {}
        for c in t:
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1

        n_s = len(s_dict)
        n_t = len(t_dict)
        if n_s != n_t: return False

        for k in s_dict:
            if k not in t_dict or t_dict[k] != s_dict[k]:
                return False
        
        return True
