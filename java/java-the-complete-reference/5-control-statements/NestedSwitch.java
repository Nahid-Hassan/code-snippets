// nested switch example

class NestedSwitch {
    public static void main(String[] args) {
        int num = 1;

        switch(num) {
            case 1:
                int target = num;
                
                switch(target) {
                    case 0:
                        System.out.println("Zero.");
                        break;
                    case 1:
                        System.out.println("One.");
                        break;
                    case 2:
                        System.out.println("two");
                        break;    
                } 
                break;
            case 2:
                System.out.println("Case 2.");
                break;
            default:
                System.out.println("default.");
        }
    }
}