// Demonstrate Relation operator and comparison between C++ and Java

class RelationalOpt {
    public static void main(String[] args) {
        if(10 < 20) {
            System.out.println("10 is less then 20");
        }
        
        if(10 > 20 == false) {
            System.out.println("10 > 20");
        } else {
            System.out.println("10 < 20");
        }

        if (10 > 20) {
            System.out.println("10 > 20");
        } else {
            System.out.println("10 < 20");
        }    
    }
}