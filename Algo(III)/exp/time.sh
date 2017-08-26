start=$(gdate +%s.%N)
($1 < $2) > temp.txt 
dur=$(echo "$(gdate +%s.%N) - $start" | bc)
printf "%.6f" $dur	