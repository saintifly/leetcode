class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasLen = len(gas)
        if gasLen == 0:
            return -1
        for i in range(gasLen):
            if gas[i]-cost[i] < 0:
                continue
            gasLeaveResult = gas[i]-cost[i]
            for j in list(range(i+1,gasLen))+list(range(gasLen)):
                if gasLeaveResult >= 0 and j==i:
                    return i
                if gasLeaveResult < 0:
                    break
                gasLeaveResult = gasLeaveResult + gas[j] - cost[j]
        return -1