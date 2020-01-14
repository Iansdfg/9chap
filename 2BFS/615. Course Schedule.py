from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        pre_to_cour = {course: [] for course in range(numCourses)}
        in_degrees = [0 for _ in range(numCourses)]
        
        for course, prere in prerequisites:
            pre_to_cour[prere].append(course)
            in_degrees[course] += 1
            
        queue, count = deque([]), 0
        
        for course in range(numCourses):
            if in_degrees[course] == 0:
                queue.append(course)
            
        while queue:
            curr = queue.popleft()
            count += 1
            for course in pre_to_cour[curr]:
                in_degrees[course] -= 1 
                if in_degrees[course] == 0:
                    queue.append(course)
                    
        return numCourses == count
                
            
                
