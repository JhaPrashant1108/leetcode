class Solution:
    def readBinaryWatch(self, num: int):
        def numTobinary(num):
            flag = True
            counter = 0
            while flag:
                if num>0:
                    if num%2==1:
                        counter+=1
                else:
                    flag = False
                num = num//2
            return counter
  
        output = []
        for i in range(12):
            for j in range(60):
                if numTobinary(i)+numTobinary(j)==num:
                    output.append(str(i)+":"+str(j).zfill(2))

        return output

l = Solution()
print(l.readBinaryWatch(1))