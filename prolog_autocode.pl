% This file contains a Prolog program that generates code in C++ and Rust based on a set of specifications.
% The code defines syntax rules for different constructs in C++ and Rust, such as assignments, loops, if-else statements, do-while loops, while loops, and print statements.
% The `generate_code/3` predicate is the main entry point for generating code. It takes the target language (either "cpp" or "rust"), a list of specifications, and returns the generated code as a string.

% Syntax rules for C++
syntax(cpp, assign(Var, Value), Code) :-
    format(atom(Code), '~w = ~w;', [Var, Value]).

syntax(cpp, loop(Var, Start, End, Body), Code) :-
    maplist(generate(cpp), Body, BodyCode),
    atomics_to_string(BodyCode, '\n    ', BodyCodeStr),
    format(atom(Code), 'for (int ~w = ~w; ~w < ~w; ++~w) {\n    ~w\n}', [Var, Start, Var, End, Var, BodyCodeStr]).

syntax(cpp, if_else(Cond, Then, Else), Code) :-
    maplist(generate(cpp), Then, ThenCode),
    maplist(generate(cpp), Else, ElseCode),
    atomics_to_string(ThenCode, '\n    ', ThenCodeStr),
    atomics_to_string(ElseCode, '\n    ', ElseCodeStr),
    format(atom(Code), 'if (~w) {\n    ~w\n} else {\n    ~w\n}', [Cond, ThenCodeStr, ElseCodeStr]).

syntax(cpp, do_while(Cond, Body), Code) :-
    maplist(generate(cpp), Body, BodyCode),
    atomics_to_string(BodyCode, '\n    ', BodyCodeStr),
    format(atom(Code), 'do {\n    ~w\n} while (~w);', [BodyCodeStr, Cond]).

syntax(cpp, while(Cond, Body), Code) :-
    maplist(generate(cpp), Body, BodyCode),
    atomics_to_string(BodyCode, '\n    ', BodyCodeStr),
    format(atom(Code), 'while (~w) {\n    ~w\n}', [Cond, BodyCodeStr]).

syntax(cpp, print(Value), Code) :-
    format(atom(Code), 'std::cout << ~w << std::endl;', [Value]).

% Syntax rules for Rust
syntax(rust, assign(Var, Value), Code) :-
    format(atom(Code), 'let mut ~w = ~w;', [Var, Value]).

syntax(rust, loop(Var, Start, End, Body), Code) :-
    maplist(generate(rust), Body, BodyCode),
    atomics_to_string(BodyCode, '\n    ', BodyCodeStr),
    format(atom(Code), 'for ~w in ~w..~w {\n    ~w\n}', [Var, Start, End, BodyCodeStr]).

syntax(rust, if_else(Cond, Then, Else), Code) :-
    maplist(generate(rust), Then, ThenCode),
    maplist(generate(rust), Else, ElseCode),
    atomics_to_string(ThenCode, '\n    ', ThenCodeStr),
    atomics_to_string(ElseCode, '\n    ', ElseCodeStr),
    format(atom(Code), 'if ~w {\n    ~w\n} else {\n    ~w\n}', [Cond, ThenCodeStr, ElseCodeStr]).

syntax(rust, do_while(Cond, Body), Code) :-
    maplist(generate(rust), Body, BodyCode),
    atomics_to_string(BodyCode, '\n    ', BodyCodeStr),
    format(atom(Code), 'loop {\n    ~w\n    if !~w {\n        break;\n    }\n}', [BodyCodeStr, Cond]).

syntax(rust, while(Cond, Body), Code) :-
    maplist(generate(rust), Body, BodyCode),
    atomics_to_string(BodyCode, '\n    ', BodyCodeStr),
    format(atom(Code), 'while ~w {\n    ~w\n}', [Cond, BodyCodeStr]).

syntax(rust, print(Value), Code) :-
    format(atom(Code), 'println!(~w );', [Value]).

% Generate code based on the given language and specifications
generate(Lang, Spec, Code) :-
    (syntax(Lang, Spec, Code) ->
        format('Generated: ~w~n', [Code])
    ; 
        format('Failed to generate code for: ~w~n', [Spec]),
        fail).

% Main predicate to initiate code generation
generate_code(Lang, Specs, Code) :-
    findall(C, (member(Spec, Specs), generate(Lang, Spec, C)), CodeList),
    atomics_to_string(CodeList, '\n', Code).
