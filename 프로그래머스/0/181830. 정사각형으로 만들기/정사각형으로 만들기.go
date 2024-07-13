func solution(matrix [][]int) [][]int {
    row := len(matrix)
    col := len(matrix[0])
    
    for row != col {
        if row < col {
            newSub := make([]int, col)
            matrix = append(matrix, newSub)
            row++
        } else {
            for i := 0; i < row; i++ {
                matrix[i] = append(matrix[i], 0)
            }
            col++
        }
    }
    
    return matrix
}
