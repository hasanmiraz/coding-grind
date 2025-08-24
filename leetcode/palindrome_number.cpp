#include <iostream>
using namespace std;

class Solution {
public:
  bool isPalindrome(int x) {
    if ((x < 0) || (x % 10 == 0 && x != 0)) {
      return false;
    }

    int rev_half = 0;

    while (x > rev_half) {
      rev_half = rev_half * 10 + x % 10;
      x = x / 10;
    }

    if ((rev_half == x) || (rev_half / 10 == x)) {
      return true;
    } else {
      return false;
    }
  }
};

int main() {
  Solution s;
  bool output;
  int testNum[] = {121, -121, 752439789, 0, 10};
  int textNumSize = sizeof(testNum) / sizeof(testNum[0]);

  for (int i = 0; i < textNumSize; i++){
    output = s.isPalindrome(testNum[i]);
    cout << output << endl;
  }
}