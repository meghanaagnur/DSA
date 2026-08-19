class Solution {
public:
    int strStr(string haystack, string needle) {
        int loc;
        for(int i=0; i<haystack.size();i++){
            if(haystack.substr(i,needle.length())==needle){
                loc=i;
                return i;
            }
        }
    return -1;
    }
};