class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length-1;
        while (numbers[i] + numbers[j] > target) j--;
        while (numbers[i] + numbers[j] < target) i++;

        while (i < j){
            if(checkSum(numbers[i], numbers[j], target)) break;
            else if (checkSum(numbers[i+1], numbers[j], target)) {
                i++;
                break;
            } else if (checkSum(numbers[i], numbers[j-1], target)) {
                j--;
                break;
            } else {
                i++;
                j--;
            }
        }
        numbers = new int[2];
        numbers[0] = i+1;
        numbers[1] = j+1;
        
        return numbers;
    }

    private static boolean checkSum(int a, int b, int target){
        if (a + b == target) return true;
        else return false;
    }
}
