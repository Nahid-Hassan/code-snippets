// closer look at argument passing
class Test {
    int a, b;

    //call by value
    Test(int i, int j) {
        i *= 2;
        j /= 2;
        a = i;
        b = j;
    }

    //call by reference
    void meth(Test o) {
        o.a *= 2;
        o.b /= 2;
    }
}

class PassObjRef {
    public static void main(String[] args) {
        int a = 15, b = 20;

        System.out.println("a and b before call: " + a + " " + b);

        Test ob = new Test(a, b);

        System.out.println("a and b after call: " + a + " " + b);
    
        System.out.println("ob.a and ob.b before call: " + ob.a + " " + ob.b);

        ob.meth(ob);
        
        System.out.println("ob.a and ob.b before call: " + ob.a + " " + ob.b);
    }
}