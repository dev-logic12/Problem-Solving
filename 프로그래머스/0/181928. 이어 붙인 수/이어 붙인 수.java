class Solution {
    public int solution(int[] num_list) {
        StringBuilder evenStr = new StringBuilder();
        StringBuilder oddStr = new StringBuilder();

        for(int num : num_list) {
            if(num % 2 == 0) {
                evenStr.append(num);
            } else {
                oddStr.append(num);
            }
        }
        
        int even = evenStr.length() > 0 ? Integer.parseInt(evenStr.toString()) : 0;
        int odd = oddStr.length() > 0 ? Integer.parseInt(oddStr.toString()) : 0;

        return even + odd;
    }
}
