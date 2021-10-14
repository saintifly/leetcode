class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        out = []
        order = []
        for i in nums1:
            for j in nums2:
                out.append([i,j])
                order.append(i+j)
        b=sorted(enumerate(order), key=lambda x:x[1])
        out_k = []
        print(b)
        num_out = k
        if len(b)<k:
            num_out =len(b)
        for i in range(num_out):
            out_k.append(out[b[i][0]])
        return out_k