/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function findTarget(root: TreeNode | null, k: number): boolean {
    let set=new Set();
    let queue:Array<TreeNode>=[];
    queue.push(root);
    while(queue.length>0){
        let node=queue.shift();
        if(node==null){
            continue;
        }
        if(set.has(k-node.val)){
            return true;
        }
        set.add(node.val);
        queue.push(node.left);
        queue.push(node.right);
    }
    return false;
};