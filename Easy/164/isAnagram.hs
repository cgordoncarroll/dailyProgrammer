import Data.Char
main = do
    putStrLn "Enter Word 1:"
    word1 <- getLine
    putStrLn "Enter Word 2:"
    word2 <- getLine
    let upperW1 = map toUpper word1
        upperW2 = map toUpper word2
    if (quicksort(upperW1) == quicksort(upperW2)) 
        then putStrLn "Words are Anagrams."
        else putStrLn "Words are not Anagrams."

quicksort :: Ord a => [a] -> [a]
quicksort [] = []
quicksort (p:xs) = quicksort smaller ++ [p] ++ quicksort bigger
    where
        smaller = [ y | y <-xs, y < p ]
        bigger = [ y | y <-xs, y >= p]
