class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int n = accounts.size();
        int max=0;
        int wealth=0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<accounts[i].size(); j++) {
                wealth=wealth+accounts[i][j];
            }
            if (max<wealth){
                max = wealth;
            }
            wealth=0;
        }
        return max;
    }
};
