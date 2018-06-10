import java.util.Arrays;
import java.util.Scanner;
public class CoinChangeProblem {

    /**
     * Implementation of famous dynamic programming problem
     * that aims to find out the maximum number of ways in
     * which a value can be achieved using some fixed valued
     * coins.
     *
     * In the implementation, the time complexity is O(mn)
     * and extra space required is O(n).
     *
     * @param coins
     * @param n
     * @return
     */
    public static int coinChangeProblem(int[] coins, int value) {
        int[] possibilities = new int[value + 1];
        Arrays.fill(possibilities, 0);
        possibilities[0] = 1;
        // Build the possibilities table in bottom-up manner
        // For all coins,
        // Update array if the current coin is capable of
        // incrementing the possibility
        for (int i = 0; i < coins.length; i++) {
            for (int j = coins[i]; j <= value; j++) {
                possibilities[j] += possibilities[j - coins[i]];
            }
        }
        return possibilities[value];
    }

    public static void main(String[] args) {
        int[] coins = {10,5,1};
	Scanner in=new Scanner(System.in);
        int value = in.nextInt();
        System.out.println(coinChangeProblem(coins, value));
    }
}
