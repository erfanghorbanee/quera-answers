import java.util.Scanner;
public class main {
	public static void main(String args[]) {
		Scanner a=new Scanner(System.in);
		int n=a.nextInt(),tul=0;
		int m=n;
		int i,j,h;
		while(0<n) {
			n=n/10;
			tul=tul+1;
		}
		
		int[] Array = new int[tul];
		if(tul>=0 && tul<100) {
		for(i=m;i>0;i=i/10){
			int g=0;
			Array[tul-1]=i%10;	
			tul--;
		}
		for(j=0;j<Array.length;j++) {
		System.out.print(Array[j]+": ");
		for(h=0;h<Array[j];h++) {
			System.out.print(Array[j]);
		}
		System.out.println();
		}
		
		}
		
		
		
		
		
		
		
	
		}
		
	}
	


