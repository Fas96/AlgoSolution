class Solution {
    public List<Integer> topStudents(String[] positive_feedback, String[] negative_feedback, String[] report, int[] student_id, int k) {
 Set<String> positiveFeedbackSet = new HashSet<>();
        Set<String> negativeFeedbackSet = new HashSet<>();
        for (int i = 0; i < positive_feedback.length; i++) {
            positiveFeedbackSet.add(positive_feedback[i]);
        }
        for (int i = 0; i < negative_feedback.length; i++) {
            negativeFeedbackSet.add(negative_feedback[i]);
        }
        PriorityQueue<Pair> pq = new PriorityQueue<>((pair1, pair2) -> {
            if (pair1.score > pair2.score) {
                return -1;
            } else if (pair2.score > pair1.score) {
                return 1;
            } else {
                if (pair1.student_id > pair2.student_id) {
                    return 1;
                } else if (pair1.student_id < pair2.student_id) {
                    return -1;
                } else {
                    return 0;
                }
            }
        });
        for (int i = 0; i < report.length; i++) {
            String reportForStudent = report[i];
            String[] words = reportForStudent.split(" ");
            int score = 0;
            for (String word : words) {
                if (positiveFeedbackSet.contains(word)) {
                    score = score + 3;
                }
                if (negativeFeedbackSet.contains(word)) {
                    score = score - 1;
                }
            }
            Pair pair = new Pair(score, student_id[i]);
            pq.offer(pair);
        }
        List<Integer> result = new ArrayList<>();
        while (k != 0) {
            if (pq.isEmpty()) {
                break;
            }
            Pair pair = pq.poll();
            result.add(pair.student_id);
            k = k - 1;
        }
        return result;
    }
	class Pair {
        public int score;
        public int student_id;
        public Pair(int score, int student_id) {
            this.score = score;
            this.student_id = student_id;
        }
    }
}