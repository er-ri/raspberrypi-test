#include <stdio.h>

/* メインタスク(起動時にのみ関数コールされる) */
void main_task(intptr_t unused) 
{
    printf("Hello World!");
    ext_tsk();
}
