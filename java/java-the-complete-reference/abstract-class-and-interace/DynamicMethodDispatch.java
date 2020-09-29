// for good understand dynamic-method-dispatch
// link: https://youtu.be/-sXqTM09LRQ?list=PLgLCjVh3O6Shp2NqygH7fvgIHSNlRYSyA 

class DynamicMethodDispatch {
    public static void main(String[] args) {
        B b = new B();

        b.print();
        System.out.println(b.x);

        A a = new B();
        a.print();
        System.out.println(a.x);
    }
}

class A {
    int x = 20;
    void print() {
        System.out.println("in class a");
    }
}

class B extends A {
    int x = 30;
    void print() {
        System.out.println("in class b");
    }
}

class normal {
    int x = 40;
    void print() {
        System.out.println("in class normal");
    }
}