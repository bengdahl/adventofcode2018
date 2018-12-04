import Data.List

hasDouble :: String -> Bool
hasDouble = any ((==2).snd).map (\a@(x:xs) -> (x,length a)).group.sort

hasTriplet :: String -> Bool
hasTriplet = any ((==3).snd).map (\a@(x:xs) -> (x,length a)).group.sort

main = do
    items <- lines `fmap` getContents
    let twos = length $ filter hasDouble items
        threes = length $ filter hasTriplet items
    print $ twos * threes