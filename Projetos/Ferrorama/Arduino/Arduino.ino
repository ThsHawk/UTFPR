#include <Servo.h>

#define sensor_01   A0
#define sensor_02   A3
#define pin_RED     4
#define pin_YELLOW  5
#define pin_GREEN   6
#define servo_pin   2
Servo servo;

void control_gate(uint8_t sensor_pin){
  bool gate_flag = false, led_state = true;
  digitalWrite(pin_GREEN, LOW);
  
  for (size_t i = 0; i < 4; i++){
    digitalWrite(pin_YELLOW, led_state);
    delay(200);
    led_state = !led_state;
  }
  
  servo.write(160);
  
  digitalWrite(pin_RED, HIGH);
  uint16_t gate_count = 0, led_count = 0;
  while(gate_count < 300){
    uint16_t sensor_read = analogRead(sensor_pin);
    delay(1);
    if(sensor_read < 200){
      gate_flag = true;
      gate_count = 0;
      led_state = led_count = 0;
    }
    if(sensor_read > 200 && gate_flag){
      gate_count++;
      led_count++;
    }
    if(led_count > 200){
      led_count = 0;
      led_state = !led_state;
    }
    //digitalWrite(pin_YELLOW, led_state);
  }
  digitalWrite(pin_RED, LOW);
  digitalWrite(pin_YELLOW, LOW);
}

void setup() {
  pinMode(sensor_01, INPUT);
  pinMode(sensor_02, INPUT);
  pinMode(pin_RED, OUTPUT);
  pinMode(pin_YELLOW, OUTPUT);
  pinMode(pin_GREEN, OUTPUT);
  servo.attach(servo_pin);
  servo.write(100);
}

void loop() {
  uint16_t a0 = analogRead(sensor_01);
  uint16_t a3 = analogRead(sensor_02);
  delay(1);
  if(a0 < 200){
    control_gate(sensor_02);
  }else if(a3 < 200){
    control_gate(sensor_01);
  }else{
    digitalWrite(pin_GREEN, HIGH);
    servo.write(100);
  }
}
//2306 //50