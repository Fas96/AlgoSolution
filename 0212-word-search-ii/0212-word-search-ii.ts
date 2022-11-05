class Trie {
    nodes = {} as {[index: string]: Trie};
    word = '';
    wordCount = 0;

    addWord(word: string) {
		let trie = this as Trie;
        for(const c of word) {
           if(!trie.nodes[c]) {
               trie.nodes[c] = new Trie();
           } 
           trie = trie.nodes[c];
        }
        trie.word = word;
        trie.wordCount++;
    }
}

function findWord(board: Array<Array<string>>, i: number, j: number,
                   width: number, height: number, node: Trie, words: Array<string>) {
	const c = board[j][i];
	if(c === '$' || !node.nodes[c]) {
		return
	}

	if(node.nodes[c].wordCount > 0) {
        if(words.indexOf(node.nodes[c].word) === -1) {
	        words.push(node.nodes[c].word);
        }
	}

	board[j][i] = '$';
	if(i+1 < width) {
		findWord(board, i+1, j, width, height, node.nodes[c], words);
	}
	if(j+1 < height) {
		findWord(board, i, j+1, width, height, node.nodes[c], words);
	}
	if(i > 0) {
		findWord(board, i-1, j, width, height, node.nodes[c], words);
	}
	if(j > 0) {
		findWord(board, i, j-1, width, height, node.nodes[c], words);
	}
	board[j][i] = c;
}

function findWords(board: string[][], words: string[]): string[] {
    const root = new Trie();
    for(const word of words) {
        root.addWord(word);
    }
    let found = new Array<string>();
    const height = board.length;
    const width = board[0].length;
    for(let j = 0; j < height; j++) {
    	for(let i = 0; i < width; i++) {
		    findWord(board, i, j, width, height, root, found);
	    }
    }
    
    return found;
};