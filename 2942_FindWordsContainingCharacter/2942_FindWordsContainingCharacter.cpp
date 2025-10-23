class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> indices;
        int n = words.size();
        for (int i=0; i<n; i++) {
            for (char c : words[i]) {
                if (c == x) {
                    indices.push_back(i);
                    break;
                }
            }
        }
        return indices;

    }
};
