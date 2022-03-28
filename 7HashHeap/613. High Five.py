import heapq 
'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        id2scores = dict()
        for record in results:
            if record.id in id2scores:
                id2scores[record.id].append(-record.score)
            else:
                id2scores[record.id] = [-record.score]
        
        res = dict()
        for key in id2scores:
            avg = self.get_high5(id2scores[key])
            res[key] = avg
        return res

    def get_high5(self,scores):
        heapq.heapify(scores)
        summ = 0
        for _ in range(5):
            summ -= heapq.heappop(scores)
        return summ * 1.0 /5




