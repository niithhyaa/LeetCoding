class Solution {
public:
    bool isPalindrome(int x) {
        if (x==0) {return true;}
        if ((x>0) && (x%10!=0)) {
            long long rev = 0;
            int y = x;
            while (y!=0) {
                int d = y%10;
                rev = rev*10 + d;
                y = y/10;
            }
            return rev == x;
        }
        else {
            return false;
        }
    }
};
