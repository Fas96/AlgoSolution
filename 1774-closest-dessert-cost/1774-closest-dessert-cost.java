class Solution {
     public int closestCost(int[] baseCosts, int[] toppingCosts, int target) {
         int n = baseCosts.length;
        int m = toppingCosts.length;

        int[] toppingCount = new int[m];
        Map<String, Integer> dp = new HashMap<>();
        int closest = Integer.MAX_VALUE;

        // start the recursion with choosing a base already since a base is mandatory
        for(int baseCost : baseCosts) {
            int cost = dfs(baseCost, dp, toppingCosts, target, toppingCount, baseCost, 0);
            closest = getClosest(cost, closest, target);
        }

        return closest;
    }

    public int dfs(
            int base,
            Map<String, Integer> dp,
            int[] toppingCosts,
            int target,
            int[] toppingCount,
            int currCost,
            int currIdx
    ) {
        if(currCost >= target) return currCost;
        if(currIdx >= toppingCount.length) return currCost;
        String key = String.valueOf(base) + "," + String.valueOf(currCost) + "," + String.valueOf(currIdx);
        if(dp.containsKey(key)) return dp.get(key);
        int closest = Integer.MAX_VALUE;

        for(int i = currIdx; i < toppingCosts.length; i++) {
            if(toppingCount[i] < 2) { // we can only have 2 of the same toppings
                toppingCount[i]++; // we want to use this topping, so increment
                int cost1 = dfs(base, dp, toppingCosts, target, toppingCount, currCost+toppingCosts[i], currIdx);
                closest = getClosest(cost1, closest, target);
                toppingCount[i]--; // backtrack
            }
            // cost2 is the 2nd choice at every recursion. We can choose not to add a topping
            int cost2 = dfs(base, dp, toppingCosts, target, toppingCount, currCost, currIdx+1);
            closest = getClosest(cost2, closest, target);
        }
        dp.put(key, closest);
        return closest;
    }

    public int getClosest(int cost, int currentClosest, int target) {
        int closest = currentClosest;
        if(Math.abs(target-cost) == Math.abs(target-closest)) {
            closest = Math.min(cost, closest); // choose the smaller one per the question requirements
        }

        if(Math.abs(target-cost) < Math.abs(target-closest)) {
            closest = cost;
        }
        return closest;
    }
}