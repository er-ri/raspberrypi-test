#include "app.h"
#include <stdio.h>

/* メインタスク(起動時にのみ関数コールされる) */
void main_task(intptr_t unused) {

    /* センサー入力ポートの設定 */
    ev3_sensor_config(touch_sensor ,TOUCH_SENSOR);
    ev3_sensor_config(color_sensor ,COLOR_SENSOR);
    ev3_sensor_config(sonar_sensor ,ULTRASONIC_SENSOR);
    ev3_sensor_config(gyro_sensor  ,GYRO_SENSOR);
    
    /* モーター出力ポートの設定 */
    ev3_motor_config(arm_motor     ,LARGE_MOTOR);
    ev3_motor_config(left_motor    ,MEDIUM_MOTOR);
    ev3_motor_config(right_motor   ,MEDIUM_MOTOR);
    
    printf("Hello World!");
    
    char command;
    scanf("%c", &command);
    switch (command) {
        case 'f':
            ev3_motor_set_power(left_motor, 30);
            break;
        case 'b':
            ev3_motor_set_power(left_motor, 0);
            break;
        case 'l':
            printf("Turning left.\n");
            break;
        case 'r':
            printf("Turning right.\n");
            break;
        default:
            printf("Invalid command.\n");
            printf("Value of c = %c\n",command);
            break;
    }

    // ev3_motor_set_power(left_motor, 30);
    // ev3_motor_set_power(right_motor, 30);
    /* ライントレースタスクの起動 */
    // sta_cyc(LINE_TRACER_TASK_CYC);

    /* タスク終了 */
    ext_tsk();
}
