class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> numbers;
        for(int i=0; i<nums.size(); i++){
            if(numbers.find(nums[i])!=numbers.end()){
                return true;
            }
            numbers.insert(nums[i]);
        }
        return false;
    }
};