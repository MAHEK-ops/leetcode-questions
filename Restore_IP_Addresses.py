class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(start, parts, path):
            if parts == 4 and start == len(s):
                res.append(".".join(path))
                return
            if parts == 4 or start == len(s):
                return
            
            for l in range(1, 4):
                if start + l > len(s):
                    break
                segment = s[start:start+l]
                if (segment.startswith('0') and l > 1) or int(segment) > 255:
                    continue
                backtrack(start + l, parts + 1, path + [segment])
        
        backtrack(0, 0, [])
        return res
