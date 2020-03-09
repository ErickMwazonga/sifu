"""
Example :
Given the AP :- 1 3 7 9 11 13 find the missing value "which would be 5 here".

Conditions :
Get an user for the length of AP sequence and make sure user provides length is above 3.
Get the input in a single line ex:- "1 3 5 7 9 11"
Provide the solution in O(n) or less if you can.

Divide and conquer with time complexity O(lgn):

binary search. The input must have at least one missing element
public static int findMissing_binary(int[] array) {
    assert array != null && array.length > 2;
    
    int diff = Math.min(array[2]-array[1], array[1]-array[0]);

    int low = 0, high = array.length-1;
    while(low < high) {
        int mid = (low+high) >>> 1;

        int leftDiff = array[mid]-array[low];
        if(leftDiff > diff * (mid-low)) {
            if(mid-low == 1)
                return (array[mid]+array[low]) / 2;
            
            high = mid;
            continue;
        }
        
        int rightDiff = array[high]-array[mid];
        if(rightDiff > diff * (high-mid)) {
            if(high-mid == 1)
                return (array[high]+array[mid]) / 2;
            
            low = mid;
            continue;
        }
    }
    
    return -1;
}

"""