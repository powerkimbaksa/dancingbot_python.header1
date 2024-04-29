import serial
import time

def create_serial_connection(port):
    try:
        connection = serial.Serial(f"COM{port}", 115200)
        if connection.is_open:
            print(f"아두이노 연결 성공: COM{port}")
            return connection
        else:
            print(f"COM{port} 연결 실패")
    except serial.SerialException as e:
        print(f"COM{port}에 연결할 수 없습니다: {e}")
    return None

def find_arduino_connection():
    for portnum in range(1, 101):
        connection = create_serial_connection(portnum)
        if connection:
            return connection
    print("100개의 포트를 모두 확인했지만, 아두이노 연결을 찾을 수 없습니다.")
    return None

def move_servos(arduino, servo_values, number, gap):
    servo_values[number-8] = gap
    arduino.write(b's')
    for val in servo_values:
        formatted_val = f"{val:03}".encode('utf-8')
        arduino.write(formatted_val)
        arduino.write(b',')  # 각 값 사이에 구분자 추가

if __name__ == "__main__":
    port_input = input("///아두이노의 포트 번호만 입력하세요///\n예)COM8 -> 8\n포트번호: ")
    if port_input.isdigit():
        arduino = create_serial_connection(int(port_input))
    else:
        arduino = find_arduino_connection()

    if arduino:
        servo_values = [90, 90, 90, 90]  # 서보모터 초기 위치 설정
        move_servos(arduino, servo_values, number=8, gap=45)
