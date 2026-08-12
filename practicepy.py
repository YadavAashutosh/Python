# swap 2 number 

a= 10 
b=12

a,b = b,a

print(a,b)

# two sum 

def twosum(nums , target):

    dict1 = {}

    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in dict1:
            return [dict1[rem], i]
        dict1.update({nums[i]:i})
    
print(twosum([2,7,11,15],9))
print(twosum([3,7,11,15],9))

# sort an array 

class BubSort:
    def s(self,nums):
        for i in range (len(nums)):
            isswap = False
            for j in range (1,len(nums)):
                if nums[j]<nums[j-1]:
                    temp = nums[j]
                    nums[j]=nums[j-1]
                    nums[j-1]=temp
                    isswap=True
            if isswap == False:
                break
        return nums


ob = BubSort()
print(ob.s([1,2,3,1,4,5,0]))

# binary search 

class BinarySearch:

    def search(self,nums,target):
        l=0
        r=len(nums)-1

        while l<=r:

            mid = (l+r)//2

            if nums[mid] > target :
                r= mid -1
            elif nums[mid]<target:
                l=mid +1
            else : 
                return mid
        return -1
ob = BinarySearch()
print(ob.search([0, 1, 1, 2, 3, 4, 5] , 6))
print(ob.search([0, 1, 1, 2, 3, 4, 5] , 5))

# fizzbuzz

class Solution:
    def fb(self,n):
        ans= []
        for i in range (1,n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else :
                ans.append((i)) 
        return ans

a=Solution()
print(a.fb(10))


#sorted , join , split , strip , map 

lst  = [ 1,2,0,7,5,6]
print(sorted(lst))

strg = "  ashu"
print(strg.strip())

print(list(map(str , lst)))

j = "".join(list(map(str,lst)))
print(j)
print("hello ashu how are u ".split())

# group anagram

class GrpAnagram:
    def ang (self,lst ):
        dict1= {}
        for i in lst :
            s = sorted(i)
            j = "".join(s)
            if j in dict1.keys() :
                dict1[j].append(i)
            else:
                dict1.update({j:[i]})
        return list(dict1.values())
ob = GrpAnagram()
print(ob.ang(["eat","tea","tan","ate","nat","bat"]))

# palindrome 
def palindrome(x):
   temp = x
   rev = 0 
   while temp >0:
        rev = rev*10 + temp%10
        temp = temp // 10
   return rev == x

print(palindrome(1234321))
print(palindrome(123421))

#fibbonacci 

def fib(n):
    if n==0:
        return 0
    a=0
    b=1
    
    for i in range (n-1):
        c=a+b
        a=b
        b=c
    return b 

print(fib(5))

# full fib 
def fib(n):
    if n==0:
        print("0")
    a=0
    b=1
    for i in range(n):
        print(a , end = " ")
        a,b = b,a+b
fib(6)

# class fib 
class Fibs:
    
    def fib(self, n):
        if n==0:
            return 0
        a=0
        b=1
    
        for i in range (n-1):
            c=a+b
            a=b
            b=c
        return b
    def fibn (self, n):
        lst = [ ]
        for i in range(n):
            lst.append(self.fib(i))
        return lst 
ob = Fibs()
print(ob.fibn(5))
    
# recursion

class Recur:
    def fib(self,n):
        if n==0 or n==1:
            return n
        return self.fib(n-1) + self.fib(n-2)
ob = Recur()
print(ob.fib(4))


# prime 
 

def prime(n):
    if n<2:
        return False
    for i in range (2,(n//2 +1) ):
        if n%i==0:
            return False
    return True

print(prime(10))

# 12 10
# [0, 1]
# None
# [0, 1, 1, 2, 3, 4, 5]
# -1
# 6
# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
# [0, 1, 2, 5, 6, 7]
# ashu
# ['1', '2', '0', '7', '5', '6']
# 120756
# ['hello', 'ashu', 'how', 'are', 'u']
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# True
# False
# 5
# 0 1 1 2 3 5 [0, 1, 1, 2, 3]
# 3
# False