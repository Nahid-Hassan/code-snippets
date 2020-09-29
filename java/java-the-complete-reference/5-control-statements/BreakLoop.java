// Using break in loop

class BreakLoop {
    public static void main(String[] args) {
        for(int i = 0; i < 100; i++){
            for(int j = 0; j < 100; j++) {
                if(j < 10) {
                    System.out.print(j + " ");
                } else {
                    System.out.println();
                    break; //inner break statement
                }
            }
            if(i == 5) {
                break; //outermost break statement
            }
        }
    }
}