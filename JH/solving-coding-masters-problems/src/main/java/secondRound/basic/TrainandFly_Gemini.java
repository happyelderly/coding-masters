package secondRound.basic;

public class TrainandFly_Gemini {
    public static long calculateFlyDistance(int X, int Y, int Z) {
        if (X <= 0 || Y <= 0 || Z <= 0) {
            throw new IllegalArgumentException("입력값은 모두 양수여야 합니다.");
        }

        long totalSpeed = 2 * (long)Y; // 두 기차의 합쳐진 속도 (long 형으로 변환)
        long collisionTime = X / totalSpeed; // 충돌까지 걸리는 시간
        long flyDistance = collisionTime * Z;
        return flyDistance;
    }

    public static void main(String[] args) {
        int[][] testCases = {
            {100, 50, 75},
            {200, 30, 90},
            {1, 1, 1},
            {1000, 1000, 1000},
            {0, 50, 75},
            {-100, 50, 75},
            {100, 0, 75},
            {100, 75, 75}
        };

        for (int[] testCase : testCases) {
            int X = testCase[0];
            int Y = testCase[1];
            int Z = testCase[2];

            try {
                long result = calculateFlyDistance(X, Y, Z);
                System.out.printf("X=%d, Y=%d, Z=%d: 결과 = %d\n", X, Y, Z, result);
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}