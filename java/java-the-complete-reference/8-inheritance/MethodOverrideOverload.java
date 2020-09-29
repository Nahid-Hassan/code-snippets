class A {
    int i, j;

    A(int a, int b) {
        i = a;
        j = b;
    }

    void show() {
        System.out.println(i + " " + j);
    }
}

class B extends A {
    int k;

    B(int a, int b, int c) {
        super(a, b);

        k = c;
    }

    // overload
    void show(String msg) {
        System.out.println(msg + " " + k);
    }
}

class C extends A {
    C(int a, int b) {
        super(a, b);
    }

    //overridden..
    void show() {
        System.out.println("i and j = " + i + " " + j);
    }
}

class MethodOverrideOverload {
    public static void main(String[] args) {
        B b = new B(1,2,3);
        b.show();
        b.show("k is ");

        C c = new C(1,2);
        c.show();
    }
}