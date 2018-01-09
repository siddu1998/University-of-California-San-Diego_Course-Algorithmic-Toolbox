import java.util.Scanner;
class euclid
{
	public static int eculid_rec(int a,int b)
	{
		return b==0?a:eculid_rec(b,a%b);
	}
	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		num1=in.nextInt();
		num2=in.nextInt();
		if(num2>num1){
		System.out.println(eculid_rec(num1,num2));
	}
	else{
		int temp=num2;
		num2=num1;
		num1=temp;
				System.out.println(eculid_rec(num1,num2));
	
}
}
}
