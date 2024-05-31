% Sintaxis de C++
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

% Sintaxis de Rust
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

% Generar código
generate(Lang, Spec, Code) :-
    Spec =.. [Functor | Args],
    format('Generating code for: ~w ~w ~w~n', [Lang, Functor, Args]),  % Línea de depuración
    Call =.. [Functor | Args],
    (syntax(Lang, Call, Code) ->
        format('Generated: ~w~n', [Code])  % Línea de depuración
    ; 
        format('Failed to generate code for: ~w ~w ~w~n', [Lang, Functor, Args]),
        fail).

% Predicado principal para iniciar la generación de código
generate_code(Lang, Specs, Code) :-
    findall(C, (member(Spec, Specs), generate(Lang, Spec, C)), CodeList),
    atomics_to_string(CodeList, '\n', Code).
