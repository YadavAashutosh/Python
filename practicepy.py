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