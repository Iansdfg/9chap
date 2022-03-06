from collections import deque
class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses, prerequisites):
        # write your code here
        cour_to_indegree, pre_to_course = self.get_indegree(num_courses, prerequisites)
        order = []
        start = [key for key in cour_to_indegree if cour_to_indegree[key] == 0]
        queue = deque(start)
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for course in pre_to_course[curr]:
                cour_to_indegree[course] -= 1
                if cour_to_indegree[course] == 0:
                    queue.append(course)
        return len(order) == num_courses
        
    def get_indegree(self, num_courses, prerequisites):
        cour_to_indegree = {i:0 for i in range(num_courses)}
        pre_to_course = {i:[] for i in range(num_courses)}
        for cour, pre in prerequisites:
            cour_to_indegree[cour] += 1 
            pre_to_course[pre].append(cour)
        return cour_to_indegree, pre_to_course
