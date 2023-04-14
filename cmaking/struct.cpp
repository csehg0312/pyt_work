#include <iostream>
#include <ostream>
using std::cout;
using std::cin;
using std::endl;

class Harcos {
	public:
	int hp;
	int dmg;
};

bool isDead(Harcos harcos){
	return harcos.hp == 0;
}

std::ostream& operator << (std::ostream& o, const Harcos& w){
	o << "HP: " << w.hp << "\n" << "DMG:  " << w.dmg;
	return o;
}

void Tamad(const Harcos& attacker, Harcos& defender) {
	if (!isDead(attacker)){
		defender.hp -= attacker.dmg;
		if (defender.hp < 0) defender.hp = 0;
	}
}

Harcos& operator >> (const Harcos& attacker, Harcos& defender){
	Tamad(attacker, defender);
	return defender;
}

int main(){
	
	Harcos Sandor{100,5};
	Harcos Bandi{80,8};
	
	cout << Sandor << endl;
	cout << (isDead(Sandor) ? "!!!DEAD!!!" : "!!!ALIVE!!!") << endl;
	cout << Bandi << endl;
	cout << (isDead(Bandi) ? "!!!DEAD!!!" : "!!!ALIVE!!!") << endl;
	
	while(!isDead(Sandor) &&  !isDead(Bandi)) {
		Bandi>>Sandor>>Bandi;
		//Sandor >> Bandi;
		
		cout << Sandor << endl;
		cout << (isDead(Sandor) ? "!!!DEAD!!!" : "!!!ALIVE!!!") << endl;
		cout << Bandi << endl;
		cout << (isDead(Bandi) ? "!!!DEAD!!!" : "!!!ALIVE!!!") << endl;
	}
	
	
	
	return 0;
}
