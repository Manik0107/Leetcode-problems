class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if(asteroids[i] < 0):
                while stack and stack[-1] < abs(asteroids[i]) and stack[-1] >= 0:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
                if stack[-1] == abs(asteroids[i]):
                    stack.pop()
            else:
                stack.append(asteroids[i])
        return stack
                    
                