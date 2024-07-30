class Solution {
    public int[][] solution(int[][] arr) {
        int rows = arr.length;
        int cols = arr[0].length;
        int max = Math.max(rows, cols);
        int[][] result = new int[max][max];

        for (int i = 0; i < rows; i++) {
            System.arraycopy(arr[i], 0, result[i], 0, cols);
        }
        return result;
    }
}
