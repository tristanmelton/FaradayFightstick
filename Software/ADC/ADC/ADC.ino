#include <SPI.h>
#include <limits.h>
#include <EEPROM.h>

// SPI Pins
#define MISO 11
#define MOSI 10
#define SCLK 9

#define CS1 17
#define CS2 8

#define LP 1
#define MP 4
#define HP 30
#define SHP 12
#define LK 6
#define MK 23
#define HK 22
#define SHK 21


#define LEFT 11
#define DOWN 10
#define RIGHT 5
#define SELECT 3
#define UP 9
#define HOME 2 
#define TURBO 0
#define START 13


// Registry Values
#define CH0 0b00000000
#define CH1 0b00001000
#define CH2 0b00010000
#define CH3 0b00011000
#define CH4 0b00100000
#define CH5 0b00101000
#define CH6 0b00110000
#define CH7 0b00111000

float lp_val = 0;
float lp_thres;
float mp_val = 0;
float mp_thres = 300;
float hp_val = 0;
float hp_thres = 300;
float shp_val = 0;
float shp_thres = 300;

float shk_val = 0;
float shk_thres = 300;
float hk_val = 0;
float hk_thres = 300;
float mk_val = 0;
float mk_thres = 300;
float lk_val = 0;
float lk_thres = 300;

float left_val = 0;
float left_thres = 300;
float right_val = 0;
float right_thres = 300;
float down_val = 0;
float down_thres = 300;
float up_val = 0;
float up_thres = 300;
float sel_val = 0;
float sel_thres = 300;
float sta_val = 0;
float sta_thres = 300;
float home_val = 0;
float home_thres = 300;
float turbo_val = 0;
float turbo_thres = 300;

bool configMode = false;

template<typename T>
void printBinary(T value)
{
    for ( size_t mask = 1 << ((sizeof(value) * CHAR_BIT) - 1); mask; mask >>= 1 )
    {
        Serial.print(value & mask ? "1" : "0");
    }
}


void ReadThresholds() 
{
  EEPROM.get(0, lp_thres);
  EEPROM.get(4, mp_thres);
  EEPROM.get(8, hp_thres);
  EEPROM.get(12, shp_thres);
  EEPROM.get(16, lk_thres);
  EEPROM.get(20, mk_thres);
  EEPROM.get(24, hk_thres);
  EEPROM.get(28, shk_thres);
  EEPROM.get(32, left_thres);
  EEPROM.get(36, right_thres);
  EEPROM.get(40, up_thres);
  EEPROM.get(44, down_thres);
  EEPROM.get(48, sta_thres);
  EEPROM.get(52, sel_thres);
  EEPROM.get(56, home_thres);
  EEPROM.get(60, turbo_thres);
}
void setup()
{
  Serial.begin(57600);
  SPI.begin();
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE3));
  pinMode(MOSI, OUTPUT);
  pinMode(MISO, INPUT);
  pinMode(SCLK, OUTPUT);
  pinMode(CS1, OUTPUT);
  pinMode(CS2, OUTPUT);

  pinMode(LP, OUTPUT);
  pinMode(MP, OUTPUT);
  pinMode(HP, OUTPUT);
  pinMode(SHP, OUTPUT);
  pinMode(LK, OUTPUT);
  pinMode(MK, OUTPUT);
  pinMode(HK, OUTPUT);
  pinMode(SHK,OUTPUT);

  pinMode(LEFT, OUTPUT);
  pinMode(RIGHT, OUTPUT);
  pinMode(UP, OUTPUT);
  pinMode(DOWN, OUTPUT);
  pinMode(START, OUTPUT);
  pinMode(SELECT, OUTPUT);
  pinMode(HOME, OUTPUT);
  pinMode(TURBO, OUTPUT);

  digitalWrite(LP, HIGH);
  digitalWrite(MP, HIGH);
  digitalWrite(HP, HIGH);
  digitalWrite(SHP, HIGH);
  digitalWrite(LK, HIGH);
  digitalWrite(MK, HIGH);
  digitalWrite(HK, HIGH);
  digitalWrite(SHK, HIGH);

  digitalWrite(LEFT, HIGH);
  digitalWrite(RIGHT, HIGH);
  digitalWrite(DOWN, HIGH);
  digitalWrite(UP, HIGH);
  digitalWrite(SELECT, HIGH);
  digitalWrite(START, HIGH);
  digitalWrite(HOME, HIGH);
  digitalWrite(TURBO, HIGH);

  digitalWrite(CS1, HIGH); //disable at start
  digitalWrite(CS2, HIGH); //disable at start

  ReadThresholds();

  lp_val = readAnalogInput(CS1, CH1);
  if(lp_val < 200) { // If we are going into config mode
    configMode = true;
    Serial.println("Entering Config Mode");
  }
}

void loop()
{
  if(configMode) {
    while (Serial.available() == 0) {}     //wait for data available
    String test = Serial.readString();

    const char* cstr = test.c_str();
    char* token = strtok(cstr, ";");
    char* button = token;
    token= strtok(0, ";");
    float val = atoi(token);

    if(!strcmp(button,"GET")) {
      //Serial.print("Getting memory value... "); Serial.println(int(val));
      float memval;
      EEPROM.get((int)val, memval);
      Serial.println(memval);
    }
    else if(!strcmp(button,"LP")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(0, val);
    }
    else if(!strcmp(button,"MP")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(4, val);
    }
    else if(!strcmp(button,"HP")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(8, val);
    }
    else if(!strcmp(button,"SHP")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(12, val);
    }
    else if(!strcmp(button,"LK")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(16, val);
    }
    else if(!strcmp(button,"MK")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(20, val);
    }
    else if(!strcmp(button,"HK")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(24, val);
    }
    else if(!strcmp(button,"SHK")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(28, val);
    }    
    else if(!strcmp(button,"LEFT")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(32, val);
    }
    else if(!strcmp(button,"RIGHT")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(36, val);
    }
    else if(!strcmp(button,"UP")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(40, val);
    }
    else if(!strcmp(button,"DOWN")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(44, val);
    } 
    else if(!strcmp(button,"START")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(48, val);
    }
    else if(!strcmp(button,"SELECT")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(52, val);
    }
    else if(!strcmp(button,"HOME")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(56, val);
    }
    else if(!strcmp(button,"TURBO")) {
      //Serial.print("Writing "); Serial.print(val); Serial.print(" to "); Serial.println(button);
      EEPROM.put(60, val);
    } 
    //Serial.println("Written");
  } 
  else
  {
    lp_val = readAnalogInput(CS1, CH1);
    mp_val = readAnalogInput(CS1, CH2);
    hp_val = readAnalogInput(CS1, CH3);
    shp_val = readAnalogInput(CS1, CH4);
    shk_val = readAnalogInput(CS1, CH5);
    hk_val = readAnalogInput(CS1, CH6);
    mk_val = readAnalogInput(CS1, CH7);
    lk_val = readAnalogInput(CS1, CH0);

    left_val = readAnalogInput(CS2, CH1);
    down_val = readAnalogInput(CS2, CH2);
    right_val = readAnalogInput(CS2, CH3);
    sel_val = readAnalogInput(CS2, CH4);
    sta_val = readAnalogInput(CS2, CH5);
    up_val = readAnalogInput(CS2, CH6);
    home_val = readAnalogInput(CS2, CH7);
    turbo_val = readAnalogInput(CS2, CH0);

    check_thresholds();
    bool ACTIONS_PRINT_DEBUG = false;
    bool DIRECTIONS_PRINT_DEBUG = false;
    if(ACTIONS_PRINT_DEBUG) {
      Serial.print("LP: ");
      Serial.print(lp_val);
      Serial.print(" MP: ");
      Serial.print(mp_val);
      Serial.print(" HP: ");
      Serial.print(hp_val);
      Serial.print(" SHP: ");
      Serial.print(shp_val);
      Serial.print(" LK: ");
      Serial.print(lk_val);
      Serial.print(" MK: ");
      Serial.print(mk_val);
      Serial.print(" HK: ");
      Serial.print(hk_val);
      Serial.print(" SHK: ");
      Serial.println(shk_val);
    }
    if(DIRECTIONS_PRINT_DEBUG) {
      Serial.print(" LEFT: ");
      Serial.print(left_val);
      Serial.print(" DOWN: ");
      Serial.print(down_val);
      Serial.print(" RIGHT: ");
      Serial.print(right_val);
      Serial.print(" SELECT: ");
      Serial.print(sel_val);
      Serial.print(" START: ");
      Serial.print(sta_val);
      Serial.print(" UP: ");
      Serial.print(up_val);
      Serial.print(" HOME: ");
      Serial.print(home_val);
      Serial.print(" TURBO: ");
      Serial.println(turbo_val);
    }
  } 

}

void check_thresholds()
{
  //Punches
  if(lp_val < lp_thres) {
    digitalWrite(LP, LOW);
    Serial.println("LP PRESSED");
  } else {
    digitalWrite(LP, HIGH);
  }
  if(mp_val < mp_thres) {
    digitalWrite(MP, LOW);
    Serial.println("MP PRESSED");
  } else {
    digitalWrite(
      MP, HIGH);
  }
  if(hp_val < hp_thres) {
    digitalWrite(HP, LOW);
    Serial.println("HP PRESSED");
  } else {
    digitalWrite(HP, HIGH);
  }
  if(shp_val < shp_thres) {
    digitalWrite(SHP, LOW);
    Serial.println("SHP PRESSED");
  } else {
    digitalWrite(SHP, HIGH);
  }    

  //Kicks
  if(lk_val < lk_thres) {
    digitalWrite(LK, LOW);
    Serial.println("LK PRESSED");
  } else {
    digitalWrite(LK, HIGH);
  }
  if(mk_val < mk_thres) {
    digitalWrite(MK, LOW);
    Serial.println("MK PRESSED");
  } else {
    digitalWrite(
      MK, HIGH);
  }
    if(hk_val < hk_thres) {
    digitalWrite(HK, LOW);
    Serial.println("HK PRESSED");
  } else {
    digitalWrite(HK, HIGH);
  }
  if(shk_val < shk_thres) {
    digitalWrite(SHK, LOW);
    Serial.println("SHK PRESSED");
  } else {
    digitalWrite(SHK, HIGH);
  }   

    //Directionals
  if(up_val < up_thres) {
    digitalWrite(UP, LOW);
    Serial.println("UP PRESSED");
  } else {
    digitalWrite(UP, HIGH);
  }
  if(down_val < down_thres) {
    digitalWrite(DOWN, LOW);
    Serial.println("DOWN PRESSED");
  } else {
    digitalWrite(DOWN, HIGH);
  }
  if(left_val < left_thres) {
    digitalWrite(LEFT, LOW);
    Serial.println("LEFT PRESSED");
  } else {
    digitalWrite(LEFT, HIGH);
  }
  if(right_val < right_thres) {
    digitalWrite(RIGHT, LOW);
    Serial.println("RIGHT PRESSED");
  } else {
    digitalWrite(RIGHT, HIGH);
  }    

  //Menu Buttons
  if(sta_val < sta_thres) {
    digitalWrite(START, LOW);
    Serial.println("START PRESSED");
  } else {
    digitalWrite(START, HIGH);
  }
  if(sel_val < sel_thres) {
    digitalWrite(SELECT, LOW);
    Serial.println("SELECT PRESSED");
  } else {
    digitalWrite(SELECT, HIGH);
  }
    if(home_val < home_thres) {
    digitalWrite(HOME, LOW);
    Serial.println("HOME PRESSED");
  } else {
    digitalWrite(HOME, HIGH);
  }
  if(turbo_val < turbo_thres) {
    digitalWrite(TURBO, LOW);
    Serial.println("TURBO PRESSED");
  } else {
    digitalWrite(TURBO, HIGH);
  }   
}
uint16_t readAnalogInput(int chipSelect, byte channel)
{
  digitalWrite(chipSelect, LOW);  
  byte msb = SPI.transfer(channel);
  byte lsb = SPI.transfer(0x00);
  digitalWrite(chipSelect, HIGH);
  uint16_t result = (msb << 8) | (lsb);
  return result;
}
