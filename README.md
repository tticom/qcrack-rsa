# qcrack-rsa

An implementation of the algorithm described in Veratasiums Youtube video

[![Watch the video](https://img.youtube.com/vi/UrdExQW0cs/0.jpg)](https://www.youtube.com/watch?v=-UrdExQW0cs)


<a href="https://www.youtube.com/watch?v=-UrdExQW0cs" target="_blank">
    How Quantum Computers Break The Internet... Starting Now
</a>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/-UrdExQW0cs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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
