freqToFunc :: String -> Int->Int
freqToFunc ('+':cs) = (+) (read cs :: Int)
freqToFunc ('-':cs) = flip (-) (read cs :: Int)
freqToFunc _ = id

main = do
	input <- lines `fmap` getContents
	print $ foldr (.) id (fmap freqToFunc input) 0
