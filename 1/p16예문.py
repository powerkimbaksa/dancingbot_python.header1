import dancingbot_python.header as servo
#댄싱봇을 파이썬으로 조작하기 위해, 명령어를 불러옵니다

def setup():
    #이 안에 들어가는 명령어는, 전원이 켜진 후 한번만 실행됩니다
    servo.time.sleep(1)	#처음 전윈이 켜진후, 1초간 대기합니다

    servo.move(8,90)	#8번 서보모터를 90도로 맞춥니다
    servo.move(9,90)	#9번 서보모터를 90도로 맞춥니다
    servo.move(10,90)	#10번 서보모터를 90도로 맞춥니다
    servo.move(11,90)	#11번 서보모터를 90도로 맞춥니다

    servo.time.sleep(2)	#loop 코드가 실행되기전에 잠시 대기합니다

def loop():
    #이 안에 들어가는 명령어는, 무한히 반복됩니다
    servo.move(8,45)	#왼쪽발을 들어올리기
    servo.time.sleep(1)	#올린채로 1초간 대기
    servo.move(8,90)	#왼쪽발을 내리기
    servo.time.sleep(1)	#내린채로 1초간 대기
    
setup()	#setup안의 명령어를 최초로 실행합니다
while(True):	#무한 반복합니다
    loop()	#loop안의 명령어를 무한 반복합니다

