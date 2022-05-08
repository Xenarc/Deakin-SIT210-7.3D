import RPi.GPIO as GPIO
from Bluetin_Echo import Echo
import time

TRIGGER = 16
ECHO = 20

LED = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

pwm = GPIO.PWM(LED,1000)
pwm.start(0)

echo = Echo(TRIGGER, ECHO, 343)

distance_cof = 0.5
last_result = 0

try:
  while True:
    result = echo.read('cm', 3)

    if(result > 0 and result <= 100*distance_cof):
      print(result, "cm")
      pwm.ChangeDutyCycle(100 - result/distance_cof)
      last_result = result
    else:
      if(last_result > 0 and last_result <= 100*distance_cof):
        pwm.ChangeDutyCycle(100 - last_result/distance_cof/2)
      pwm.ChangeDutyCycle(0)
      print(" - ")


except KeyboardInterrupt:
  echo.stop()
  GPIO.cleanup()
  print("\nProgram Exited Cleanly")

