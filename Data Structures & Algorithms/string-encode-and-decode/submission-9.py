class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"

        return encoded
        
    def decode(self, s: str) -> List[str]:
        decoded = []

        n = len(s)
        p = 0
        while p < n:
            l = ""
            while s[p] != '#':
                l += s[p]
                p += 1

            p += 1
            decoded.append(s[p:p+int(l)])
            p += int(l)

        return decoded