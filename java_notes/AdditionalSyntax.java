package java_notes;

public class AdditionalSyntax {
    public static void main(String[] args) {
        // just like python java has ==, !=, <=, >=
        int x = 1;
        int y = 1;
        System.out.println(x==y);
        // && for and, || for or 
        int temperature = 22;
        boolean isWarm = temperature > 20 && temperature < 30;
        System.out.println(isWarm);
        // if statement java 
        int weather = 10;
        if (weather > 30){
            System.out.println("its a hot day");
            System.out.println("Drink water");
        }
        else if (weather >= 20 && weather <= 30){
            System.out.println("Its a nice day");
        } else{
            System.out.println("Its cold");
        }
        // ternary in Java
        int income = 120000;
        String classname = income > 100000 ? "First" : "Economy";
        System.out.println(classname);

        
        
    }
}
