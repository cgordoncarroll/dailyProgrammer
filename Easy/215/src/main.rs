extern crate num;

use std::io;

fn main() {
    let mut buf = io::stdin();
    println!("Base Number: ");
    let mut raw_b = String::new();
    buf.read_line(&mut raw_b).ok().expect("Failed to read base number");
    println!("Starting Number: ");
    let mut raw_n = String::new();
    buf.read_line(&mut raw_n).ok().expect("Failed to read starting number");

    let b: u64 = raw_b.to_string().trim().parse::<u64>().ok().unwrap();
    let n: usize = raw_n.to_string().trim().parse::<usize>().ok().unwrap();

    floyd(b, n);
}

fn floyd(start: u64, power: usize) {
    let mut tortoise = power_sum(start.clone(), power);
    let mut hare = power_sum(power_sum(start.clone(), power), power);

    while tortoise != hare {
        tortoise = power_sum(tortoise, power);
        hare = power_sum(power_sum(hare, power), power);
    }

    // If tortoise is 1, print that
    if tortoise == 1{
        println!("Found cycle of repeating 1's.");
    } else {
        let mut done = false;
        println!("Found {}-sad cycle", power.to_string());
        while !done {
            tortoise = power_sum(tortoise, power);
            print!("{}", tortoise.to_string());
            if tortoise == hare {
                done = true;
            } else {
                print!(",");
            }
        }
        println!("");
    }
}

fn power_sum(mut x: u64, power: usize) -> u64 {
    let mut sum = 0;
    while x > 0 {
        let digit = x % 10;
        sum += num::pow(digit, power);
        x /= 10;
    }
    sum
}
