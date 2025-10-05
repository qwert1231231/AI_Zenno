// Minimal C++ AI core placeholder
#include <iostream>

int compute_heavy(int x) {
    // placeholder heavy computation
    return x * x;
}

#ifdef BUILD_TEST
int main() {
    std::cout << "compute_heavy(4) = " << compute_heavy(4) << std::endl;
    return 0;
}
#endif
