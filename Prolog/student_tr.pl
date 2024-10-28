% Facts
student(john).
student(mary).
student(alice).

professor(smith).
professor(jones).
professor(brown).

teaches(smith, math).
teaches(smith, physics).
teaches(jones, chemistry).
teaches(brown, computer_science).
teaches(brown, data_science).

% Rules
% A student is taught by a professor if that professor teaches a subject.
taught_by(Student, Professor) :-
    student(Student),
    teaches(Professor, Subject),
    enrolled_in(Student, Subject).

% Facts about which student is enrolled in which subject
enrolled_in(john, math).
enrolled_in(john, chemistry).
enrolled_in(mary, chemistry).
enrolled_in(mary, computer_science).
enrolled_in(alice, data_science).

% Example Queries:
% ?- taught_by(john, Professor).
% ?- taught_by(mary, Professor).
% ?- taught_by(alice, Professor).
