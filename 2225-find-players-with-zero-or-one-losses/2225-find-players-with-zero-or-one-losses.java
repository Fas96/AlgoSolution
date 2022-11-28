class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
            Map<Integer,int[]> score = new HashMap<>();
        for (   int[] match : matches) {
            int winner = match[0];
            int loser = match[1];
            int[] winnerScore = score.getOrDefault(winner, new int[]{0,0});
            int[] loserScore = score.getOrDefault(loser, new int[]{0,0});
            winnerScore[0]++;
            loserScore[1]++;
            score.put(winner, winnerScore);
            score.put(loser, loserScore);
        } 
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> zeroLoss = new ArrayList<>();
        List<Integer> oneLoss = new ArrayList<>();
        for (int player : score.keySet()) {
            int[] playerScore = score.get(player);
            if (playerScore[1] == 0) {
                zeroLoss.add(player);
            } else if (playerScore[1] == 1) {
                oneLoss.add(player);
            }
        }
        zeroLoss.sort((a,b) -> a - b);
        oneLoss.sort((a,b) -> a - b);
        res.add(zeroLoss);
        res.add(oneLoss);

        return res;

    }
}