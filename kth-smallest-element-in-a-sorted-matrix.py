class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                heappush(heap, -1 * matrix[i][j])
                if len(heap) > k:
                    heappop(heap)
                
        return -1 * heap[0]