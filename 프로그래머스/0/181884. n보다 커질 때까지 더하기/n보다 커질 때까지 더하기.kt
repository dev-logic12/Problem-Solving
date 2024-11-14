class Solution {
    fun solution(numbers: IntArray, n: Int): Int {
        var answer: Int = 0
        numbers.forEach {
            answer += it
            if (answer > n) return answer
        }
        return answer
    }
}