% Facts about genders
female(mary).
female(alice).
female(charlie).
female(eve).
female(frank).  % Added female sibling
male(john).
male(bob).
male(dave).

% Facts about family relationships
parent(john, alice).   % John is the parent of Alice
parent(john, bob).     % John is the parent of Bob
parent(mary, alice).   % Mary is the parent of Alice
parent(mary, bob).     % Mary is the parent of Bob
parent(alice, charlie). % Alice is the parent of Charlie
parent(bob, dave).     % Bob is the parent of Dave
parent(bob, eve).      % Bob is the parent of Eve
parent(alice, frank).  % Alice is the parent of Frank

% Defining relationships
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
sister(X, Y) :- sibling(X, Y), female(X).
brother(X, Y) :- sibling(X, Y), male(X).


% Grandparent relationship
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Aunt and uncle relationships
aunt(X, Y) :- sibling(X, Z), parent(Z, Y), female(X).
uncle(X, Y) :- sibling(X, Z), parent(Z, Y), male(X).

% Cousin relationship
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).

% Ancestor relationship
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(Z, Y), ancestor(X, Z).

% Example Queries:
% ?- mother(Mother, charlie).
% ?- grandparent(Grandparent, dave).
% ?- aunt(Aunt, dave).
% ?- uncle(Uncle, charlie).
% ?- cousin(Charlie, Cousin).
% ?- ancestor(Ancestor, frank).
% ?- sister(Sister, bob).
% ?- brother(Brother, alice).
