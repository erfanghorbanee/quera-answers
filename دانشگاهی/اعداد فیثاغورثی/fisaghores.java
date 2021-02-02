import java.util.Scanner;
public class fisaghores {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n1= sc.nextInt();
		int n2= sc.nextInt();
		int n3= sc.nextInt();
		int a = 0 ,b = 0;
		int c=n1;
		if(n2>c) { 
			c=n2;
		    b=n1;}
		else b=n2;
		
		if(n3>c) { 
			c=n3;
			a=n1;
		}
		else a=n3;
		

		if(a*a + b*b == c*c) {
			
			System.out.println("YES");
		}
			
		else System.out.println("NO");
		
	}

}