// Project Euler Problem #2
// Sums even Fibonacci numbers up to 4,000,000
// and prints the result.
#include <cstdlib>
#include <iostream>

using namespace std;

bool iseven (int& num) {
   if (num % 2 == 0) return true;
   else return false;
}

int main (int argc, char** argv) {
   int sum = 0;
   int limit = 4000000;
   int fib1{1};
   int fib2{2};
   int curr;
   
   sum += fib2;
   while (curr <= limit) {
      curr = fib1 + fib2;
      if (curr >= limit) break;
      if (iseven (curr)) sum += curr;
      fib1 = fib2;
      fib2 = curr;
   }
   cout << "Sum = " << sum << endl;
   return 0;
}

