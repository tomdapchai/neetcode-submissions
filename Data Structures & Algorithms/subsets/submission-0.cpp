class Solution {
public:
    vector<vector<int>> solveSubset(int n, vector<int> &nums)
{
    if (nums.size() < 1)
        return vector<vector<int>>({{}});
    if (nums.size() == 1)
    {
        vector<vector<int>> res;
        res.push_back(vector<int>({n}));
        res.push_back(vector<int>({nums[0]}));
        res.push_back(vector<int>({n, nums[0]}));
        return res;
    }
    vector<int> sub(nums.begin() + 1, nums.end());
    vector<vector<int>> res = solveSubset(nums[0], sub);
    int size = res.size();
    for (int i = 0; i < size; i++)
    {
        vector<int> dup(res[i]);
        dup.push_back(n);
        res.push_back(dup);
    }
    res.push_back(vector<int>({n}));
    return res;
}

vector<vector<int>> subsets(vector<int> &nums)
{
    if (nums.size() == 0)
    {
        return vector<vector<int>>({{}});
    }
    if (nums.size() == 1)
    {
        return vector<vector<int>>({{}, {nums[0]}});
    }
    
    vector<int> subNum(nums.begin() + 1, nums.end());
    vector<vector<int>> res = solveSubset(nums[0], subNum); 
    res.push_back({});
    return res;
}
};