class PriorityQueue<T> {
    
    private compare: (a, b) => boolean;
    constructor(param: (a, b) => boolean) {
        this.compare = param;
    }
    
    private heap: T[] = [];
    
    public push(val: T) {
        this.heap.push(val);
        this.up(this.heap.length - 1);
    }


    private up(number: number) {
        if (number == 0) return;
        let parent = Math.floor((number - 1) / 2);
        if (this.compare(this.heap[parent], this.heap[number])) {
            this.swap(parent, number);
            this.up(parent);
        }
    }

    private swap(parent: number, number: number) {
        let temp = this.heap[parent];
        this.heap[parent] = this.heap[number];
        this.heap[number] = temp;
    }
    
    public pop(): T {
        let result = this.heap[0];
        this.heap[0] = this.heap[this.heap.length - 1];
        this.heap.pop();
        this.down(0);
        return result;
    }

    private down(number: number) {
        let left = number * 2 + 1;
        let right = number * 2 + 2;
        let largest = number;
        if (left < this.heap.length && this.compare(this.heap[left], this.heap[largest])) {
            largest = left;
        }
        if (right < this.heap.length && this.compare(this.heap[right], this.heap[largest])) {
            largest = right;
        }
        if (largest != number) {
            this.swap(largest, number);
            this.down(largest);
        }
    }
    
    public peek(): T {
        return this.heap[0];
    }
    
    public size(): number {
        return this.heap.length;
    }
    
    public isEmpty(): boolean {
        return this.heap.length == 0;
    }
}

function topKFrequent(words: string[], k: number): string[] {
   let result: string[] = [];
    let map: Map<string, number> = new Map();
    for (let word of words) {
        map.set(word, (map.get(word) || 0) + 1);
    }
    let candidates: string[] = Array.from(map.keys());
    candidates.sort((w1, w2) => map.get(w1) == map.get(w2) ? w1.localeCompare(w2) : map.get(w2) - map.get(w1));
    for (let i = 0; i < k; i++) {
        result.push(candidates[i]);
    }
    return result;

};