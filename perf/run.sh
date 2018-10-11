#!/usr/bin/env bash

iterations=1000
n_pow_start=7
n_pow_max=16
out_file="$(\date +'%F_%T').bench"

for pow in $(seq "$n_pow_start" "$n_pow_max")
do
    n=$(echo "2^${pow}" | bc)
    ./benchmark.py "$n" -i "$iterations" >> "$out_file"
done
