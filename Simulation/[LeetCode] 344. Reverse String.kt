class Solution {
    fun reverseString(s: CharArray): Unit {
        var start = 0
        var end = s.size - 1
        var tmp = 'a'
        while (end > start) {
            tmp = s[start]
            s[start]= s[end]
            s[end] = tmp
            start++
            end--
        }
        
        
    }
}


// abc 
// start/ end/ tmp
// 0/ 2/ ""
// tmp = a
// cbc
// cba
// 1/1/"a"




// 1. problem is...?
//     a) reverse 
//     b) no not use additional space => O(1) : 입력이 커져도 항상 일정한 공간을 사용해야함 
//     c) can s be null ? , non-null
    
// 2. TC
//     apple => elppa

// 3. brain storming
    
//     s
//             e

//     a p p l e




// space)
// tmp * (N/2) => N * tmp/2 => O(N)

// time)
// helper * (N/2) => O(N)

// ===
// space)
// start, end, tmp => O(1) 

//   s
//       e

// a p p l e
    
    
// time)
// helper * (N/2) => O(N)
    