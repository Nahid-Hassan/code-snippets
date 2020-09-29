// a simple example for recursion

class Factorial {
    int fact(int n) {
        int result;

        if(n == 1) return 1;
        result = fact(n - 1) * n;
        return result;
    }
}

class Recursion {
    public static void main(String[] args) {
        Factorial f = new Factorial();

        for(int i = 1; i <= 10; i++) {
            System.out.println(f.fact(i));
        }
    }
}