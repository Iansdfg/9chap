'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        id2heap = dict()
        id2avg = dict()
        for result in results:
            if result.id not in id2heap:
                heap = []
                heapq.heapify(heap)
                id2heap[result.id] = heap

            socres = self.check_or_replace(id2heap[result.id], result.score)
            id2avg[result.id] = sum(socres) * 1.0 / 5
        return id2avg

    def check_or_replace(self, socres, score):
        if len(socres) >= 5:
            mini = heapq.heappop(socres)
            if mini > score:
                score = mini
        heapq.heappush(socres, score)
        return socres

