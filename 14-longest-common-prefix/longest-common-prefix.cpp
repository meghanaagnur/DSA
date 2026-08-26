class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        std::string c, add;
        std::string str =strs[0];
        int minlen=200;
        for(int k=0; k<strs.size(); k++){
            if(minlen> strs[k].size()){
                minlen=strs[k].size();
            }
        }
        for(int i=0; i<minlen; i++){
            for(int j=0; j<strs.size(); j++){
                if(str[i]==strs[j][i]){
                }
                else{
                    return c;
                }
                add = strs[j][i];
            }
            c += add;
        }
        return c;
    }
};