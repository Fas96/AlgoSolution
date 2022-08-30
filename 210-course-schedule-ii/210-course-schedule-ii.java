class Solution {
    
        public int[] findOrder(int numCourses, int[][] prerequisites) {
    int[] table= new int[numCourses];
    for (int[] course : prerequisites) {
      int curCourse= course[0];
      table[curCourse]++;
    }
  
    Set<Integer> noIncomingEdges= new HashSet<>();
    int []res= new int[numCourses];
    int resCnt=0;
    for (int i = 0; i < numCourses; i++) {
      if(table[i]==0)noIncomingEdges.add(i);
    }
   
    //if set is empty that means we have cyclic graph
    if(noIncomingEdges.isEmpty())return new int[]{};
   
            
    while (!noIncomingEdges.isEmpty()){
      Iterator<Integer> it=noIncomingEdges.iterator();
      Integer element=  it.next();
       
      //remove the edges the current element has
      for (int course = 0; course < prerequisites.length; course++) {
        //check if prerequisite is equals to current element
        if(prerequisites[course][1]==element){
          int curCourse=prerequisites[course][0];
          //remove the incoming edges of this current course
          table[curCourse]--;
          if(table[curCourse]==0){
            noIncomingEdges.add(curCourse);
          }
        }
      }
      noIncomingEdges.remove(element);
      res[resCnt++]=element;
    }

    //check if there is cycle
    for (int course :table) {
      if(course>0)return new int[]{};
    }
        
    return  res;

  }
    
}