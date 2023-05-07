class Solution {
    public void sortColors(int[] arr) {
        int low=0;
        int high=arr.length-1;
        for (int i = 0; i <=high;) {
            if(arr[i]==0){
                swap(arr,i,low);
                low++;
                i++;
            }else if(arr[i]==1){
                i++;
            }else {
                swap(arr,i,high);
                high--;  
            }
        }
    }
    
    private void swap(int[] arr,int i,int j){
        int tmp=arr[i];
        arr[i]=arr[j];
        arr[j]=tmp;
    }
}