#include "app.h"
#include <stdio.h>
#include <unistd.h>

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
    
    printf("Hello World!\n");
    
    ev3_motor_set_power(left_motor, 310);
    // ev3_motor_set_power(right_motor, 30);
    /* ライントレースタスクの起動 */
    // sta_cyc(LINE_TRACER_TASK_CYC);
    sleep(5);

    ev3_motor_set_power(left_motor, 0);
    /* タスク終了 */
    ext_tsk();
}
