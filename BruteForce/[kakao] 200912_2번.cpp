#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
int n,m;
string aa = "";
string list = "";
vector<vector<string>> mem;


void func(vector<int> arr, vector<bool> isused, int k){ // 현재 k개까지 수를 택했음.
  if(k == m){ // course[i] 개를 모두 택했으면
      for(int i = 0; i < m; i++){
          aa += list[arr[i]];
      }
      
      
      // arr에 기록해둔 수를 저장, 또는 이미 있으면 ++
      for(int i =0; i<mem[m].size();i++){
          if(mem[m][i].compare(aa) == 0){
              
          }else{
              
          }
      }
      
    return;
  }

  for(int i = 0; i < n; i++){ // 1부터 n까지의 수에 대해
      cout << "ddaf" << endl;
    if(!isused[i]){ // 아직 i가 사용되지 않았으면
      arr[k] = i; // k번째 수를 i로 정함
      isused[i] = 1; // i를 사용되었다고 표시
      func(arr, isused, k+1); // 다음 수를 정하러 한 단계 더 들어감
      isused[i] = 0; // k번째 수를 i로 정한 모든 경우에 대해 다 확인했으니 i를 이제 사용되지않았다고 명시함.
    }
  }

}


vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    mem.resize(course[course.size()-1]);
    
    for(int i =0; i<orders.size(); i++){
        for(int j =0; j<course.size(); j++){
            list = orders[i];
            n = (int)orders[i].length();
            vector<bool> isused(n); //알파벳이랑 숫자랑 대치시킬 것임
            m = course[j];
            vector<int> arr(m); //course 의 각원소가 들어가야함
            
            //course[i] 개수 만큼의 부분 수열을 찾아서 새로 등록하거나, 이미 해당 부분 수열이 있다면 개수를 추가하는 함수
            func(arr, isused, 0);
        }
        
        
    }
    
    
    
    
    
    
    
    
    
//    signed long size = course.size();
//    vector<vector<string>> mem( size,  vector< string >(1) );
//
//    for(int i = 0 ; i<orders.size(); i++){
//        vector<char> tmp(orders.size());
//        for(int a = 0; a<orders[i].size(); a++){
//            tmp[a] = orders[i][a];
//        }
//
//        for(int j =0; j<course.size(); j++){
//            int cnt = 0;
//            do{
//
//                mem[course[j]][cnt] =
//                cnt++;
//
//            }while(next_permutation(v.begin(),v.end()));
//
//        }
//
//    }
//
//    // 1부터 4까지 저장할 벡터 선언
//    // 배열도 가능!
//    vector<int> v(4);
//
//    // 1부터 4까지 벡터에 저장
//    for(int i=0; i<4; i++){
//        v[i] = i+1;
//    }
//
//    // next_permutation을 통해서 다음 순열 구하기
//    do{
//
//        for(int i=0; i<4; i++){
//            cout << v[i] << " ";
//        }
//
//        cout << '\n';
//
//    }while(next_permutation(v.begin(),v.end()));
//
//
    
    return answer;
}



int main(void){
    solution({"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"}, {2,3,4});
    
//    for(int i =0; i<mem[2].size();i++){
//        cout << mem[2][i];
//    }
    
    
    return 0;
}
