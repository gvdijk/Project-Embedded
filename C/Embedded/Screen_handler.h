
void LED_init(void);
void handle_sensors(void);
void set_led(bool status);
void screen_roll_in(void);
void screen_roll_out(void);
void status_led_toggle(void);
void status_led_off(void);
void set_stopstate(bool state);
bool toggle_auto_temp(void);
bool toggle_auto_light(void);
void set_temperature(uint16_t val);
uint16_t get_temperature(void);
void set_light(uint16_t val);
uint16_t get_light(void);
