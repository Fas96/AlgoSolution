class RandomizedSet {

   List<Integer> randomList;
    public RandomizedSet() {
        randomList = new ArrayList<>();
    }

    public boolean insert(int val) {
        if (randomList.contains(val)) {
            return false;
        }
        randomList.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (!randomList.contains(val)) {
            return false;
        }
        randomList.remove((Integer) val);
        return true;
    }

    public int getRandom() {
        return randomList.get((int) (Math.random() * randomList.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */