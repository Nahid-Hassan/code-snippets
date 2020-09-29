// search an array using for-each style for
// for each with break 

class Search {
    public static void main(String[] args) {
        int numbers[] = { 4, 2, 1, 4, 6, 7, 5, 8, 10, 100 };

        int val = 5;

        boolean found = false;
        for(int num : numbers ) {
            if(num == val) {
                found = true;
                break;
            }
        }

        if(found) {
            System.out.println("Found.");
        } else {
            System.out.println("Not found.");
        }
    }
}