class TimeMap:

    def __init__(self):
        self.keystore = {} #key : list of [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keystore.get(key, []) #if we find  a match return key, else empty list
        
        print(f'length: {len(values)}')
        l, r = 0, len(values) - 1

        while l<=r:
            m = (l+r) // 2
            if values[m][1] == timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

if __name__ == "__main__":
    timeMap = TimeMap()

    timeMap.set("alice", "happy", 1)
    timeMap.set("alice", "happy", 2)
    timeMap.set("alice", "happy", 3)
    timeMap.get("alice", 1)

