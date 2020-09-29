// Left shift as a quick way to multiply by 2

class MultByTwo {
    public static void main(String[] args) {
        int i;
        int num = 0xFFFFFFF;

        for(i = 0; i < 4; i++) {
            num = num << 1;

            System.out.println(num);
        }
        // some example
        for(i = 0; i < 10; i++) {
            for(int j = 0; j < 4; j++) {
                System.out.println(i << j);
            }
            System.out.println("------");
        }
    }
}