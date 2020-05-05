class Solution:
    
    

    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_str(s):
            char_lsit = []
            for i in range(len(s)):
                if s[i] == '#' and char_lsit != []:
                    char_lsit.pop(-1)
                elif s[i] != '#':
                    char_lsit.append(s[i])
            return ''.join(char_lsit)
        newS = get_str(S)
        newT = get_str(T)
        return newS == newT