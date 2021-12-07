# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
	def totalFruit(self, fruits: List[int]) -> int:
		if len(fruits)<=2: return len(fruits)
		# 2 pointers
		l, r = 0, 0
		dic = {} #hashmap for the right most index
		res = 1
		for i, f in enumerate(fruits):
			dic[f]= i
			r = i
			if len(dic)>2:
				low = min(dic, key=lambda x: dic[x])
				l = dic[low]+1
				del dic[low]
			res = max(res, r-l+1)
			
		return res
