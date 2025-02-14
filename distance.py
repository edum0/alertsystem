import RPi.GPIO as GPIO
import time 
TRIG = 23
ECHO = 24
BUZZER = 18
LED = 17
SWITCH = 27 

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN)
GPIO.setwarnings(False)

while True:
  time.sleep(0.05)
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  start_time = time.time()
  stop_time = time.time()

  while GPIO.input(ECHO) == 0:
      start_time = time.time()

  while GPIO.input(ECHO) == 1:
      stop_time = time.time()

  elapsed_time = stop_time - start_time
  distance = (elapsed_time * 34300) / 2
  distance=round(distance,2)
  if distance<20 and distance>10 and GPIO.input(SWITCH) == GPIO.HIGH:
    print(f"CLOSE! Disatance: {distance} cm")
    GPIO.output(LED, True)
    GPIO.output(BUZZER, True)
    time.sleep(0.2)
    GPIO.output(BUZZER, False)
    time.sleep(0.2)
  elif distance<10 and distance>5 and GPIO.input(SWITCH) == GPIO.HIGH:
    print(f"VERY CLOSE!! Distance: {distance} cm")
    GPIO.output(LED, True)
    GPIO.output(BUZZER, True)
    time.sleep(0.1)
    GPIO.output(BUZZER, False)
    time.sleep(0.1)
  elif distance<5 and GPIO.input(SWITCH) == GPIO.HIGH:
    print(f"VERY VERY CLOSE!!! Distance: {distance} cm")
    GPIO.output(LED, True)
    GPIO.output(BUZZER, True)
    time.sleep(0.05)
    GPIO.output(BUZZER, False)
    time.sleep(0.05)
  else:
    GPIO.output(LED, False)
    print(f"Distance: {distance} cm")
