// Demonstrate a one-dimensional array

class Array {
    public static void main(String[] args) {
        //type var-name[]; //var-name = array-var
        //array-var = new type[size]
        
        int month_days[];
        month_days = new int[12];

        month_days[0] = 31;  // jan
        month_days[1] = 28;  // feb
        month_days[2] = 31;  // mar
        month_days[3] = 30;  // apr
        month_days[4] = 31;  // may
        month_days[5] = 30;  // jun
        month_days[6] = 31;  // jul
        month_days[7] = 31;  // aug
        month_days[8] = 30;  // sep
        month_days[9] = 31;  // oct
        month_days[10] = 30; // nov
        month_days[11] = 31; // dec

        for (int i = 0; i < 12; i++) {
            System.out.println(month_days[i]);
        }

        // An improve version of the previous program.
        int month_days_1[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        for (int i = 0; i < 12; i++) {
            System.out.println(month_days_1[i]);
        }
    }
}