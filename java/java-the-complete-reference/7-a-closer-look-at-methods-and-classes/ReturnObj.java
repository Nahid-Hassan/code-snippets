// Returning an object

class Test {
    int a;

    Test(int i) {
        a = i;
    }

    Test inCreByTen() {
        Test temp = new Test(a + 10);
        return temp;
    }
}

class ReturnObj {
    public static void main(String[] args) {
        Test ob1 = new Test(2);
        Test ob2;

        ob2 = ob1.inCreByTen();
        System.out.println("Ob1.a: " + ob1.a);
        System.out.println("Ob1.b: " + ob2.a);

        ob2 = ob2.inCreByTen();
        System.out.println("Ob1.a: " + ob1.a);
        System.out.println("Ob1.b: " + ob2.a);
    }
}