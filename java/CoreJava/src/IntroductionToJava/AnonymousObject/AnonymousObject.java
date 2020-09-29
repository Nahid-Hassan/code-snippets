package IntroductionToJava.AnonymousObject;

public class AnonymousObject {
    public static void main(String[] args) {
        new Nadia(10).print();
    }
}

class Nadia {
    int x;

    Nadia(int x) {
        this.x = x;
    }

    void  print() {
        System.out.println(this.x);
    }
}