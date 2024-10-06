import java.util.Scanner;
public class main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		int i,sum=0;
		 for(i=1;i<n;i++) {
			 if(n%i==0) {
				 sum+=i;
			 }
		 }
		if(sum==n) {
			System.out.println("YES");
		}
		else System.out.println("NO");
	}

}
