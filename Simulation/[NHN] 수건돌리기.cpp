#include <iostream>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <utility>
using namespace std;



void solution(int numOfAllPlayers, int numOfQuickPlayers, char *namesOfQuickPlayers, int numOfGames, int *numOfMovesPerGame) {
  // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
    
    vector<pair<char, int>> mem(numOfAllPlayers);
    pair<char, int> tmp,tagger; //술래가 정한 사람, 술래
    
    //게임 자리는 mem의 1~numOfAllPlayers-1로 생각한다. 0은 술래자리!
    for(int i = 0; i<numOfAllPlayers-1; i++){
        mem[i] = make_pair(char(66+i), 0);
    }

    for (int i= 0; i< numOfQuickPlayers; i++) {
        int ix = (int)namesOfQuickPlayers[i];
        //절대 술래가 되지 않는 QuickPlayers들 구분
        mem[ix-66].second = -1;
        //printf("ㅇㄴㄹㅁ%c %d\n", mem[i].first, mem[i].second);
    }

    //항상 술래는 A부터 시작한다.
    tagger = make_pair('A', 1);
    int next = 0;//, st = 1;
    for(int i =0; i<numOfGames; i++){

        
        //시계 방향
        if(numOfMovesPerGame[i] > 0){
            //수건을 둔 자리
            next = (numOfMovesPerGame[i]%(numOfAllPlayers-1) + next)%(numOfAllPlayers-1);
            
            //잡힘: 자리 이동
            if(mem[next].second != -1){
                mem[next].second++;
                tmp = mem[next]; // 잡힌 사람
                mem[next] = tagger; // 잡힌 사람 자리에 술래가 앉음
                tagger = tmp; //잡힌 사람은 술래가 된다.
         
            }else{ //잡히지 않음: next만 업데이트 됨 자리 이동 없음
                tagger.second++;
     
            }
            
        }else{ //반시계 방향
            //수건을 둔 자리
            next = ((((numOfAllPlayers-1)+numOfMovesPerGame[i]%(numOfAllPlayers-1)))%(numOfAllPlayers-1) + next)%(numOfAllPlayers-1);
            //잡힘: 자리 이동
            
            if(mem[next].second != -1){
                mem[next].second++;
                tmp = mem[next]; // 잡힌 사람
                mem[next] = tagger; // 잡힌 사람 자리에 술래가 앉음
                tagger = tmp; //잡힌 사람은 술래가 된다.

            }else{ //잡히지 않음: next만 업데이트 됨 자리 이동 없음
                tagger.second++;
         
            }
        }
        
        
    }
    
    
    for(int i = 0; i<numOfAllPlayers-1; i++){
        if(mem[i].second == -1){
            printf("%c %d\n", mem[i].first, 0);
        }else{
            printf("%c %d\n", mem[i].first, mem[i].second);
        }
        
    }
    
    printf("%c %d\n", tagger.first, tagger.second);
    

}

struct input_data {
  int numOfAllPlayers;
  int numOfQuickPlayers;
  char *namesOfQuickPlayers;
  int numOfGames;
  int *numOfMovesPerGame;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.numOfAllPlayers;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.numOfQuickPlayers;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
  for (int i = 0; i < inputData.numOfQuickPlayers; i++) {
    iss >> inputData.namesOfQuickPlayers[i];
  }

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.numOfGames;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  inputData.numOfMovesPerGame = new int[inputData.numOfGames];
  for (int i = 0; i < inputData.numOfGames; i++) {
    iss >> inputData.numOfMovesPerGame[i];
  }
}

int main() {
  struct input_data inputData;
  process_stdin(inputData);

  solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
  return 0;
}
