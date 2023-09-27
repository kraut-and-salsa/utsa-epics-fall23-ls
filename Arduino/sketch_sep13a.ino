int led_pin1 = 15
int led_pin2 = 17
int blink_duration1 = 1000

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  digitalWrite (led_pin1,HIGH);
  delay (blink_duration1);
  digitalWrite (led_pin1,LOW);
  delay (blink_duration1);
}
