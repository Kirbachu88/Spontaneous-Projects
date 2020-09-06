/* *
 * Kirbachu
 * For Fun
 * 8/11/2020
 * 
 * Fizzbuzz
 * Count from 1-100, say Fizz if number is divisible by 3 and Buzz if divisible by 5
 * If a number is divisible by both 3 and 5, say Fizzbuzz
 * */

public class Fizzbuzz
{
	public static void main(String[] args) {
		int x = 1;
		while(x <= 100) // Counting from 1-100
		    if(x % 3 == 0 && x % 5 == 0) {
		        System.out.println("Fizzbuzz");
		        x++;
		    } // Fizzbuzz: divisible by both 3 and 5
            else if(x % 3 == 0) {
                System.out.println("Fizz");
                x++;
            }
            else if(x % 5 == 0) {
                System.out.println("Buzz");
                x++;
            }
            else {
                System.out.println(x);
                x++;
            }
	}
}


