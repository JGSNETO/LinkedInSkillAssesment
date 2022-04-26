/**
 * @file Q3.cpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-04-06
 * 
 * @copyright Copyright (c) 2022
 * https://en.cppreference.com/w/cpp/language/bit_field
 * https://stackoverflow.com/questions/67398921/smallest-size-of-bit-field#:~:text=The%20size%20of%20child_t%20is,type%20of%20age%20and%20size%20.
What is the smallest size a variable of the type child_t may occupy in memory?
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    unsigned int  size   : 2;
}child_t;

 */

#include <iostream>

typedef struct {
    unsigned int  age    : 4; // Size 4 (Packed attribute)
    unsigned char gender : 1; // Size 1 (Packed attribute)
    unsigned int  size   : 2; // Size 2 (Packed attribute) 
}child_t;
/*7 bits cabem em 1 byte*/
int main()
{
    std::cout << "Age: " << sizeof(struct child) << "\n";
    system("PAUSE");
    return 0;

}