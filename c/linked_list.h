#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

bool ll_prepend(Node **list, int element);
void ll_display(Node *list);
void ll_unload(Node *list);
// TODO: implement functions: pop, insert, reverse, search, other???



/* Prepends element to the beginning of the list. 
 * Returns true if successful and false if failed.
 */
bool ll_prepend(Node **list, int element) {
    Node *n = malloc(sizeof(Node));
    if (n == NULL) {
        return false;
    }
    n->value = element;
    n->next = *list;
    *list = n;
    return true;
}


/* Pretty prints linked list, using sep as separator
 */
void ll_display(Node *list) {
    char *sep = "=> ";
    Node *ptr = list;
    while (ptr != NULL) {
        printf("%i %s", ptr->value, sep);
        ptr = ptr->next;
    }
    printf("\n");
}

void ll_unload(Node *list) {
    if (list==NULL) {
        return;
    }

    ll_unload(list->next);
    free(list);
}
