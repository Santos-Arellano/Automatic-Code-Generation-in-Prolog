#Steps
1. Install swipl 8.4.2
1. Make sure that you have the path to swipl in your system variables 
2. git clone 
3. Make a virtual environment   
4. pip install pyswipl
5. Once in the interface: Language (cpp/rust): Type cpp or rust
5. Specifications: just put the high level instruction. example:

Language: cpp

Specifications: assign(x, 10), loop(i, 0, 5, [assign(sum, 'sum + i')]), if_else('x > 0', [assign(y, 'x - 1')], [assign(y, 'x + 1')])
