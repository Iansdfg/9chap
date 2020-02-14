from collections import defaultdict, deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        pre_to_cours = defaultdict(list)
        in_degree = [0] * numCourses
        
        for prerequisite in prerequisites:
            pre_to_cours[prerequisite[1]].append(prerequisite[0])
            in_degree[prerequisite[0]] += 1 
            
        queue = deque([])
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
            
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for next_cour in  pre_to_cours[curr]:
                in_degree[next_cour] -= 1 
                if in_degree[next_cour] == 0:
                    queue.append(next_cour)
        
        return result if len(result) == numCourses else []
            
