% Facts about student and teacher
studies(charlie, csc135).   % Charilie studies csc135
studies(olivia, csc135). 
studies(jack, csc131). 
studies(arthur, csc134). 

teaches(kirke, csc135). 	% Kirke teaches csc135
teaches(collins, csc131). 
teaches(collins, csc171).
teaches(juniper, csc134). 

% Rules for professor relationship
professor(X, Y) :- teaches(X, C), studies(Y, C).

% Quries

?- studies(charlie, What).
?- professor(kirke, Students).