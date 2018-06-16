public class Solution {
    Stack stack= new Stack();
    Queue queue = new LinkedList();
    void pushCharacter(char ch){
            stack.push(ch);
    }
    char popCharacter(){
        if(!stack.empty())
            return (char)stack.pop();
        return ' ';
    }
    void enqueueCharacter(char ch){
        queue.add(ch); // .offer()
    }
    char dequeueCharacter(){
        if(!queue.isEmpty())
            return (char)queue.poll();
        return ' ' ;
    }
