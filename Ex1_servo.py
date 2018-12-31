import RPi.GPIO as GPIO
import sys
import time

#하드웨 PWM은 18번 핀을 이용해 제어한다.
pin  = 18

#SG90 모터를 우측으로 회전시킨다. 0 ~ 5사이 값을 이용한다.
def my_left():
    x = 2.5
    print("왼쪽 회전값:(%.1f)"%x)
    pwm.ChangeDutyCycle(x)
#SG90 모터를 중앙에 위치시킨다.. 중앙은 정학하게 7.5 듀티비를 이용한다.
def my_middle():
    y = 5.5
    print("중앙 회전값:(%.1f)"%y)
    pwm.ChangeDutyCycle(y)
#SG90 모터를 좌측으로 회전시킨다. 듀티비 10을 이용한다.
#일부 제품은 12.5 듀티비를 이용한다.
def my_rigth():
    z = 10.5
    print("오른쪽 회전값:(%.1f)"%z)
    pwm.ChangeDutyCycle(z)
    #pwm.ChangeDutyCycle(12.5)
#임의의 입력 듀티비 만큼 SG90 모터를 회전시킨다.
def servo(duty):
    if(duty <= 0.0 or duty >= 10.5):
        print("invalid duty:",duty)
        return 
    pwm.ChangeDutyCycle(duty)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
#18번 핀을 H/W PWM(50Hz)으로 지정한다.
pwm = GPIO.PWM(pin,35)

#듀티비 7.5로 설정한다. 50Hz에서 7.5 듀티비는 1.5ms 파형을 만들어 서보모터를 중앙에 위치 시킴

pwm.start(7.5)
time.sleep(1)
#서보 모터르 좌우로 회전시킨다.
my_left()
time.sleep(1)
my_rigth()
time.sleep(1)
my_middle()


try:
    while True:
        my_left()
        time.sleep(1)
        print("======")
        my_rigth()
        time.sleep(1)
        print("======")
        my_middle()
        print("======")
        #임의 듀티비를 입력 받음
        #duty = float(12.5)#(raw_input("duty[Range:0.0~12.5]: "))
        #if(0 == duty):
        #    print("종료")
        #    break
        #servo(12.5)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    

