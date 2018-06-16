class Student extends Person{
	private int[] testScores;

    Student(String firstName,String lastName,int id,int[] testScores)
    {
        super(firstName,lastName,id);
        this.testScores = testScores;
    }

    public char calculate()
    {

        int sum =0;
        for(int i = 0 ; i< testScores.length ; i++){
            sum+= testScores[i];
        }
        sum = sum/ testScores.length;

        if( sum <= 100 && sum>=90){
            return 'O';

        }else if(sum <90 && sum>=80) {
            return 'E';
        }else if(sum <80 && sum>=70) {
            return 'A';
        }else if(sum <70 && sum>=55) {
            return 'P';
        }else if(sum <55 && sum>=40) {
            return 'D';
        }else{
            return 'T';
        }

    }

}
