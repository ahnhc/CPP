/* 
source file -> object file -> executable file

compiler�� ��ü�� �����ϰ� ��ȯ�Ѵ�.
interpreter�� �� ������ �ؼ��ϰ� �����Ѵ�.

linker ���� �����ϱ�

Debugging
�α� �м�, �޸� �˻�

GDB, pythontutor ����غ���!
*/

#include <iostream>
#define PRINT_FILE std::cout << "[[[ " << __FILE__ << " ]]]" << std::endl;
#define PRINT_TIME std::cout << "[[[ " << __TIMESTAMP__ << " ]]]\n" << std::endl;
int main()
{
	PRINT_FILE;
	PRINT_TIME;
	std::cout << "�̸� : ������" << std::endl;
	std::cout << "�й� : 202322515" << std::endl;
	std::cout << "�а� : ���̿��޵��ü���Ʈ�����а�" << std::endl;
	return 0;
}