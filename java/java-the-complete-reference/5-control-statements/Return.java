// demonstrate return

class Return {
    public static void main(String[] args) {
        boolean t = true;

        System.out.println("Before the return...");

        if(t) return;

        System.out.println("After the return...this won't execute...");
    }
}