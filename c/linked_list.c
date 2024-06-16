/* Program accepts a list of command-line arguments. Program initializes a 
* linked list and then performs a sequence of operations on it. 
* Operations include:
* pr <int> - prepending <int> to the linked list (implemented)
* d - pretty prints current state of the list (implemented)
* ap <int> - appends <int> to the linked list
* p - pops first element of te list (i.e. pop([1 => 2 => 3 =>]) -> [2 => 3 =>])
* rm <pos> - removes element at a <pos> position (rm[0] = pop)
    * rm[0] is same as pop
    * rm[1]([1 => 2 => 3 =>]) -> 1 => 3 =>
* r - reverses a list
*/ 
// TODO: Implement accepting command-line arguments
// TODO: Implement missing functions
#include "linked_list.h"

int main (int argc, char *argv[]) {
    Node *list = NULL;

    // Populate linked list
    for (int i = 1; i < argc; i++) {
        bool result = ll_prepend(&list, atoi(argv[i]));
        if (!result) {
            // TODO: Free memory
            return 1;
        }
    }

    // Display with function
    ll_display(list);
    
    // TODO: Release allocated memory
    ll_unload(list);
    return 0;
}

