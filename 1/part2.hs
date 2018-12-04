import System.IO.Unsafe

disp a = let io = unsafePerformIO $ print a
		 in seq io a

freqToFunc :: String -> Int->Int
freqToFunc ('+':cs) = (+) (read cs :: Int)
freqToFunc ('-':cs) = flip (-) (read cs :: Int)
freqToFunc _ = id

firstFreq :: [Int->Int] -> [Int] -> Int -> Int
firstFreq (f:fs) xs n = let res = f ( n)
						in if n `elem` xs
						   then n
						   else firstFreq fs ( n:xs) res

main = do
	input <- lines `fmap` getContents
	let freqs = fmap freqToFunc input
	print $ firstFreq (cycle freqs) [] 0