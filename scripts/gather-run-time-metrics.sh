#!/usr/bin/env bash

# default values
iterations=1000
n_pow_start=0
n_pow_end=16

while [[ $# -gt 0 ]]
do
    key="$1"
    value="$2"

    case "$key" in
        -i|--iterations)
            iterations="$value"
            shift; shift
            ;;

        -s|--n-pow-start)
            n_pow_start="$value"
            shift; shift
            ;;

        -e|--n-pow-end)
            n_pow_end="$value"
            shift; shift
            ;;

        *)
            ;;
    esac
done

for pow in $(seq "$n_pow_start" "$n_pow_end")
do
    n=$(echo "2^${pow}" | bc)
    dir="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"
    "$dir"/benchmark.py "$n" -i "$iterations"
done
