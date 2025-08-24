#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hashmap;
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
      int comp = target - nums[i];
      if (hashmap.find(comp) != hashmap.end()) {
        result.push_back(hashmap[comp]);
        result.push_back(i);

        return result;
      } else {
        hashmap[nums[i]] = i;
      }
    }
    return result;
  }
};

int main() {
  Solution s;
  vector<int> nums = {2, 7, 11, 15};
  int target = 9;

  vector<int> r = s.twoSum(nums, target);
  cout << "result: ";
  for (int i : r) {
    cout << i << " ";
  }

  cout << endl;

  return 0;
}
