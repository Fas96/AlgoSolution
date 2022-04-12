class Solution {
    public int countHillValley(int[] nums) {
        Slop lastSlop = null;
        int count = 0;
        for (int i = 1; i < nums.length; i++)
        {
            Slop slop = null;
            if (nums[i-1] < nums[i])
            {
                slop = Slop.Up;
            }
            else if (nums[i-1] > nums[i])
            {
                slop = Slop.Down;
            }

            if ((lastSlop != null) && (slop != null) && (lastSlop != slop))
            {
                count++;
                lastSlop = slop;
            }
            else if (lastSlop == null)
            {
                lastSlop = slop;
            }

        }
        return count;
    }

    enum Slop
    {
        Down,
        Up
    }
}