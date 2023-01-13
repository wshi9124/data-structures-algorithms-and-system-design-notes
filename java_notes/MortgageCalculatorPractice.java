package java_notes;
import java.util.Scanner;
import java.text.NumberFormat;

class MortgageCalculatorPractice {
    public static void main(String[] args) {
        // avoid magic numbers 
        final byte MONTHS_IN_YEARS = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);
        System.out.print("Principal: ");    
        int principal = scanner.nextInt();

        System.out.print("Annual Interest Rate: ");
        float annualInterest = scanner.nextFloat();
        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEARS;
        
        System.out.print("Period (Years): ");
        byte years = scanner.nextByte();
        int numberOfPayments = years * MONTHS_IN_YEARS;

        double mortgage = principal 
                        * (monthlyInterest * Math.pow(1+ monthlyInterest, numberOfPayments)
                        / (Math.pow(1+ monthlyInterest, numberOfPayments)) -1);
        
        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Mortgage: " + mortgageFormatted);

    }

}