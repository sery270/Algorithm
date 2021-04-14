# 😇 세리의 Algorithm 공부😇

코딩 테스트 대비로 시작했는데, 나름 재밌게 게임 하듯 공부하고 있는 알고리즘님! 잘 부탁해 !


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

## Algorithm 스터디 TIL(Today I Learned)

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


### 🎮 2021/04/14 수
- 주언어 python으로 다시 돌아왔습니다. C++도 좋긴하지만이 아니라 나빴습니다..
- [Python 자료형에 대한 정리](https://github.com/sery270/Algorithm/blob/master/Docs/python%20%EC%9E%90%EB%A3%8C%ED%98%95.md)
