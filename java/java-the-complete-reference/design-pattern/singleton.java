class singleton {
    public static void main(String[] args) {
        SingleObject so = SingleObject.getInstance();
        so.show();        
    }
}

class SingleObject {
    private static SingleObject instance = new SingleObject();

    private SingleObject() {
        //cannot modified from other class
    }

    public static SingleObject getInstance() {
        return instance;
    }

    public void show() {
        System.out.println("single-ton design pattern.");
    }
}
