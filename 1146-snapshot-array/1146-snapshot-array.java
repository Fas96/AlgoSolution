class SnapshotArray {

    HashMap<Integer, Integer>[] snapshotMap;
    int snapID;
    
    public SnapshotArray(int length) {
         snapID = 0;
        snapshotMap = new HashMap[length];
        for(int i=0; i<length; i++) snapshotMap[i] = new HashMap<>();
    }

    public void set(int index, int val) {
        snapshotMap[index].put(snapID, val);
    }

    public int snap() {  
        return (++snapID) - 1;
    }

    public int get(int index, int snap_id) {
        while(snap_id >= 0) {
            if(snapshotMap[index].containsKey(snap_id)) return snapshotMap[index].get(snap_id);
            snap_id -= 1;
        }
        return 0;
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */