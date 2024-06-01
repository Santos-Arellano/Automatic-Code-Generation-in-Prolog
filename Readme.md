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

Prolog Code Generation Workflow
1. Predicates Overview
syntax/3 Predicate
Purpose: Generates C++ code based on specified patterns (Spec) and language (Lang).
Usage: Called with syntax(Lang, Spec, Code), where Lang specifies the target language (e.g., cpp) and Spec defines the code structure to be generated.
Implementation: Typically uses format/3 to construct code strings and may recursively call generate(Lang, Spec, Code) for nested structures.
generate/3 Predicate
Purpose: Orchestrates the generation process by calling syntax(Lang, Spec, Code) and handling success or failure.
Usage: Initiates code generation with generate(Lang, Spec, Code), where Lang specifies the target language and Spec defines the specific code structure to generate.
Implementation: Verifies if syntax(Lang, Spec, Code) succeeds and optionally provides debugging or error messages.
generate_code/3 Predicate
Purpose: Acts as the main entry point to generate code for a list of specifications (Specs) in a specified language (Lang).
Usage: Called with generate_code(Lang, Specs, Code), where Lang specifies the target language and Specs is a list of code specifications.
Implementation: Uses findall/3 to collect generated code snippets (C) for each Spec in Specs, then concatenates them into a single string using atomics_to_string/3.
2. Built-in Predicates
findall/3
Purpose: Collects all instances of a specified term that satisfy a goal.
Usage: findall(X, Goal, List), collects all instances of X that satisfy Goal into List.
Example: findall(X, member(X, [a, b, c]), List) collects all elements in [a, b, c] into List.
format/2 and format/3
Purpose: Generates formatted strings.
Usage: format(Format, Arguments) formats Arguments according to Format and outputs the result.
Example: format(atom(Code), 'for (int ~w = ~w; ~w < ~w; ++~w) {\n ~w\n}', [Var, Start, Var, End, Var, BodyCodeStr]) formats a C++ loop construct.
atom/1
Purpose: Converts a term to an atomic term (an atom).
Usage: atom(Term) converts Term to an atom.
Example: atom('hello') creates the atom hello.
maplist/2
Purpose: Applies a predicate to each element of a list.
Usage: maplist(Pred, List) applies Pred to each element of List.
Example: maplist(number, [1, 2, 3]) succeeds if each element is a number.
3. Nesting Code Generation Capabilities
Description: Prolog's recursive predicate capabilities enable nested code generation.
Usage: Inside syntax/3, you can call generate(Lang, SubSpec, SubCode) for nested specifications (SubSpec) within Spec.
Example: Generating a loop where the loop body (Body) itself contains further specifications (e.g., assignments or nested loops).

