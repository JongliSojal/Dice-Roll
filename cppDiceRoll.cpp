///Made by Jongli Sojal

#include<iostream>
#include<ctime>
#include<cstdlib>

using namespace std;

void pc_roll(int x){
    if (x==1){
        cout << " ___________\n|           |\n|     _     |\n|    |_|    |\n|           |\n|___________|" << endl;

    }

    if (x==2){
        cout << " ___________\n|   _       |\n|  |_|      |\n|       _   |\n|      |_|  |\n|___________|" << endl;
    }

    if (x==3){
        cout << " ___________\n|  _        |\n| |_| _     |\n|    |_| _  |\n|       |_| |\n|___________|" << endl;
    }
    if (x==4){
        cout << " ___________\n|  _     _  |\n| |_|   |_| |\n|  _     _  |\n| |_|   |_| |\n|___________|" << endl;
    }

    if (x==5){
        cout << " ___________\n|  _     _  |\n| |_| _ |_| |\n|  _ |_| _  |\n| |_|   |_| |\n|___________|" << endl;
    }

    if (x==6){
        cout << " ___________\n|  _  _  _  |\n| |_||_||_| |\n|  _  _  _  |\n| |_||_||_| |\n|___________|" << endl;
    }
}

void your_roll(int x){
    if (x==1){
        cout << " ___________\n|           |\n|     _     |\n|    |_|    |\n|           |\n|___________|" << endl;

    }

    if (x==2){
        cout << " ___________\n|   _       |\n|  |_|      |\n|       _   |\n|      |_|  |\n|___________|" << endl;
    }

    if (x==3){
        cout << " ___________\n|  _        |\n| |_| _     |\n|    |_| _  |\n|       |_| |\n|___________|" << endl;
    }
    if (x==4){
        cout << " ___________\n|  _     _  |\n| |_|   |_| |\n|  _     _  |\n| |_|   |_| |\n|___________|" << endl;
    }

    if (x==5){
        cout << " ___________\n|  _     _  |\n| |_| _ |_| |\n|  _ |_| _  |\n| |_|   |_| |\n|___________|" << endl;
    }

    if (x==6){
        cout << " ___________\n|  _  _  _  |\n| |_||_||_| |\n|  _  _  _  |\n| |_||_||_| |\n|___________|" << endl;
    }
}

int main()
{
    cout << "Welcome to Dice Roll 1.0\n" << endl;
    int n, x, victory=0, defeat=0;

    while (1){
        srand(time(0));
        x = (1+rand()%6);

        cout << "Enter 0 to quit.\nEnter roll value[1-6]: ";
        cin >> n;
        if (n==0){
            cout << "\nThank you for playing!" << endl;
            cout << "Win: " << victory << endl;
            cout << "Lose: " << defeat << "\n" << endl;
            break;
        }

        else{
            cout << "\nRequired Roll:" << endl;

            pc_roll(x);

            cout << "\nYour Roll:" << endl;

            your_roll(n);

            if (x==n){
                victory++;
                cout << "\nVictory!" << endl;
                cout << "Win: " << victory << endl;
                cout << "Lose: " << defeat << "\n" << endl;
            }

            else{
                defeat++;
                cout << "\nDefeat!" << endl;
                cout << "Win: " << victory << endl;
                cout << "Lose: " << defeat << "\n" << endl;
            }
        }
    }
    system("pause");

    return 0;
}
