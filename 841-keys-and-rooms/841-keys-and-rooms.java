class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
         
         Set<Integer> v= new HashSet<>();
        Queue<List<Integer>> keys= new LinkedList<>();
        keys.add(rooms.get(0));
        v.add(0);
        while (!keys.isEmpty()){
            List<Integer> temp=keys.poll();
            for (int i = 0; i < temp.size(); i++) {
                if (!v.contains(temp.get(i))){
                    v.add(temp.get(i));
                    keys.add(rooms.get(temp.get(i)));
                }
            }
        }
        return v.size()==rooms.size();
    }
}