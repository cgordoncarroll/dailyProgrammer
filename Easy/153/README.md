Pascal's Pyramid
=====

u may have seen Pascal's Triangle before. It has been known about for a long time now and is a very simple concept - it makes several appearances in mathematics, one of which is when you calculate the binomial expansion[1] .
If you've not seen it before, you can calculate it by first putting 1 on the outermost numbers:
1
1 1
1 _ 1
1 _ _ 1
1 _ _ _ 1
And then each number within the triangle can be calculated by adding the two numbers above it, to form this:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
It has several interesting properties, however what we're interested in is the 3-dimensional version of this triangle - Pascal's Pyramid.
It works in much the same way - the corner numbers are all 1s. However the edges are all layers of Pascal's triangle, and each inner number is the sum of the 3 numbers above it. Besides that there is nothing else to it.
