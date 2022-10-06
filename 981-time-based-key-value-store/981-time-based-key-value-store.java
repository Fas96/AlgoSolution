class TimeMap {

    HashMap<String, Map<String ,Integer>> map;
        public TimeMap() {
            map = new HashMap<>();
        }

        public void set(String key, String value, int timestamp) {
            if(!map.containsKey(key))map.put(key,new HashMap<>());
            map.get(key).put(value,timestamp);
        }

        public String get(String key, int timestamp) {
            if(!map.containsKey(key))return "";
            Map<String,Integer> m = map.get(key);
            String res = "";
            for(String s : m.keySet()){
                if(m.get(s)<=timestamp && m.get(s)>m.getOrDefault(res,0))res = s;
            }
            return res;
        }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */