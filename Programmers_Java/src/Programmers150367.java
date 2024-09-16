import java.util.*;

class Solution {
    static int[] decToBin(long n) {
        LinkedList<Integer> temp = new LinkedList<>();
        int count = 0;

        while (n > 0) {
            temp.offer((int) (n % 2));
            count++;
            n /= 2;
        }

        int nodeCount = 1;
        int leafCount = 1;

        while (nodeCount < count) {
            leafCount *= 2;
            nodeCount += leafCount;
        }

        int[] result = new int[nodeCount];
        int index = nodeCount - 1;

        while (!temp.isEmpty()) {
            result[index--] = temp.poll();
        }

        return result;
    }

    static int check(int[] binNumber, int left, int right) {
        /*
        반환값
        0 : 정상 더미 트리 (더미 노드로만 이루어진 트리)
        1 : 정상 찐 트리
        -1 : 이상한 트리 (더미 노드 하위에 찐 노드가 있는 경우)
        */
        if (left == right) {
            return binNumber[left];
        }

        int root = (left + right) / 2;
        int leftSubTree = check(binNumber, left, root - 1);
        int rightSubTree = check(binNumber, root + 1, right);

        if (binNumber[root] == 1) {     // 루트가 찐 노드인 경우
            // 양쪽이 정상 트리인 경우 정상 (찐) 트리
            if (leftSubTree != -1 && rightSubTree != -1) return 1;
            else return -1;
        } else {                        // 루트가 더미 노드인 경우
            // 양쪽 서브트리가 모두 정상 더미 트리일 경우에만 정상 (더미) 트리
            if (leftSubTree == 0 && rightSubTree == 0) return 0;
            else return -1;
        }
    }

    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            int[] binNumber = decToBin(numbers[i]);
            // System.out.println("binNumber " + Arrays.toString(binNumber));
            int result = check(binNumber, 0, binNumber.length - 1);
            // System.out.println("result " + result);
            answer[i] = result != -1 ? 1 : 0;
        }

        return answer;
    }
}
