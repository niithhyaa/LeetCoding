class Solution {
public:
    string defangIPaddr(string address) {
        string newStr = "";
        for (int i=0; i<address.length(); i++) {
            if (address[i] == '.') {
                newStr.append("[.]");
            }
            else { 
                newStr += address[i];
            }
        }
        return newStr;
    }
};
