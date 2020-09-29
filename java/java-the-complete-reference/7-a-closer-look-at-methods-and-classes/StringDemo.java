class StringDemo {
    public static void main(String[] args) {
        String strObj1 = "First String...";
        String strObj2 = "Second String...";

        String strObj3 = strObj1 + " " + strObj2;

        // boolean equals(2nd str)
        // int length()
        // char charAt(index)

        String strObj4 = strObj1;

        //equals..
        if(strObj1.equals(strObj4)) {
            System.out.println("strobj1 == strobj4");
        } else {
            System.out.println("strobj1 !=  strobj4");
        }

        if (strObj1.equals(strObj2)) {
            System.out.println("strobj1 == strobj2");
        } else {
            System.out.println("strobj1 !=  strobj2");
        }

        // length
        System.out.println(strObj1.length());
        System.out.println(strObj3.length());
        System.err.println(strObj3.length() - strObj1.length() - 1); // length for strObj2 
     
        // char charAt(index)
        System.out.println(strObj2.charAt(4));
    }
}