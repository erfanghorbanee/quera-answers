import java.util.Scanner;
public class factoriel {
	public static void main(String args[]) {
		Scanner s1= new Scanner(System.in);
		int n = s1.nextInt();
		int i = 1;
		int temp =1;
		for(i=1;i<=n;i++) {
			temp*=i;
		}
		System.out.print(temp);
	}

}