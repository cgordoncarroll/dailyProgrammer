<?php

function quicksort($array){
    if( count($array) <= 1) {
        return $array;
    }

    $pivotPoint = $array[rand(0, count($array) - 1)];

    $smaller = array();
    $equal = array();
    $greater = array();
    foreach($array as $chunk) {
        if ($chunk < $pivotPoint) {
            $smaller[] = $chunk;
        } else if ($chunk === $pivotPoint) {
            $equal[] = $chunk;
        } else {
            $greater[] = $chunk;
        }
    }

    return array_merge(quicksort($smaller), $equal, quicksort($greater));
}

$array = [5, 12, -3, 570, -91];
print_r(quicksort($array));
