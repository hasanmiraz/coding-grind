#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
  int romanMapping(char r) {
    switch (r) {
    case 'I':
      return 1;
    case 'V':
      return 5;
    case 'X':
      return 10;
    case 'L':
      return 50;
    case 'C':
      return 100;
    case 'D':
      return 500;
    case 'M':
      return 1000;
    default:
      return 0;
    }
  }

  int romanToInt(string s) {

    int size = s.size();

    if (size == 0) {
      return 0;
    }

    int last = 0;
    int result = 0;

    for (int i = size - 1; i > -1; i--) {
      int current = romanMapping(s[i]);
      if (current < last) {
        result -= current;
      } else {
        result += current;
        last = current;
      }
    }

    return result;
  }
};

int main() {
    Solution s;
    string test[] = {"III", "LVIII", "MCMXCIV"};
    int test_size = sizeof(test) / sizeof(test[0]);

    for (int i = 0; i < test_size; i++) {
        int r  = s.romanToInt(test[i]);
        cout << test[i] << " " << r << endl;
    }
}