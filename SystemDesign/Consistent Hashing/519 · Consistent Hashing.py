class Solution:
    """
    @param n: a positive integer
    @return: n x 3 matrix
             we will sort your return value in output
    """
    def consistent_hashing(self, n):
        # write your code here
        results = [[0,359,1]]
        #result[0], result[1] is #start, #end
        #result[2] is # of machine
        #暴力编号最小的区间with max size
        for i in range(1, n):
            index = 0
            for j in range(i):
                # check size, get result with max size
                j_size = results[j][1] - results[j][0]
                max_size = results[index][1] - results[index][0]
                if j_size> max_size:
                    index = j

            #found machine with max size min id
            start, end = results[index][0], results[index][1]
            results[index][1] = (start + end) / 2
            results.append([(start + end) / 2 + 1, end, i + 1])
        return results

    
    
