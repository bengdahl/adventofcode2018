import Data.List
import System.IO.Unsafe

disp a = seq (unsafePerformIO $ print a) a

pairs :: [a] -> [(a, a)]
pairs l = [(x,y) | (x:ys) <- tails l, y <- ys]

areCorrect a b = 1 == (length $ filter (\(a,b) -> a/=b) (zip a b))

main = do
    items <- lines `fmap` getContents
    print $ (\(a,b) -> [x | (x,y) <- zip a b, x==y]) . disp . head . filter (\a@(x,y) -> seq ( a) $ areCorrect x y) . pairs $ items