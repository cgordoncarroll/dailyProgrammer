main = do
    print $ divisibleBy3And5
divisibleBy3And5 :: [Integer]
divisibleBy3And5 = take 100 [x | x <- [1..], x `mod` 3 == 0, x `mod` 5 == 0]
