package firstRound.intermediate;

import java.io.IOException;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class GuessingNumbers {

    public int bfs(int s, int g) {
        Queue<int[]> q = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        q.add(new int[]{s, 0});
        visited.add(s);

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int n = cur[0];
            int c = cur[1];
            if (n == g) {
                return c;
            }
            int[] nexts = {n + 1, n - 1, n * 2};
            for (int next : nexts) {
                if (next >= 0 && next <= 100000 && !visited.contains(next)) {
                    visited.add(next);
                    q.add(new int[] {next, c + 1});
                }
            }
        }
        return -1;
    }


    public static void main(String[] args) throws IOException {
        GuessingNumbers main = new GuessingNumbers();
        Scanner scanner = new Scanner(System.in);
        int g = scanner.nextInt();
        int s = scanner.nextInt();
        System.out.println(main.bfs(s, g));

    }
}
