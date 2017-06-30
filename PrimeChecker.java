import static java.lang.System.in;

class Prime {
    String string = new String();
    public void checkPrime(int... args){
        for(int i : args){
            if(isPrime(i))
                string += i+ " ";
        }
        System.out.println(string.trim());
        string="";
    }
    
    public boolean isPrime(int a){
        int maxNum = (int)Math.round(Math.sqrt(a));
        if(a<2) return false;
        for(int i=2 ; i<=maxNum ; i++){
            if(a%i == 0)
                return false;
        }
        return true;
    }
   
    }
