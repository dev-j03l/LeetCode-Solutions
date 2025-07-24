/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.*;

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        ArrayDeque<TreeNode> q = new ArrayDeque<>();
        if(root != null) q.add(root);

        while(!q.isEmpty()){
            TreeNode right = null;
            int levelLength = q.size();
            for(int i = 0; i < levelLength; i++){
                TreeNode curr = q.removeFirst();
                right = curr;
                
                if(curr.left!= null) q.add(curr.left);
                if(curr.right!= null) q.add(curr.right);
            }
            if(right != null) result.add(right.val);
        }
        return result;
    }
}
