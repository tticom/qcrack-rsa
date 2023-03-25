# qcrack-rsa

An implementation of the algorithm described in Veratasiums Youtube video

[![How Quantum Computers Break The Internet... Starting Now](https://img.youtube.com/vi/UrdExQW0cs/default.jpg)](https://www.youtube-nocookie.com/embed/-UrdExQW0cs)


use python primesto.py <any integer> 
python primesto.py 100

will print out 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


calculate N
23 * 41 = 943

so run

python crack_rsa.py 943

It should just keep going until it finds a g that works

991*997
python .\crack_rsa.py 988027

Is just beyond the limits of my machine and/or patience
