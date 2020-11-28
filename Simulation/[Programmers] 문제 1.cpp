#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool tg = true; // true -> 1; false -> 0
bool now = true;
bool did = false;
int cnt = 0;
int num = cnt;
string answer = "";

string solution(string src) {
    int size = src.length();

    answer += src[0];

    tg = (src[0] == '1') ? true: false;

    for(int i =0; i<size; i++){
        now = (src[i] == '1') ? true: false;


        if(tg == now){
            cnt++;
            tg = now;
        }else{

            cout << char(cnt+64);
            answer += char(cnt+64);
            cnt = 0;
            cnt++;
            tg = now;
        }

    }
    answer += char(cnt+64);





    return answer;
}