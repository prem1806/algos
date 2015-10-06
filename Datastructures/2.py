class Solution:
    def maxSubArray(self, A):
		maxi = -10e9
		presum = [A[0]]
		for i in range(1, len(A)):
			presum[i] = presum[i-1] + A[i]
		
		for i in range(0, len(A)):
			for j in range(i, len(A)):
				if i == 0:
					h = presum[j]
				else:
					h = presum[j] - presum[i-1]
				if h > maxi:
					maxi = h
		return maxi