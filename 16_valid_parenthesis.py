class Solution:
    def checkValidString(self, s: str) -> bool:
        os = set([0])
        
        for char in s:
            ns = set()
            if char == '(':
                for v in os:
                    ns.add(v+1)
            elif char == '*':
                for v in os:
                    ns.add(v+1)
                    ns.add(v)
                    if v >0:
                        ns.add(v-1)
            else:
                for v in os:
                    if v>0:
                        ns.add(v-1)
            os = ns
        return 0 in os
                