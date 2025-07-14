/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n){
        int left = 1;
        int right = n;
        int mid = left + (right-left)/2;

        while(left <= right){
            mid = left + (right-left)/2;
            if(isBadVersion(mid)){
                right = mid -1;
            } else{
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean isBadVersion(int mid) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'isBadVersion'");
    }
}