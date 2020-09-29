package IntroductionToJava.Overloading;

public class ThisKeyword {
    public static void main(String[] args) {
        A a = new A("nahid");
        System.out.println(a.name);

        B b = new B();
        b.print();

        B b1 = new B("Nahid");
        b1.print();

        B b2 = new B("Nahid", 20);
        b2.print();

        B b3 = new B("Nahid", 20, 160);
        b3.print();

    }
}

class A {
    String name;
    int age;

    A(int a) {
        age = a; // no problem
    }

    A(String name) {
        //name = name; // create problem
        /* কোনটা instance variable and  কোনটা parameter variable  সেইটা diff.. করতে পারে না*/

        // to overcome this problem use this keyword
        this.name = name; // this.name = instance variable, name = parameter
    }
}

// more on this keyword..using this keyword call constructor
class B {
    String name;
    int age;
    double height;

    B() {
        name = "not given";
        age = 0;
        height = 0.0;
    }

    B(String name) {
        this(); // call B() constructor
        this.name = name;
    }

    B(String name, int age) {
        this(name); // call B(String name) constructor
        this.age = age;
    }

    B(String name, int age, double height) {
        this(name, age);
        this.height = height;
    }

    void print() {
        System.out.println("name: " + this.name);
        System.out.println("age: " + this.age);
        System.out.println("height: " + this.height);
        System.out.println("-----------------------");
    }
}