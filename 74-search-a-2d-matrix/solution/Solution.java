class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // we could just treat the matrix like a regular array
        // i.e get length and width (m and n)
        // multiply to get array size (m*n) [- 1 for index]
        // set left = 0 right = size-1; // we need to convert this using size-1/n to get
        // row and size-1 % n to get item in row
        // mid = right - left / 2
        // convert that into a 2d access by doing same calc above
        // do binary search
        int m = matrix.length;
        int n = matrix[0].length;
        int size = n * m;
        int left = 0;
        int right = size-1;

        while(left <= right){
            int mid = left + (right - left) / 2;
            if(matrix[mid/n][mid%n] < target){
                left = mid + 1;
            } else if (matrix[mid/n][mid%n] > target){
                right = mid - 1;
            } else if (matrix[mid/n][mid%n] == target){
                return true;
            }
        }
        return false;
    }

}
