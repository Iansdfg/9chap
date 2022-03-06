from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        cour_to_indegree, pre_to_cour = self.get_indegree(numCourses, prerequisites)
        starts = [cour for cour, indegree in enumerate(cour_to_indegree)  if cour_to_indegree[cour] == 0]
        queue = deque(starts)
        order = []
        while queue:
            cour = queue.popleft()
            order.append(cour)
            for next_cour in pre_to_cour[cour]:
                cour_to_indegree[next_cour] -= 1 
                if cour_to_indegree[next_cour] == 0:
                    queue.append(next_cour)
        if len(order) == numCourses:
            return order
        return []

    def get_indegree(self, numCourses, prerequisites):
        cour_to_indegree = [0 for n in range(numCourses)]
        pre_to_cour = {x:[] for x in range(numCourses)}
        for cour, pre in prerequisites:
            cour_to_indegree[cour] += 1 
            pre_to_cour[pre].append(cour)
        return cour_to_indegree, pre_to_cour
