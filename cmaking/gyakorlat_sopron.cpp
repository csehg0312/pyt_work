#include <iostream>
using std::cout;
using std::cin;
using std::endl;

void udvozlet() {
	cout << "Hello Stranger!" << endl;
}

int get_age(){
	int age;
	cout << "How old are you?" << endl;
	cin >> age;
	return age;
}

int main(){
	udvozlet();
	int age_of_user = get_age();
	if (age_of_user >= 18){
		cout << "Sor johet" << endl;
	} else {
		cout << "Csak tea" << endl;
	}
	
	return 0;
}
