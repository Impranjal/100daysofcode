class Solution {
public:
    vector<int> runningSum(vector<int>& a) {
        int n=(int)a.size();
        int sum=0;
        for(int i=0;i<n;i++)
        {
            sum=sum+a[i];
            a[i]=sum;
        }
        return a;
    }
};