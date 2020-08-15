#include <iostream>
#include <string>
 
using namespace std;
int alpha[27];
int main() {
    string input;
    cin >> input;
    for (int i = 0; i < 26; i++)
        alpha[i] = -1;
    for (int i = 0; i < input.length(); i++)
        if(alpha[input[i] - 97] == -1)
            alpha[input[i] - 97] = i;
    for (int j = 0; j < 26; j++)
        cout << alpha[j] << " ";
    return 0;
}