# This converts the given text to handwritten text.

import pywhatkit as pw

text = '''
Hii, I am Ayush Agrawal
I am a programmer.
This is a code to convrt textual content to handwritten thing 

Here is a the example of Printing hello world in cpp

# include <iostream>
using namespace std;
int main() {
    cout<<"Hello World";
}
'''

pw.text_to_handwriting(text)
# It has 3 arguments ->> text, file name 'z.png', color code -> [0,0,0](rbg) for black