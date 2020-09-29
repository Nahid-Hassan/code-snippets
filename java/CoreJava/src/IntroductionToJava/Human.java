package IntroductionToJava;

public class Human {
    String name;
    int age;
    double height;

    /* Constructor */
    Human() {
        System.out.println("Constructor...");
        name = "No name";
        age = 10;
    }

    void eat() {
        System.out.println("Eating...");
    }

    void sleep() {
        System.out.println("Sleeping...");
    }

    void walk() {
        System.out.println("Walking...");
    }
}
