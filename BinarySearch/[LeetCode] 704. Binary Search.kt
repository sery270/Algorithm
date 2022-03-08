class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size-1
        var mid = 0
        var answer = -1

        while (left <= right){
            mid = left + (right-left).div(2)

            if(nums[mid] == target){
                answer = mid
                break
            }
            if(nums[mid] < target){
                left = mid + 1
                continue
            }
            if(nums[mid] > target){
                right = mid -1 
                continue
            }
        }
        return answer
    }
}


// test

// right == left ?
//         r
//     l
//     [0,1]
//     2
//     mid = 1
//     0 == 2


// 1. Problem is...
//     - impl binary search
//     - 0-indexed

// 2. TC
//     tc1)
//     nums        : [0,1,2]
//     target      : 1
//     res         : 1

//     tc2)
//     nums        : [0,1,2]
//     target      : 3
//     res         : -1

//     tc3)
//     nums        : [1]
//     target      : 0
//     res         : -1


// 3. Brain Storming
//     - sorted nums -> binary search

//              m
//         [0,1,2,3,4,5]


//         left = 0
//         right = len(nums)-1
//         answer = -1
//         while left <= right:
//             mid = left + (right-left)//2
//             if mid == target:
//                 answer = mid
//             if mid < target:
//                 left = mid
//             if mid > target:
//                 right = mid

//         return answer 


// 4. Summarize
//     var left = 0
//     var right = nums.size-1
//     var mid = 0
//     var answer = -1
    
//     while (left <= right){
//         mid = left + (right-left)//2
        
//         if(mid == target){
//             answer = mid
//             break
//         }
//         if(mid < target){
//             left = mid
//             continue
//         }
//         if(mid > target){
//             right = mid
//             continue
//         }
//     }
    

            
        





