class MinStack {
    private int[] stack;
    private int count;
    private class Node {
        public Node next;
        public int val;
        public Node(Node next, int val){
            this.next = next;
            this.val = val;
        }
    }
    private Node min;
    private Node prevMin;
    
    public MinStack() {
        stack = new int[10];
        count = 0;
    }
    
    public void push(int val) {
        if (count == 0){
            prevMin = new Node(null, 0);
            min = new Node(prevMin, 0);
        } else {
            if (val < stack[min.val]){
                prevMin = min;
                min = new Node(prevMin, count);
            }
        }
        stack[count++] = val; 
    }
    
    public void pop() {
        --count;
        if (min.val >= count){
            min = prevMin;
            prevMin = prevMin.next;
        }
    }
    
    public int top() {
        return stack[count-1];
    }
    
    public int getMin() {
        return stack[min.val];
    }
}
