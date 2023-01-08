package java_notes;
import java.util.Arrays;
import java.util.Date;
import java.awt.*;
import java.text.NumberFormat;

// We need a return type in Java 
// Void is a reserve keyword in Java 
// Every Java program should have a function called main 

// Class is a container for related fuctions 
// When a fuction belongs to a class we call it a method 
// When naming a class we use the PascalNamingConvention (first letter of every word should be uppercased) 
// When naming methods we use the camelNamingConvention (first letter of every word should be uppercased except first letter)

// We need an access modifier so we put that inside our class and method declarations (public or private)
// We terminate statements with ;

// Primitive Types- Type | Bytes | Range
// byte | 1 byte | [-128, 127]
// short | 2 byte | [-32k, 32k]
// int | 4 byte | [-2B, 2B]
// long | 8 byte |
// float | 4 byte 
// double | 8 byte 
// char | 2 byte | A,B,C...
// boolean | 1 byte | true/false  

// sout print shortcut
// fori for loop shortcut

public class Main {
   public static void main(String[] args) {
      // when you initialized variables you need to declare type  
      // you can use _ to separate every 3 digets 
      // if number is over 2 billion we need to use long  ex: long viewCount = 3_213_213_321L;
      // float ex: float price = 10.99F;
      // letters are surrounded with single quote while words are surrounded with double quotes.
      // ex char letter = 'A';
      // booean are lowercase on Java instead of capital on python
      int age = 30;
      age = 35;
      Date now = new Date();
      System.out.println(age);
      System.out.println(now);
      // point 1 would print out [x=2, y=1]
      Point point1 = new Point(1,1);
      Point point2 = point1;
      point2.x = 2;
      System.out.println(point1);
      // initialize string .length() .indexOf()(return -1 if index doesnt exist) .replace(target, replacement) .toLowerCase() .trim()
      // if you wanna use quotation marks we use back slash \
      String message = "hello"; 
      System.out.println(message);
      // Arrays have a fixed length in Java 5 is the length of the array 
      // .length() and .sort() important 
      int [] numbers = new int[5];
      numbers[0] = 2;
      System.out.println(Arrays.toString(numbers));
      // Array part 2 use curly brackets if you know what is inside the array
      int [] numbers2 = {1,2,3,4,5};
      System.out.println(Arrays.toString(numbers2));
      // 2 dimensional arrays row x column
      int [][] twoDimensionArray = new int[2][3];
      int [][] twoDimensionArray2 = {{1,2,3}, {1,2,3}};
      System.out.println(Arrays.deepToString(twoDimensionArray));
      System.out.println(Arrays.deepToString(twoDimensionArray2));
      //constants final- makes value not be able to change (By convention final constants are capitalized)
      final float PI = 3.14F;
      System.out.println(PI);
      // diving by doubles and floats 
      double result = (double)10/(double)3;
      float result2 = (float)10/(float)3;
      System.out.println(result);
      System.out.println(result2);
      //Integer.parseInt(), Double.parseDouble() 
      String x = "1";
      int y = Integer.parseInt(x) + 2;
      System.out.println(x);
      System.out.println(y);
      // Math.round(), Math.ceil(), Math.floor(), Math.min(x,y), Math.max(x,y), Math.random() * range you want it to produce
      int round = Math.round(1.7F);
      int ceiling = (int)Math.ceil(1.1F);
      double random = Math.random() * 100;
      System.out.println(round);
      System.out.println(ceiling);
      System.out.println(random);
      // formatting Numbers- NumberFormat.getCurrencyInstance() and NumberFormat.getPercentInstance()
      //Two ways to write it
      NumberFormat currency = NumberFormat.getCurrencyInstance();
      String currencyResult = currency.format(123456.847);
      String percentResult = NumberFormat.getPercentInstance().format(.9);
      System.out.println(currencyResult);
      System.out.println(percentResult);
   } 
} 
 
