class Solution {
    public int snakesAndLadders(int[][] board) {
         if (board == null || board.length == 0 || board[0].length == 0) return -1;
        int rows = board.length;
        int cols = board[0].length;
        int endPosition = rows * cols; 
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(1);   
        boolean[] visited = new boolean[endPosition + 1];  

        int moves = 0;
 
        while(!queue.isEmpty())
        {
            int size = queue.size();

            for (int i = 0; i < size; i++)
            {
                int curr = queue.poll(); 
                if (visited[curr])
                {
                    continue;
                }
                visited[curr] = true;

                if (curr == endPosition)
                {
                    return moves;
                }

                for (int dice = 1; (dice <= 6) && (curr + dice <= endPosition);dice++)
                {
                    int next = curr + dice;
                    int val = getCurBoardValue(board, next);

                    if (val > 0)
                    {
                        next = val;
                    }

                    if (!visited[next])
                    {
                        queue.offer(next);
                    }
                }
            }
 
            moves++;
        }

        return -1;
    }

    private int getCurBoardValue(int[][] board, int num) {
        int n = board.length;
        int lastRow = (num - 1) / n;
        int newRow = n - 1 - lastRow;
        int lastCol = (num - 1) % n;
        int newCol = lastRow % 2 == 0 ? lastCol : n - 1 - lastCol;

        return board[newRow][newCol];
    }
}