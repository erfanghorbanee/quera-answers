import java.util.*;

public class main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		if (T < 0) {
			System.out.print("Ice");
		} else if (T > 100) {
			System.out.print("Steam");
		} else
			System.out.print("Water");
	}

}
