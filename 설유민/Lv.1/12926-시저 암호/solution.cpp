#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for (int i = 0; i < s.length(); i++) {
        if ((65 <= s[i]) && (s[i] <= 90)) {
            answer.push_back((s[i] + n - 65) % 26 + 65);
        }
        else if ((97 <= s[i]) && (s[i] <= 122)) {
            answer.push_back((s[i] + n - 97) % 26 + 97);
        }
        else {
            answer.push_back(s[i]);
        }
    }
    return answer;
}