#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

vector<string> split(string str, char delimiter)
{
    vector<string> internal;
    stringstream ss(str);
    string temp;


    while (getline(ss, temp, delimiter))
    {
        internal.push_back(temp);
    }

    return internal;
}

string dot (string a){
    string answer = "";
    //    3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    
    vector<string> splited = split(a, '.');
    for(int i =0; i< splited.size(); i++){
        if(splited[i].compare("") != 0){
            answer += splited[i];
            answer += '.';
        }
    }
    
    

    return answer;
}


string solution(string new_id) {
    string answer = "";
    
    unsigned long size = new_id.size();
    
    int tmp;

    for(int i =0; i<size; i++){
        tmp = new_id[i];
        //    1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
        if( tmp >= 65 && tmp <=90){
            tmp += 32;
        }
        //    2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
        if((tmp >= 97 && tmp <= 122)|| tmp == 45 || tmp == 95 || tmp ==46 || (tmp >= 48 && tmp <=57)){
            answer += char(tmp);
        }
    }

//    3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    answer = dot(answer);

//    4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    size = answer.size();
    while(answer[size-1] == '.'){
        answer = answer.substr(0,size-1);
    }




//    5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if(answer.size() == 0){
        answer = "a";
    }
    
    size = answer.size();
//    6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if(size >= 16){
        string tmpAnswer = answer;
        answer = "";
        for(int i = 0; i< 15; i++){
            tmp = tmpAnswer[i];
            answer += char(tmp);
        }
    }
    
//         만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    //    4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    size = answer.size();
    while(answer[size-1] == '.'){
        answer = answer.substr(0,size-1);
    }

//    7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    size = answer.size();
    if(size <= 2){
        char tmpAnswer = answer[size-1];
        while(size <= 2){
            answer += char(tmpAnswer);
            size = answer.size();
        }
        

    }


    
    
    return answer;
}

int main(){
    
    cout << solution("z-+.^.");
    return 0;
}
