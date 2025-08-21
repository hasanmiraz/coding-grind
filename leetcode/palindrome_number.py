
class Solution_1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        return str(x) == str(x)[::-1]

class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        x_list = str(x)
        for i in range(int(len(x_list)/2)):
            if x_list[i] != x_list[(i+1) * -1]:
                return False

        return True

class Solution_3:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed = 0
        while x > 0:
            digit = x%10
            reversed = reversed * 10 + digit
            x = x // 10
        
        return original == reversed

r = Solution_1().isPalindrome(121)
print(r)
r = Solution_1().isPalindrome(123)
print(r)
r = Solution_1().isPalindrome(-121)
print(r)
print()
r = Solution_2().isPalindrome(121)
print(r)
r = Solution_2().isPalindrome(123)
print(r)
r = Solution_2().isPalindrome(-121)
print(r)
print()
r = Solution_3().isPalindrome(121)
print(r)
r = Solution_3().isPalindrome(123)
print(r)
r = Solution_3().isPalindrome(-121)
print(r)