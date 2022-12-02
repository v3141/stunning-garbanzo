class Solution:
    def aboveBelow(self, nums, threshold):
        numAbove = numBelow = 0
        for num in nums:
            if num > threshold:
                numAbove += 1
            elif num < threshold:
                numBelow += 1
        
        return { "above": numAbove, "below": numBelow }
    

    def stringRotation(self, string, rot):
        rot = rot % len(string)

        rev = string[::-1]
        first = rev[:rot][::-1]
        last = rev[rot:][::-1]
        return first + last
    

sol = Solution()
ans = sol.aboveBelow([1, 5, 2, 1, 10], 6)
ans2 = sol.stringRotation("MyString", 2)
print(ans)
print(ans2)
