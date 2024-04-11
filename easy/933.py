class RecentCounter:
    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        # Remove pings that are outside the 3000ms window
        while self.pings[0] < t - 3000:
            self.pings.pop(0)
        return len(self.pings)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/number-of-recent-calls/submissions/1229112729?envType=study-plan-v2&envId=leetcode-75
