class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0) && search(board, word, i, j, 0)) return true;
            }
        }
        return false;
    }

    private boolean search(char[][] board, String word, int i, int j, int index) {
        if (index == word.length()) return true;
        if (isBoundaryCharCheck(board, word, i, j, index)) return false;
        char temp = board[i][j];
        board[i][j] = ' ';
        boolean found = isFoundInAnyDirections(board, word, i, j, index);
        board[i][j] = temp;
        return found;
    }

    private boolean isFoundInAnyDirections(char[][] board, String word, int i, int j, int index) {
        return search(board, word, i + 1, j, index + 1) ||
                search(board, word, i - 1, j, index + 1) ||
                search(board, word, i, j + 1, index + 1) ||
                search(board, word, i, j - 1, index + 1);
    }

    private static boolean isBoundaryCharCheck(char[][] board, String word, int i, int j, int index) {
        return i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(index);
    }

}    