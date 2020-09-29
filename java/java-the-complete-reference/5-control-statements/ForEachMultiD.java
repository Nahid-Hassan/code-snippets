// use for-each style for on a two-dimensional array

class ForEachMultiD {
    public static void main(String[] args) {
        int numbers[][] = new int[3][5];

        //given numbers some values
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 5; j++) {
                numbers[i][j] = (i + 1) * (j + 1);
            }
        }

        // use for-each for to display and sum the values
        for(int number[] : numbers) {
            for(int num : number) {
                System.out.print(num + " ");
            } System.out.println("\n");
        }
    }
}
