package java_notes;

import java.util.Date;
import java.awt.*;

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
      String message = "hello"; 
      System.out.println(message);
   } 
} 
 
