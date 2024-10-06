import java.util.*;

public class main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int x1 = sc.nextInt();
		int y1 = sc.nextInt();
		int x2 = sc.nextInt();
		int y2 = sc.nextInt();
		if (y1 == y2)
			System.out.print("Horizontal");
		else if (x1 == x2)
			System.out.print("Vertical");
		else
			System.out.print("Try again");
	}

}
