class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q=deque(students)
        sw=deque(sandwiches)
        prog=0
 
        while q:
            if q[0]==sw[0]:
                q.popleft()
                sw.popleft()
                prog=0
            else:
                student=q.popleft()
                q.append(student) 
                prog+=1
            if prog>len(q):
                break
           
       
        return len(q)