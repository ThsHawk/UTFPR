#include <Servo.h>

#define sensor_01_trig  8
#define sensor_01_echo  9
#define sensor_02_trig  10
#define sensor_02_echo  11
#define servo_pin       2
Servo servo;

void pulse(uint8_t pin){
    digitalWrite(pin, HIGH);
    delayMicroseconds(10);
    digitalWrite(pin, LOW);
}

void control_gate(bool pin){
    bool gate_flag = false, led_state = true;

    for (size_t i = 0; i < 4; i++){
        //digitalWrite(pin_YELLOW, led_state);
        delay(200);
        led_state = !led_state;
    }

    servo.write(160);

    uint16_t gate_count = 0;
    while (gate_count < 700){
        pulse(pin == true ? sensor_02_trig : sensor_01_trig);
        float dist = pulseIn(pin == true ? sensor_02_echo : sensor_01_echo, HIGH) * 0.017;
        delay(1);
        if (dist < 5.0){
            gate_flag = true;
            gate_count = 0;
        }
        if (dist > 5.0 && gate_flag)gate_count++;
    }
}

void setup(){
    pinMode(sensor_01_trig, OUTPUT);
    digitalWrite(sensor_01_trig, LOW);
    pinMode(sensor_01_echo, INPUT);
    pinMode(sensor_02_trig, OUTPUT);
    digitalWrite(sensor_02_trig, LOW);
    pinMode(sensor_02_echo, INPUT);

    servo.attach(servo_pin);
    servo.write(100);

    delay(100);
}

void loop(){
    pulse(sensor_01_trig);
    float sensor_01_dist = pulseIn(sensor_01_echo, HIGH) * 0.017;
    pulse(sensor_02_trig);
    float sensor_02_dist = pulseIn(sensor_02_echo, HIGH) * 0.017;
    if (sensor_01_dist < 5.0){
        control_gate(true);
    }else if (sensor_02_dist < 5.0){
        control_gate(false);
    }else{
        servo.write(100);
    }
    delay(1);
}