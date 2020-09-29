import java.util.Scanner;

class RunTimeExcep {
    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);

        // int x;

        // System.out.println("Enter a number: ");
        // x = sc.nextInt();

        // if(x > 10) {
        //     throw new MyException();
        // }
    
        A a = new A();
        try {
            a.print();
        } catch (Exception e) {
            //TODO: handle exception
        }

        B b = new B();
        b.print();
    }
}

// class MyException extends RunTimeException {

// }

class A {
    public void print() throws Exception {
        // code////
    }
}

class B {
    public void print() {
        // code
    }
}