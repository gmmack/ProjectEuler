// Project Euler Problem #1
// Sum multiples of 3 and 5 up to 1000
#include <cstdlib>
#include <iostream>

using namespace std;

int sumof3s (int limit) {
   int sum = 0;
   for (int i=3; i<limit; i+=3) {
      sum += i;
   }
   return sum;
}

int sumof5s (int limit) {
   int sum = 0;
   int index = 5;
   while (index<limit) {
      sum += index;
      index += 5;
   }
   return sum;
}

int main (int argc, char** argv) {
   int sum = 0;
   for (int i=1; i<1000; ++i) {
      if (i%5 == 0 || i%3 == 0) sum += i;
   }
   cout << "Sum = " << sum << endl;
   return 0;
}

