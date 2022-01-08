class Solution {
    public String solution(String new_id) {
        
        String answer = "";
        String output = "";
        //1st step
        for(int i = 0; i <new_id.length(); i++){
            int tmp = (int)new_id.charAt(i);
            if((65<=tmp) && (tmp<=90))
                answer += (char)(tmp+32);
            else
                output += (char)tmp;
        }
        new_id = output;
        output = "";
        //2nd step
        for(int i = 0; i < new_id.length(); i++){
            char a = new_id.charAt(i);
            if(a == '-' || a == '_' || a=='.' )
                output += a;
            else if(((int)a >= 97) && (int)a<=122)
                output += a;
            else if(Character.isDigit(a) == true)
                output += a;
            else
                continue;
        }
        new_id = output;
        output = "";
        //3rd step
        for(int i = 0; i<new_id.length();i++){
            int j;
            if(new_id.charAt(i)=='.'){
                j = i;
                while(new_id.charAt(j) != '.')
                    j++;
                if(i == j)
                    output += new_id.charAt(i);
                else{
                    output += '.';
                    i = j;
                }
            }else
                output += new_id.charAt(i);
        }
        //4th step
        new_id = output;
        if(new_id.startsWith(".")==true)
            new_id.substring(1);
        if(new_id.endsWith(".")==true)
            new_id = new_id.substring(0,new_id.length()-1);
        //5th step
        if(new_id == null)
            new_id += 'a';
        //6th step
        if(new_id.length()>=16)
            new_id.substring(0, 15);
        //7th step
        if(new_id.length()<=2){
            char a = new_id.charAt(new_id.length());
            while(new_id.length()<3)
                new_id += a;
            }
                
        answer = new_id;     
        return answer;
    }
}