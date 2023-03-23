# qcrack-rsa

use python primesto.py <any integer> 
python primesto.py 100

will print out 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


calculate N = 23 * 41 = 943

so run

python crack_rsa.py 943

If it fails either with an error or with a p or q of 1, just run it over and over again, it means the g value wasn't suitable 