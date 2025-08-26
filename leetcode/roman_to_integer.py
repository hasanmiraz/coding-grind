# 6ms
class Solution1:
    def romanToInt(self, s: str) -> int:
        roman_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0

        for i in range(len(s)):
            if i + 1 < len(s) and  roman_mapping[s[i]] < roman_mapping[s[i+1]]:
                result -= roman_mapping[s[i]]
            else:
                result += roman_mapping[s[i]]
        
        print(result)
        return result
    
# 2ms
class Solution2:
    def romanToInt(self, s: str) -> int:
        roman_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0

        for a, b in zip(s, s[1:]):
            if roman_mapping[a] < roman_mapping[b]:
                result -= roman_mapping[a]
            else:
                result += roman_mapping[a]
        
        print(result + roman_mapping[s[-1]])
        return result + roman_mapping[s[-1]]

# 0ms
class Solution3:
    def romanToInt(self, s: str) -> int:
        roman_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        last = 0

        for i in reversed(s):
            current = roman_mapping[i]

            if current < last:
                result -= current
            else:
                result += current
                last = current
        
        print(result)
        return result
    
obj1 = Solution1()
obj2 = Solution2()
obj3 = Solution3()

obj1.romanToInt("III") # 3
obj1.romanToInt("LVIII") # 58
obj1.romanToInt("MCMXCIV") # 1994
print("")
obj2.romanToInt("III") # 3
obj2.romanToInt("LVIII") # 58
obj2.romanToInt("MCMXCIV") # 1994
print("")
obj3.romanToInt("III") # 3
obj3.romanToInt("LVIII") # 58
obj3.romanToInt("MCMXCIV") # 1994
