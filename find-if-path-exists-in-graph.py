class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        unionSet = {i:i for i in range(n)}
        size = [1 for i in range(n)]
        # print(unionSet)

        def representative(member):
            if member == unionSet[member]:
                return member
            
            unionSet[member] = representative(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            repMember1 = representative(member1)
            repMember2 = representative(member2)

            if repMember1 != repMember2:
                if size[repMember1] < size[repMember2]:
                    unionSet[repMember1] = repMember2
                    size[repMember2] += size[repMember1]
                else:
                    unionSet[repMember2] = repMember1
                    size[repMember1] += size[repMember2]

        for member1, member2 in edges:
            union(member1, member2)
        

        print(unionSet)
        if representative(source) == representative(destination):
            return True
        return False