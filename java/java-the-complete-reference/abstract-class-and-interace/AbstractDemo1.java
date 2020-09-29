class AbstractDemo {
    public static void main(String[] args) {
        A a =  new A() {
            @Override
            public void print3() {
                System.out.println("print--3");
            }
        };

        a.print1();
        a.print2();
        a.print3();
    }
}

abstract class A {
    public void print1() {
        System.out.println("print--1");
    }

    public void print2() {
        System.out.println("print--2");
    }

    public abstract void print3();
}