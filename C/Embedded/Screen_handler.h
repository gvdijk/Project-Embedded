
void LED_init(void);
void handle_sensors(void);
void set_led(bool status);
void screen_roll_in(void);
void screen_roll_out(void);
void status_led_toggle(void);
void status_led_off(void);
void set_stopstate(bool state);
bool toggle_auto_sensor(void);
void set_sensor_threshold(uint16_t val);
uint16_t get_sensor_threshold(void);
