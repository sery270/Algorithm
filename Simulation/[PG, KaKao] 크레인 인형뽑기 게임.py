def solution(board, moves):
    answer = 0
    cart = [-1]
    for m in moves:
        for i in range (len(board)):
            if board[i][m-1] != 0:
                if cart[-1] == board[i][m-1]:
                    print(cart)
                    cart = cart[0:-1]
                    print(cart)
                    answer += 2
                else:
                    cart.append(board[i][m-1])
                board[i][m-1] = 0
                break
            else:
                continue
    return answer
'''
        0 0 0 0 0
        0 0 1 0 3
        0 2 5 0 1
        0 2 4 4 2
        3 5 1 3 1
    m = 1
    b[i][0] 
    move    : [1, 5, 3, 5, 1, 2, 1, 4] 
    cart    : -1 4 
    res : 4
23:57
~
12:35
1. Problem is...?
    - 떠트려진 인형의 개수를 리턴 
    - 0은 빈칸, 나머지 숫자는 인형 
2. TC
    tc1)
        0 0 0 0 0
        0 0 1 0 3
        0 2 5 0 1
        4 2 4 4 2
        3 5 1 3 1
            
        0 0 0 0 0
        0 0 0 0 0
        0 0 5 0 0
        0 2 4 0 2
        0 5 1 3 1
        
    move: [1, 5, 3, 5, 1, 2, 1, 4] 
    tmp : 4 3 1 1 3 2 0 4
    res : 4
    
    tc2)
        0 0 0 0 0 
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        
    move    : 1 2 3 4 5 
    tmp     : 0 0 0 0 0
    res     : 0 
    
    tc3)
        1 1 1 1 1 0
        1 1 1 1 1 1
        1 1 1 1 1 2
        1 1 1 1 1 3
        1 1 1 1 1 4 
        0 1 2 3 4 
    move    : 1 2 3 
    tmp     : 1 1 1
    res     : 2

3. Brain Storming
    1. 인형 뽑기
        moves -> 
        board[][]의 스펙 
        
        지정된 한 열에서 인형을 뽑는다
        board[0][0]
        board[1][0]
        board[2][0]
        board[3][0]
        board[4][0]
        
        => board[iter][move[iter]-1]
        
        - 인형이 있다
            m == move[i]
            for m in move:
                for i in range (len(board)):
                    if board[i][m-1] != 0:
                        // add cart
                        board[i][m-1] = 0
                    else:
                        continue
            
            
        
        - 인형이 없다 
        
        
    2. 인형 바구니에 쌓기 
        cart = []
        
        cart.append(board[i][m-1])
    3. 터트리기 
        answer
        if cart[-1] == board[i][m-1]:
            cart = cart[0:-1]
            answer += 1
        else:
            cart.append(board[i][m-1])
        
4. Summarize
            cart = []
            for m in move:
                for i in range (len(board)):
                    if board[i][m-1] != 0:
                        if cart[-1] == board[i][m-1]:
                            cart = cart[0:-1]
                            answer += 1
                        else:
                            cart.append(board[i][m-1])
                        board[i][m-1] = 0
                    else:
                        continue
    
    
    
    
    
    
        
'''