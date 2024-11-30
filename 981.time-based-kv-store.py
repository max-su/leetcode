import collections

class TimeMap:


    def __init__(self):
        self.key_to_vt = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_vt[key].append((value, timestamp))
        

    def get(self, key: str, target_time: int) -> str:
        if key not in self.key_to_vt:
            return ''

        vt_list = self.key_to_vt[key]
        l, r = 0, len(vt_list) - 1
        
        while l <= r:
            m = (l + r) // 2
            mid_time = vt_list[m][1]
            if mid_time == target_time:
                return vt_list[m][0]
            elif target_time > mid_time:
                l = m + 1
            else:
                r = m - 1

        if r < 0:
            return ''
        return vt_list[r][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)