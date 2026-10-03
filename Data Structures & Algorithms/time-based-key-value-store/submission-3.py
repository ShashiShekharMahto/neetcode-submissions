class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = []
        self.mapping[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        v = self.mapping.get(key, [])
        final_v = ""
        
        l,r = 0, len(v) - 1
        while l<=r:
            m = (l+r)//2
            if v[m][1] <= timestamp:
                final_v = v[m][0]
                l = m + 1
            else:
                r = m-1
        return final_v

        
