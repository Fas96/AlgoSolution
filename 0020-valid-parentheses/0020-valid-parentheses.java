class Solution {
    public boolean isValid(String s) {
         Stack<Character> lifo= new Stack<>();
        for (Character c : s.toCharArray()) {
            if (c=='('||c=='['||c=='{'){
                lifo.push(c);
            }else {
                if (lifo.isEmpty()) return false;
                Character pop = lifo.pop();
                if (c==')'&&pop!='(') return false;
                if (c==']'&&pop!='[') return false;
                if (c=='}'&&pop!='{') return false;
            }
        }
        return lifo.isEmpty();
    }
}