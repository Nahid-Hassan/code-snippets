// Demonstrate dynamic initialization

class DynInit {
    public static void main(String[] args) {
        // declare variable
        // variable a, and b are initialized by constant.
        double a = 3.0, b = 4.0;
        
        // c is dynamically initialized.
        
        double c = Math.sqrt(a * a + b * b);
        System.out.println(c);
    }
}
// Output:
// 5