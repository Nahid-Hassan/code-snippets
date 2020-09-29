// demonstrate java access test

class Test {
    int a;
    public int b;
    private int c;

    void setC(int i) {
        c = i;
    }
    int getC() {
        return c;
    }
}

class AccessTest {
    public static void main(String[] args) {
        Test ob = new Test();

        ob.a = 10;
        ob.b = 20;

        //ob.c = 23; // Error! variable c is not visible here.
        
        //but you can access c using setC() and getC()
        ob.setC(10);
        int retVal = ob.getC();

        System.out.println(retVal);
    }
}