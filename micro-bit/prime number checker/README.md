# Prime Number Checker using micro:bit

## Project Summary

* **Concept:** Number theory, divisibility, prime numbers, integer operations
* **Project:** Press Button A to check whether a given number is prime; the device displays the number's divisors as it tests and confirms "Prime Number" if none are found
* **Components:** micro:bit + virtual display
* **Math Link:** Divisibility rules, factors, prime vs composite numbers
* **Simulate:** Basic primality test with loop and modulo logic

---

## List of Materials Required

* micro:bit (physical device or Tinkercad simulator)
* micro:bit 5×5 LED display (built-in)
* Button A (built-in)
* Computer with internet access (for Tinkercad or MakeCode editor)

---

## How to Build

### Introduction

This project turns the micro:bit into a prime number checker. When Button A is pressed, the device tests whether a stored number `num` is prime by iterating through potential divisors from 2 up to √num. Any divisors found are displayed on screen; if none exist, it confirms the number is prime with a message.

### Working Principle

* `num` is the number to test (set in the **on start** block)
* `i` is the current divisor being tested, starting at 2
* `isPrime` is a flag (1 = prime, 0 = not prime)
* The loop runs while `i × i ≤ num`
* If `num % i == 0`, then `i` is a divisor — it is displayed and `isPrime` is set to 0
* `num / i` (the paired divisor) is also displayed
* After the loop, if `isPrime` is still 1, "Prime Number" is shown

### Controls

* **Button A pressed:** Run the prime check on `num`
* **On start:** Set `num` to the target value and display it

---

## Detailed Guidelines

### DIY Tutorial Guide

You can build this in the [MakeCode editor](https://makecode.microbit.org) or Tinkercad Circuits. No extra wiring is needed — the button and display are built into the micro:bit.

---

### Procedure Steps

1. Open the MakeCode micro:bit editor or create a new micro:bit circuit in Tinkercad.
2. Select **Blocks** as the coding mode.
3. Create variables: `num`, `i`, and `isPrime`.

**On Start block:**
4. Set `num = 5` (or any number you wish to test)
5. Show number `num`

**On Button A Pressed block:**
6. Set `i = 2`
7. Set `isPrime = 1`
8. Add a **repeat while** loop with condition: `i × i ≤ num`
9. Inside the loop, add an **if** block: `if num % i == 0 then`
   * Show number `i`
   * Show number `num / i`
   * Set `isPrime = 0`
10. After the if block (still inside the loop): Set `i = i + 1`
11. After the loop, add an **if** block: `if isPrime == 1 then`
    * Show string `"Prime Number"`

12. Start the simulation or flash the device.

---

## How It Works

* The loop tests every integer `i` starting at 2. Because factors come in pairs around √num, checking only up to `i × i ≤ num` is sufficient to find all divisors.
* If any value of `i` divides `num` evenly (`num % i == 0`), both `i` and `num / i` are shown on the LED display, and the prime flag is cleared.
* If the loop ends with `isPrime` still equal to 1, no divisors were found and the display shows "Prime Number".
* This teaches learners about modulo arithmetic, loop conditions, and the mathematical definition of a prime number.

---

## Tips

* Change `num` in the **on start** block to test different numbers (e.g., 7, 13, 15, 29, 100).
* For large numbers the scrolling display may be slow — keep `num` under 100 for quick demos.
* Ask students to predict whether a number is prime before pressing Button A to build intuition.
* Pair with the multiplication table project to connect factors and multiples as complementary concepts.

---

## Testing

* Set `num = 5` and press Button A — the display should show "Prime Number".
* Set `num = 12` and press Button A — the display should scroll divisors (2, 6, 3, 4) and **not** show "Prime Number".
* Set `num = 1` — by convention 1 is not prime; verify `isPrime` stays 0 because the loop never executes when `i × i > 1` immediately (adjust initial logic if needed to handle this edge case).
* Set `num = 2` — the smallest prime; the loop condition `2 × 2 ≤ 2` is false immediately, so "Prime Number" should appear.
* Set `num = 9` — the display should show 3 and 3 as divisors, confirming 9 is not prime.

---

## Troubleshooting Guide

* **Issue:** Nothing happens when Button A is pressed.
  * **Possible causes:** Code is not inside the `on button A pressed` block, or the simulation is not running.
  * **Solution:** Ensure all logic (variable initialization, loop, and if checks) is placed inside the `on button A pressed` event block. Start the simulation.

* **Issue:** Every number is shown as "Prime Number" even when it is not.
  * **Possible causes:** `isPrime` is not being set to 0 when a divisor is found, or the modulo condition is incorrect.
  * **Solution:** Confirm the inner `if` block checks `num % i == 0` and sets `isPrime = 0` inside it.

* **Issue:** The loop runs forever or the device freezes.
  * **Possible causes:** `i` is never incremented inside the loop.
  * **Solution:** Verify `set i to i + 1` is placed at the end of the loop body, outside the divisor `if` block.

* **Issue:** The loop condition is wrong and some composite numbers pass as prime.
  * **Possible causes:** Loop condition uses `i ≤ num` instead of `i × i ≤ num`, which still works but is slower — or the condition uses `<` instead of `≤`.
  * **Solution:** Use `i × i ≤ num` for efficiency. Both `<` and `≤` are acceptable but `≤` is more correct.

* **Issue:** Divisors are displayed but "Prime Number" still appears at the end.
  * **Possible causes:** `isPrime` is being reset to 1 inside the loop after being set to 0.
  * **Solution:** Set `isPrime = 1` only once, before the loop begins, and never reset it inside the loop.

* **Issue:** `num = 1` is incorrectly labelled as prime.
  * **Possible causes:** The loop exits immediately (since `2 × 2 > 1`) and `isPrime` stays 1.
  * **Solution:** Add a check before the loop: `if num < 2 then set isPrime = 0` to handle the edge case.

---

### Extension Steps

1. Create variables `numA`, `numB`, `hcf`, `lcm`, and `temp`.
2. In **on start**, set `numA = 12` and `numB = 8`.
3. On **Button A pressed** — calculate and display HCF:
   * Copy `numA` and `numB` into working variables
   * Loop while the second value is not 0: store remainder, shift values, repeat
   * Show string `"HCF"` then show the result
4. On **Button B pressed** — calculate and display LCM:
   * Use the HCF already found: `lcm = (numA × numB) / hcf`
   * Show string `"LCM"` then show the result
5. On **shake** — swap `numA` and `numB` to explore a different pair.

### Math Link

* HCF and LCM directly reinforce understanding of prime factors and divisibility rules from the prime checker.
* Students can verify: for any two primes p and q, HCF = 1 and LCM = p × q.
* Connecting the three concepts — primes, HCF, and LCM — builds a complete picture of number theory at the foundational level.