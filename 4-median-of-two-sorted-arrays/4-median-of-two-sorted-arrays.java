
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
            
        int k=0;
        int[] array3 = new int[nums1.length+nums2.length];
        for (int i = 0; i < nums1.length; i++) {
            array3[k]=nums1[i];
            k++;
        }
        for (int i = 0; i < nums2.length; i++) {
            array3[k]=nums2[i];
            k++;
        } 
        array3=Arrays.stream(array3).sorted().toArray();
        int arrLength = array3.length;
        int mid = array3.length/2;
        if(arrLength %2==0){
            int midValue = array3[mid];
            int midVal2= array3[mid-1];
            return (double) (midValue+midVal2)/2;
        }else{
            return (double) array3[mid];
        }
    }
}