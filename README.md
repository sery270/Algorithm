# 😇 세리의 Algorithm 공부😇

코딩 테스트 대비로 시작했는데, 나름 재밌게 게임 하듯 공부하고 있는 알고리즘님! 잘 부탁해 !

## Algorithm 스터디 TIL(Today I Learned)

### 🎮 2022/03/26 토
- 올해 sk1,2차에 이은 3번째 코테 ! 라인 공채 코테를 보았다. 생각보다 초반 문제 난이도는 쉽게 느껴졌다. 라고 할 뻔~~ 후반부에 시간이 애매하게 30분 남아서 푼 문제들 TC를 왕창 적고 돌려보다가 3개 정도의 예외처리를 추가했다. 내 로직은 항상 ["콩쥐야 조때써"](https://www.youtube.com/watch?v=IoYACdKipKs)의 상황과 같고, 그렇게 TC 검증 단계의 중요성을 다시 깨달았다. 
- 2번 문제.. 효율성을 고려하지 않은 부분이 아쉬웠다. itertools를 사용했는데, 별다른 방법이 생각이 나지 않았다는 것이다. 뭔가 카카오 작년 공채 양궁게임이랑 비슷한 느낌의 문제였다. 
- 작년에 비해, 아니 당장 2주전과 비교해서라도 피지컬이 많이 좋아진 것 같다. 기나긴 구현 문제를 읽고 소화하기 + 파이선의 다양한 활용법 암기 + 포기하지 않고 부분 코드들 제작하고, 조합하기 + 차분하게 TC작성 및 디버깅하기 등등의 액션이 실전에서도 적용되었다는 의미이다. 좋은 방향이라 생각든다. 
- 한편 어젯밤부터 오늘 아침까지 알고리즘 책을 보면서 문자열, 우선순위 큐, 투포인터 같은 자료구조나 간단한 알고리즘을 암기하려했는데, 책 따라가다보니 재밌었고, 꾸준히 공부해야할 범위라고 생각했다.. 평소에 위에서 말했던 피지컬을 유지하면서 알고리즘 책을 꾸준히 읽고 싶어졌다 ! 음 그리고 굳이 문제를 끝까지 붙잡기보다 다른 사람의 코드를 흡수하는 편이 내 공부법과 잘 맞았다. (못풀겠는거 계속 붙잡는다고 풀리는거 아니고, 오히려 나에게 사기를 떨어뜨리는 행위이다,,)
- 예상했듯이 구현 문제만 와르르 나왔다. 코테 대비한다면, 뭐 구현 중심으로 투포인터, 슬라이딩 윈도우, 자료구조 같은거 공부하고, 알고는 재귀 풀이,,그리고 dfs, bfs, 이진탐색 이면 괜찮지 않나 싶다..(?) 너무 어려운 알고리즘은 실전에서 적용하기도 어려울뿐더러, 실제로 [구현 중심의 문제가 출제한다는 인터뷰](https://engineering.linecorp.com/ko/blog/2020-line-sw-developer-recruit-coding-test/)도 이 주장을 뒷받침한다. 
- 지난 주에 치뤘던 올해 sk 공채 코테에선 프로세스 스케줄링 알고리즘 구현 문제가 나왔었고, 2018 카카오에선 LRU 캐싱 알고리즘 구현 문제가 나왔던걸로 기억한다. 운체에서 등장하는 특정 알고리즘들에 대해서 구현하는 문제 한 번씩 풀어봄직하다. (os 지식, 자료구조 지식, 구현 능력을 확인할 수 있기 때문에 상당히 멋진 코테 주제라고 생각된다.) 

### 🎮 2021/05/09 일

- 오늘은 모의 코딩 인터뷰를 해보았다. 생각보다 유익했다 ! 
- 보통 문제를 보자마자 드는 생각을 바로 코드로 적어왔는데, 이렇게 기존 방식대로 코딩인터뷰를 진행했을때의 문제와 개선 방법을 피드백 받았다.
- 기존 방식의 문제
    - 소통이나 충분한 주석 없이 바로 코드를 작성하기 시작하면, 면접관을 이해시킬 수 없다.
    - 머릿속으로만 생각하면, 예외 TC를 고려하기 어렵다.
    - 질문 없이 문제를 이해하고 넘어가면, 질문자의 의도에 다르게 문제를 풀게 될 수 있다. 수렁으로 빠질 수 있다.
- 개선
    - 코딩 인터뷰는 면접관과 함께 소통하며, 문제를 구체화 시키고 해결해가야하는 시간이다.
    - 핵심은 **시각화**이다. **brain storming한 내용을 sudo 코드로 작성**하는 것 핵심이다. 
    - 아래 방식을 따라가면 좋다. 
        1. Problem is
            - 문제 상세 조건 확인하기
            - **질문하면서 소통**하기
        2. TC
            - **TC를 새로 작성**해가면서 내가 이해한 문제가 맞는지 질문자에게 확인하기
        3. Brain Storming
            - 이해한 문제를 TC가지고 해결하는 과정을 **시각화** 하면서, 솔루션을 도출해내기
        4. Sumarize my idea (Write SUDO Code)
            - 3의 결과에 SUDO를 첨부하기
        5. Write Code 
            - 4를 뼈대로 for문의 인덱스나, 추상적으로 정의만 해뒀던 변수들에 대한 초기화를 하기 (SUDO 코드 보완)
        6. Debuging
            - **2에서 만든 TC로, 3의 방식으로 디버깅하기**
            - 사실 print() 떡칠해서 디버깅하는 것보다, 더 빨리 문제 지점을 찾을 수 있다. 
                - 특히 코드로 구현하면서 발생한 문제라면, 3에서 도출한 방법 그대로 디버깅하는 것이기 때문에 더 효과적으로 구현에 대한 디버깅을 할 수 있는 것이다.
                - 솔루션 자체의 문제일 때도, bottom-up으로 빠짐없이 체크할 수 있기 때문에 효과적이기도 하다. 


### 🎮 2021/05/08 토

- 오늘 카카오 여름 인턴십 코딩테스트를 치뤘다. 예상처럼 구현 문제가 많이 출제되었다. (하)
- 네이버보단 지문도 짧고, 테케도 주어져서 좋았다.
    - 히든 테케 없이 공개된 테케로만 채점이 돼서 맘은 편했으나, 해당 테케 실행 시간이나 등등이 좀 거슬렸다. 
- 네이버때도, 지금도, 항상 커트라인에 애매하게 걸치거나 안된다. 조금만 더,, 조금만 더,,, 피지컬을 내야 안정적인 결과를 얻을 수 있을 것이다. (너무 아쉽다.)
- 그리고 이번에 칭찬하고 싶은 점은, 아무리 빡 구현 문제라 해도, 무조건 문제 말 그대로 빡 구현 하기 보단, 문제를 추상화 시켜서 최소 연산 횟수 방법이나 자료 구조 같은걸 고려하면 풀었다는 점이다.
    -  이러한 접근 방법이 틀리지 않았다는 것에,  가능성을 싣고, 이 가능성을 시간내에 실현하기 위한 피지컬 연습을 많이 해야겠다고 느꼈다. 

### 🎮 2021/04/24 토

- 오늘 네이버 상반기 신입 공채 코딩테스트를 치뤘다. 예상과는 달리 알고리즘을 묻는 문제가 아닌 구현 문제가 많이 출제되었다. 
이 긴 지문을 차분히 빠짐없이 이해할 수 있는지, 로직을 생각할 수 있는지, 그것을 코드로 구현할 수 있는지,  코드로 구현한다면 효율성도 생각해볼 수 있는지 등등을 본다는 느낌으로 응시했던 것 같다. 
- 2번 문제같이 까다로운 문자열 문제를 열심히 봐야겠다 !
- 아무 생각없이 3번 문제에 itertools combinations 를 썼는데, 효율성에 대한 고민도 해봐야겠다.

### 🎮 2021/04/22 목

- PG 단어변환을 풀면서, str의 특정 문자를 삭제하는 두가지 방법을 알게 되었다. 1개의 테스트 케이스를 통과 하지 못하고 있었는데, replace 함수에 대해 잘 모르고 쓴 것이 문제였다. replace와 인덱스 슬라이싱을 활용한 방법은 중복 출현된 문자에 대해서 다른 결과를 가져올 수 있다.
    - 특정 인덱스의 문자를 삭제하기

        ```python
        now_tmp = now[:i] + now[i+1:]
        word_tmp = word[:i] + word[i+1:]
        ```

    - 특정 문자를 모두 삭제하기

        ```python
        # replace는 비파괴적 함수이므로, 새로운 대입이 필요함
        now_tmp = now.replace(now[i],"")
        word_tmp = word.replace(word[i],"")
        ```
- 특정 원소의 값이 리스트의 몇번째 인덱스에 위치하는지 알려주는 함수 find()를 활용한 조건문은 아래와 같다.
    - index(now)는 words에 now가 없을 때 valueError 발생시키므로, if문에 사용할 수 없다.
    - find(now)는 words에 now가 없을 때 -1을 반환하므로, 이를 활용하여 if문에 사용할 수 있다.

    ```python
    # word는 str형 list, str형
    # before는 str형 list
    # now는 str

    # if문에선 0이 false고, 0 이외의 것들은 true이므로, +1을 해서 분기처리 해줌 
    if words.find(now)+1:
      print(words.find(now))
      print("if")
    else:
      print(words.find(now))
      print("else")
    ```

### 🎮 2021/04/21 수

- BOJ 9019를 풀다가, L과 R 연산 (왼쪽 회전, 오른쪽 회전 : 1234 → 2341, 1234 → 4123)을 구현하면서 고통받았었다. 이 **회전 연산을 deque의 rotate를 사용**하여 리펙토링 해보았다. 과정은 아래와 같다.
    - 전체 코드는 [여기에](https://github.com/sery270/Algorithm/blob/master/Note/%5BNOTE%5D%20%ED%9A%8C%EC%A0%84%EC%97%B0%EC%82%B0.py)
    1. 입력된 숫자 N을 str로 표현하기 → N_str

        ```python
        N = int(input()) # input : 12
        print(N)
        print(type(N))
        # 12
        # <class 'int'>

        N_str = str(N)
        print(N_str)
        print(type(N_str))
        # 12
        # <class 'str'>
        ```

    2. len(N_str)에 따라 (N의 자릿수에 따라) 0을 패딩해주기 → 패딩된 N_str

        ```python
        N_str = N_str.zfill(4)
        print(N_str)
        print(type(N_str))
        # 0012
        # <class 'str'>
        ```

    3. N_str을 deque로 표현하기 → N_dq

        ```python
        N_dq = deque(N_str)
        print(N_dq)
        print(type(N_dq))
        # deque(['0', '0', '1', '2'])
        # <class 'collections.deque'>
        ```

    4. N_dq를 회전하기 

        ```python
        N_dq.rotate(1)
        print(N_dq)
        print(type(N_dq))
        # deque(['2', '0', '0', '1'])
        # <class 'collections.deque'>
        ```

    5. N_dq를 다시 int로 변환하기 

        ```python
        N_str = "".join(N_dq)
        print(N_str)
        print(type(N_str))
        # 2001
        # <class 'str'>

        N = int(N_str)
        print(N)
        print(type(N))
        # 2001
        # <class 'int'>
        ```

### 🎮 2021/04/20 화

- 파이선의 **for-else, while-else** 문을 들어보셨나요. 오늘 BOJ 9019를 풀면서 발견한 트릭이다. 각 반복문-else에선, 반복문이 끝까지 정상적으로 돌았을때, else의 내용을 실행한다. 

  - 아래는 for - else 의 예제이다. 반복문이 정상적으로 종료되고 for-else의 else가 실행된 결과이다. 

  ```python
  i = 0
  for i in range(0,5):
    print(f"it's {i}")
    i += 1
  else:
    print('while-else !')
  
  # it's 0
  # it's 1
  # it's 2
  # it's 3
  # it's 4
  # while-else !
  
  
  ```

  - 아래는 while-else의 예제이다. 반복문이 break로 인해 비정상적으로 종료되고 while-else의 else가 실행되지 않았다.

  ```python
  i = 0
  while True :
    print(f"it\'s {i}")
    if i == 5:
      print("it's break time")
      break
    i += 1
  else:
    print('while-else !')
  
  # it's 0
  # it's 1
  # it's 2
  # it's 3
  # it's 4
  # it's 5
  # it's break time
  
  ```

  



### 🎮 2021/04/18 일

- 2178_미로 탐색을 풀면서, **파이선의 for를 통한 리스트 생성 방식과 * 를 통한 리스트 생성 방식의 차이점**을 알게되었다. * 를 통한 리스트 생성은 주소까지 복사되어, 추후에 값 초기화시에 원치 않는 위치도 초기화 될 수 있으므로, **for를 통한 리스트 생성을 사용해야겠다고 결론**지었다.
    1. **for를 통한 리스트 생성**

        ```python
        before = [[[0] for _ in range(5) ]for _ in range(7)] 
        before[0][0] =(1,2)
        print(before)
        ```

        ```python
        [
        [(1, 2), [0], [0], [0], [0]], 
        [[0], [0], [0], [0], [0]], 
        [[0], [0], [0], [0], [0]], 
        [[0], [0], [0], [0], [0]], 
        [[0], [0], [0], [0], [0]], 
        [[0], [0], [0], [0], [0]], 
        [[0], [0], [0], [0], [0]]
        ]
        ```

    2. **\* 를 통한 리스트 생성**

        ```python
        before = [[0] * (5)] * (7)
        before[0][0] =(1,2)
        print(before)
        ```

        ```python
        [
        [(1, 2), 0, 0, 0, 0], 
        [(1, 2), 0, 0, 0, 0], 
        [(1, 2), 0, 0, 0, 0], 
        [(1, 2), 0, 0, 0, 0], 
        [(1, 2), 0, 0, 0, 0], 
        [(1, 2), 0, 0, 0, 0], 
        [(1, 2), 0, 0, 0, 0]
        ]
        ```
### 🎮 2021/04/17 토

- 13919_숨바꼭질4를 풀면서, **파이선에서의 재귀는 최대한 지양**해야겠다는 결론을 내렸다.
    1. 런타임 에러 (RecursionError)의 위험이 있다. 파이선을 재귀 호출 깊이를 제한하면서 발생하는 문제이다. 아래 코드로 재귀 깊이 제한을 풀 수 있긴하다. 

        ```python
        import sys

        MAX = 100000
        sys.setrecursionlimit(MAX*2)
        ```

    2. 파이선에서의 재귀호출은 메모리와 시간 복잡도가 크게 증가하게 한다. 특히 무한루프로 구현할 수 있는 똑같은 동작을 재귀로 구현했을땐, 공간 복잡도(메모리)가 약 2-3배 정도 증가했다. 🥲 

        ![말도 안되는 차이](https://user-images.githubusercontent.com/59532818/115101542-0eed6000-9f80-11eb-92c1-57e4af210fbb.png)
        
        - [[BOJ] 13913_숨바꼭질4.py](https://github.com/sery270/Algorithm/commit/6e91fad2a5a5ccae10fb38d410bfe4cf13a86aee)

            ```python
            # 메모리 36628 KB
            # 시간 256 ms

            k = K
              while 1:
                if before[k] == N:
                  path.append(before[k])
                  break
                path.append(before[k])
                k = before[k]
            ```
        - [[BOJ] 13913_숨바꼭질4_recursion.py](https://github.com/sery270/Algorithm/commit/aae2502d9720b08c64a1b6a30dcf53eca81b021e)
            ```python
            # 메모리 118284 KB
            # 시간 332 ms

            def find_path(K):
              if before[K] == N :
                path.append(before[K])
                return
              path.append(before[K])
              find_path(before[K])

            find_path(K)
            ```

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

> [PG] k번째 큰수 

> [DOCS] - readme, wiki 작성한 경우

> [CHORE] - 동작에 영향을 주는 코드 변경 없는 변경사항 (주석, 정렬 등등)

> [NOTE] - 알고리즘 노트, 알고리즘 템플릿 작성 

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



