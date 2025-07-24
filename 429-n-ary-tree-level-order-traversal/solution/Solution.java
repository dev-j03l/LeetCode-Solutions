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
    public List<List<Integer>> levelOrder(TreeNode root) {
        ArrayDeque<TreeNode> q = new ArrayDeque<>();
        List<List<Integer>> result = new ArrayList<>();

        if(root != null) q.add(root);

        while(!q.isEmpty()){
            int levelLength = q.size();
            List<Integer> levelValues = new ArrayList<>();;
            for(int i =0; i < levelLength; i++){
                TreeNode curr = q.removeFirst();
                if(curr.left != null) q.add(curr.left);
                if(curr.right != null) q.add(curr.right);
                levelValues.add(curr.val);
            }
            result.add(levelValues);
        }

        return result;
    }
}
