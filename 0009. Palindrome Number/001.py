# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         s = str(x)

 
#         for i in range(len(s)//2):
#             if s[i] != s[-1-i]:
#                 return False

#         return True


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         s = str(x)

#         if int(s) - int(s[::-1]):
#             return False
#         else:
#             return True


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         if x - int(str(x)[::-1]):
#             return False
#         else:
#             return True
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


