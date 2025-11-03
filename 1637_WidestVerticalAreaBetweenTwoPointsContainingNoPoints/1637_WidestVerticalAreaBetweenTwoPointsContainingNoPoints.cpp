class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> arr;
        for (int i=0; i<points.size(); i++) {
            arr.push_back(points[i][0]);
        }
        sort(arr.begin(),arr.end());
        int max_diff = 0;
        int diff;
        for (int i=1; i<arr.size(); i++) {
            diff = abs(arr[i]-arr[i-1]);
            if (max_diff<diff) {
                max_diff = diff;
            }
        }
        return max_diff;
    }
};
