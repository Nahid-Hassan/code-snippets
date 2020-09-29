// Demonstrate automatic type promotion in expression

class Promote {
    public static void main(String[] args) {
        byte b = 43;
        char c = 'a';

        short s = 1024;
        int i = 50000;

        float f = 5.67f;
        double d = .12121;

        double result = (f * b) + ( i / c) - (d * s);
        System.out.println(result);
    }
}
/*
 * f->float, b->byte, i->int, c->char, d->double, s->short
 * double result = (f * b) + ( i / c) - (d * s);
 * First step -->
 * (f * b) --> float
 * (i / c) --> int 
 * (d * s) --> double
 * 
 * Second step -->
 * float + int --> float
 * 
 * third step -->
 * float + double --> double
 * 
 * Final promotion is double
 */