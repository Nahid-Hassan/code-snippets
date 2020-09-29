package IntroductionToJava;

public class HumanMain {
    // main function
    public static void main(String[] args) {
        // create object: var_type var_name;
        Human mahin = new Human();

        Human nahid1; // Without memory allocation constructor is not called
/*
        mahin.name = "Mehedi Mahin";
        mahin.age = 21;
*/

        mahin.eat();

        System.out.println(mahin.name + " " + mahin.age);

        Human nahid = new Human();
        nahid.name = "Nahid Hassan";
        nahid.age = 22;

        System.out.println(nahid.name + " " + nahid.age);
    }
}
