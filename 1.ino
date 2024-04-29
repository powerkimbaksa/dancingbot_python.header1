#include <Servo.h>    //서보모터를 쓰기위해 명령어를 불러옵니다.

Servo sv1;      //첫 번째 서보모터 정의
Servo sv2;      //두 번째 서보모터 정의
Servo sv3;      //세 번째 서보모터 정의
Servo sv4;      //네 번째 서보모터 정의

void setup() {
Serial.begin(115200);   //고속 시리얼 통신을 시작합니다
sv1.attach(8);      //첫 번째 서보모터는 8번핀에 연결됨
sv2.attach(9);      //두 번째 서보모터는 9번핀에 연결됨
sv3.attach(10);       //세 번째 서보모터는 10번핀에 연결됨
sv4.attach(11);       //네 번째 서보모터는 11번핀에 연결됨
}

void loop() {
while(!Serial.available()){}    //시리얼 통신으로 값이 올 때 까지 기다리기
while(Serial.read() != 's'){}   //시리얼 통신으로 문자’s’가 온다면(시작하겠다)

int finalresult[4];   //통신값을 받을 변수 배열을 만듭니다

for(int i = 0; i < 4; i++){   //4번 반복합니다
  finalresult[i] = 0;     //하나씩 배열 공간을 모두 초기화합니다
} 

for(int j = 0; j < 4; j++){   //4번 반복합니다
  int type = 100;   
  char gap;     //통신값을 임시로 담아둘 변수를 만듭니다
  int result;     //변환된 통신값을 담아둘 변수를 만듭니다
for(int i = 0; i < 3; i++){    //3번 반복합니다
while(!Serial.available()){}    //처음 값을 받기 전까지 기다립니다
    gap = Serial.read();    //통신값 하나를 받아옵니다
    String gap2(gap);   //통신값을 문자열로 변환합니다
    result = gap2.toInt();    //문자열을 다시 정수로 변환합니다
    finalresult[j] = finalresult[j] + result * type;  //자리수에 맞게 정수를 가공합니다
 type = type / 10;    
} 
}

sv1.write(finalresult[0]);    //최종 값들을 서보모터에 전달합니다
sv2.write(finalresult[1]);
sv3.write(finalresult[2]);
sv4.write(finalresult[3]);
}
