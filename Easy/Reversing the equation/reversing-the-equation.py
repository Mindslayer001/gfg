#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        new_list=[]
        new_str=""
        k=""
        for i in s:
            if i in ["+","-","*","/"]:
               new_list.append(k)
               new_list.append(i)
               k=""
            elif i.isnumeric() :
                k=k+i
            else:
                s.replace(i,"")
        new_list.append(k)
        new_list.reverse()
        new_str="".join(new_list)
            
        return new_str
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends