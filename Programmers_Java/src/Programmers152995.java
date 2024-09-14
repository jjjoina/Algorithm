import java.util.*;

class Solution {
    public int solution(int[][] scores) {
        int[] wanhoScore = scores[0];

        Arrays.sort(scores, (s1, s2) -> {
            if (s1[0] != s2[0]) return s2[0] - s1[0];
            else                return s1[1] - s2[1];
        });

        // for (int[] score : scores) {
        //     System.out.println(Arrays.toString(score));
        // }

        ArrayList<Integer> incentiveScores = new ArrayList<>();
        int[] standard = scores[0];

        for (int[] score : scores) {
            if (score[0] < standard[0] && score[1] < standard[1]) {
                if (score == wanhoScore) {
                    return -1;
                }
            } else {
                if (score[1] > standard[1]) {
                    standard = score;
                }
                incentiveScores.add(score[0] + score[1]);
            }
        }

        int answer = 1;
        int wanhoScoreSum = wanhoScore[0] + wanhoScore[1];

        for (int score : incentiveScores) {
            if (score > wanhoScoreSum) {
                answer++;
            }
        }

        return answer;
    }
}