/* 
source file -> object file -> executable file

compiler는 전체를 번역하고 변환한다.
interpreter는 줄 단위로 해석하고 실행한다.

linker 개념 이해하기

Debugging
로그 분석, 메모리 검사

GDB, pythontutor 사용해보기!
*/

#include <iostream>
#define PRINT_FILE std::cout << "[[[ " << __FILE__ << " ]]]" << std::endl;
#define PRINT_TIME std::cout << "[[[ " << __TIMESTAMP__ << " ]]]\n" << std::endl;
int main()
{
	PRINT_FILE;
	PRINT_TIME;
	std::cout << "이름 : 안형찬" << std::endl;
	std::cout << "학번 : 202322515" << std::endl;
	std::cout << "학과 : 바이오메디컬소프트웨어학과" << std::endl;
	return 0;
}