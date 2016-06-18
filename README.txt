# STEP_GOOGLE_HW4
step hw4
pagerank.py stops the calculation if nodes' scores remain unchanged after each round.  
pagerank_with_different_precision.py stops the calculation if the change of nodes' scores after each round is smaller than 0.00001.

I have altered the contents in "middle_data.txt". I think it is the data that you want us to calculate on.
Also, my answer for "small_data.txt" is different from the answer given in the slide. I could not figure out the reason. Maybe, I have comprehended the concept of pagerank algorithm wrongly. I would like to hear your suggestions.

the answer of the small_data.txt
(1)pagerank.py result:

start calculation of the score of each person
the balance has been reached in round 110
D has score 107.69230769230768
E has score 107.69230769230768
C has score 107.69230769230768
B has score 107.69230769230768
G has score 107.69230769230768
F has score 53.84615384615384
A has score 107.69230769230768

(2)pagerank_with_different_precision.py

start calculation of the score of each person
the balance has been reached in round 47
C has score 107.69230723381042
F has score 53.84615659713745
D has score 107.69230723381042
B has score 107.69230723381042
A has score 107.69230723381042
E has score 107.69230723381042
G has score 107.69230723381042

the answer of the medium_data.txt
(1)pagerank.py
the calculation does not converge within 1000 rounds.

(2)pagerank_with_different_precision.py

start calculation of the score of each person
the balance has been reached in round 130
J has score 138.7271571353741
N has score 159.63190274520795
W has score 2.710505431213761e-18
Q has score 39.98703935482538
U has score 0
A has score 154.75360078634043
S has score 140.8540031242196
P has score 90.58458011051998
V has score 1.3552527156068805e-18
R has score 39.98704274860049
F has score 136.1615058619789
I has score 112.0269649947956
O has score 159.94816737116525
M has score 74.62139096448014
T has score 60.09718075189647
L has score 79.97407841278168
G has score 113.87312823241092
E has score 227.0939704994438
B has score 168.1827623287452
D has score 147.98960428893778
H has score 34.68179061368767
C has score 71.02789414442604
K has score 149.79623553016418

the answer of the large_data.txt
(1)pagerank.py
the calculation does not converge within 1000 rounds

(2)pagerank_with_different_precision.py

the calculation converged in round 921

