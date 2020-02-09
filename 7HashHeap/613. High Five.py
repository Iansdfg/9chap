'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
from heapq import heapify, heappop

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        id_to_scores = dict()
        for result in results:
            if result.id not in id_to_scores:
                id_to_scores[result.id] = [-result.score]
            else:
                id_to_scores[result.id].append(-result.score) 
        print(id_to_scores)
        
        id_to_high_five = dict()
        for key in id_to_scores:
            id_to_high_five[key] = self.find_one_ave(id_to_scores[key])

        return id_to_high_five
    
    
    def find_one_ave(self, array):
        heapify(array)
        summ = 0
        for i in range(5):
            summ += -heappop(array)
        return summ/5
            
        
