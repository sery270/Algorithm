# 😇 세리의 Algorithm 공부😇

코딩 테스트 대비로 시작했는데, 나름 재밌게 게임 하듯 공부하고 있는 알고리즘님! 잘 부탁해 !

## Algorithm 스터디 TIL(Today I Learned)

### 🎮 2021/04/15 목
- 요즘 언어들은 좋은 연산자가 많다. 예를 들면 in, not in, is, range 등등 직관적이어서 좋다. collections 너무 좋다.
- BFS 공부하면서, gragh 입력 방식을 정리하고 있는데, 생각보다 정말 다양하다. 
- [알고리즘 풀이를 위한 파이선 표준 라이브러리 6가지에 대한 정리](https://github.com/sery270/Algorithm/blob/master/Docs/%ED%8C%8C%EC%9D%B4%EC%84%A0%20%ED%91%9C%EC%A4%80%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%206%EA%B0%80%EC%A7%80.md)


### 🎮 2021/04/14 수
- 주언어 python으로 다시 돌아왔습니다. C++이 매웠던걸 느꼈습니다.. python으로 알고리즘 푸니 수도 코드만 적는 느낌이라 편하다.
- [Python 자료형에 대한 정리](https://github.com/sery270/Algorithm/blob/master/Docs/%ED%8C%8C%EC%9D%B4%EC%84%A0%20%EC%9E%90%EB%A3%8C%ED%98%95.md)

### 🎮 2020/08/24 월

- [BOJ] 9465_스티커
- [BOJ] 9465_스티커_최적화
- 메모리 최적화 :: 40N Byte → 12N Byte
    - 점수를 담는 배열의 자료형을 long long으로 잘못 사용한 것을 int로 수정
        - 8 Byte → 4 Byte
    - 굳이 윗행, 아랫행 모두 선택되지 않은 경우를 계산하지 않음
        - 8 * 3N Byte → 4 * 2N Byte
- 시간 최적화 :: 4N * max() 호출 → 2N * max() 호출
    - 굳이 윗행, 아랫행 모두 선택되지 않은 경우를 계산하지 않음
        - 3N * max() 호출 → 2N * max() 호출
    - 처음과 끝 열은 무조건 1개가 선택된다는 문제의 성질 → bottom-up 알고리즘이므로, 마지막 열에서의 두가지 분기를 통해 sol 계산
        - N * max() 호출 → 1 * max() 호출
- <img src="https://user-images.githubusercontent.com/59532818/91048122-21fc9a00-e656-11ea-908c-1f05c9e18162.png" width="40%">
- <img src="https://user-images.githubusercontent.com/59532818/91048133-25902100-e656-11ea-96d6-c165a6248743.png" width="40%">



## Algorithm 스터디 conventions

### commit convention

> [BOJ] 9465_스티커

> [Docs] - readme, wiki 작성한 경우

> [Chore] - 동작에 영향을 주는 코드 변경 없는 변경사항 (주석, 정렬 등등)

<br/>

### foldering

> BruteForce : 완전탐색

[BruteForce에 대해 공부하고 정리한 WIKI](https://github.com/sery270/Algorithm/wiki/🔵-brute-force)

> DP : 다이나믹 프로그래밍

[DP에 대해 공부하고 정리한 WIKI](https://github.com/sery270/Algorithm/wiki/🤢-Dynamic-Programing-(DP))

> DataStructure : 자료구조

[자료구조에 대해 공부하고 정리한 WIKI](https://github.com/sery270/Algorithm/wiki/🔶Data-Structure)

> Greedy : 탐욕법

Greedy 알고리즘에 대해 공부하고 정리한 WIKI

> I:O : 입출력, 문자열

[입출력에 대해 공부하고 정리한 WIKI](https://github.com/sery270/Algorithm/wiki/🟥-I,-O-(입출력))

<br/>



