# 프로젝트 생성
# cli 명령 :  pip install 지원하는 라이브러리 이름 
# pip install googletran == 4.0.0-rc1
  # 부득이하게 번역기 라이브러리의 버전 지정
  # 보통의 경우 == <-- 이퀄표시는 사용하지 않음 (버전지정을 해야 할 때만 사용한다.)

import googletrans
# 설치한 모듈 가져오기
translate_worker = googletrans.Translator()
# 설치한 모듈의 생성자 함수에 접근한 데이터를 translate_worker 라는 변수에 가리킴 
input_data = input('영어로 번역하고 싶은 한글을 입력하세요 >> ');
# REPL 환경에서 입력 데이터를 받음 
result_value = translate_worker.translate(input_data, dest="en");
# 엑세스한 생성자 함수에 내장된 translate() 메서드 호출
print(result_value.text)