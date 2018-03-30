\version "2.18.0"
\language "english"
#(set-default-paper-size "letter")
\relative c'{
\set Staff.extraNatural = ##f

% key of c:
\octaveCheck c'
c8^"key of c" d e f g f e d
c8 e g c b g f d

% key of f:
\octaveCheck c'
f8^"key of f" g a bf c bf a g
f8 a c f e c bf g

% key of bf:
\octaveCheck c'
bf8^"key of bf" c d ef f ef d c
bf8 d f bf a f ef c

% key of ef:
\octaveCheck c'
ef8^"key of ef" f g af bf af g f
ef8 g bf ef d bf af f

% key of af:
\octaveCheck c'
af8^"key of af" bf c df ef df c bf
af8 c ef af g ef df bf

% key of df:
\octaveCheck c'
df8^"key of df" ef f gf af gf f ef
df8 f af df c af gf ef

% key of gf:
\octaveCheck c'
gf8^"key of gf" af bf cf df cf bf af
gf8 bf df gf f df cf af

% key of b:
\octaveCheck c'
b8^"key of b" cs ds e fs e ds cs
b8 ds fs b as fs e cs

% key of e:
\octaveCheck c'
e8^"key of e" fs gs a b a gs fs
e8 gs b e ds b a fs

% key of a:
\octaveCheck c'
a8^"key of a" b cs d e d cs b
a8 cs e a gs e d b

% key of d:
\octaveCheck c'
d8^"key of d" e fs g a g fs e
d8 fs a d cs a g e

% key of g:
\octaveCheck c'
g8^"key of g" a b c d c b a
g8 b d g fs d c a
}

