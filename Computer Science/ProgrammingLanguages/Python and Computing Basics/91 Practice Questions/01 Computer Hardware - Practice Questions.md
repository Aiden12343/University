# 1.13 Exercises

Exercises are ordered by increasing integration. Do not run software to substitute for reasoning; Chapter 4 will establish a controlled programming environment.

### 1.13.1 Recall and classification

1. Define *physical state*, *logical state*, *representation*, and *interpretation*. Give one example in which all four are distinct.
2. Explain why a noise margin improves reliability. Do not use the phrase “because binary is simpler” without identifying what is being distinguished.
3. Reproduce the truth tables for NOT, AND, OR, and XOR from memory.
4. Classify each as combinational or stateful: inverter, half adder, register, full adder without retained carry, clocked accumulator.
5. State the difference between a register and main memory without claiming that either is physically instantaneous.

### 1.13.2 Representation practice

6. Decode the unsigned binary numeral `11010110` into decimal, showing each positional contribution.
7. Convert decimal 93 to binary by repeated division, retaining every quotient and remainder.
8. How many distinct patterns exist in 12 bits? What is the greatest 12-bit unsigned integer?
9. Under eight-bit two’s complement, decode `11110110`. Show the negative high-position contribution and every positive contribution.
10. Explain why `01000001` is insufficient by itself to establish that the stored value is the letter A.

### 1.13.3 Logic and state

11. Write the eight-row truth table for a majority function over three inputs: output 1 exactly when at least two inputs are 1.
12. Express that majority function using only AND and OR. Explain why each input combination with at least two 1s activates the result.
13. Design the abstract transition rule for a two-bit counter that advances through `00`, `01`, `10`, `11`, then returns to `00`. Distinguish current state from next state.
14. A clocked register requires its input to be stable for a period before an edge. Explain why the truth table of the stored Boolean value alone cannot express this requirement.

### 1.13.4 Machine tracing

15. Extend the teaching ISA with `SUB D, A, B`, meaning register `D` receives `A-B`. Write a five-instruction program that computes memory[100] minus memory[101] and stores the result at address 103. Trace every register and changed memory location.
16. Add `JZ R, a`, meaning set `PC` to address `a` when register `R` contains zero; otherwise leave the already advanced `PC` unchanged. Construct and trace a program that stores 1 at address 200 when memory[100] is zero and stores 0 otherwise.
17. In the original addition trace, suppose address 2 is accidentally changed from `ADD R2, R0, R1` to `ADD R2, R0, R0`. Identify the earliest state divergence from the correct trace. Explain why examining only final memory gives weaker diagnostic evidence.

### 1.13.5 Integrated exercise

18. Produce a complete paper design for a four-state traffic signal controller. Your answer must include:
    - the bit pattern assigned to each state;
    - the interpretation contract for input sensors;
    - a current-state/next-state transition table;
    - the outputs activated in each state;
    - the role of clocked storage;
    - one invalid physical input condition;
    - one claim at each of the device, logic, architecture, and application levels;
    - a trace of at least six clock edges.

The exercise is complete only if another reader can distinguish every physical condition, bit pattern, abstract state, transition rule, and externally visible effect without inferring an unstated convention.

### 1.13.6 Electrical and timing derivations

19. Under the stated ideal models, calculate current and power for 3.3 volts across 2,200 ohms. State every unit and identify at least three reasons a physical circuit may differ.
20. A node has effective capacitance 25 picofarads and changes by 0.8 volts. Calculate charge moved. If average current is 0.5 milliampere, calculate transition time under the constant-current simplification.
21. Given output/input voltage guarantees, calculate high and low noise margins. Classify three intermediate voltages as valid low, indeterminate, or valid high.
22. Draw a CMOS inverter at the switch-abstraction level. Trace charging, discharging, short-circuit transition current, and capacitive energy for each input transition.
23. Three paths have delay lists \((80,120,60)\), \((90,90,90)\), and \((50,200)\) picoseconds. Add clock-to-output, setup, and uncertainty. Identify the critical path and maximum simplified clock frequency.
24. If voltage scales from 1.0 to 0.75 under unchanged activity, capacitance, and frequency, calculate the dynamic-power model ratio. Explain why actual chip power need not follow exactly.

### 1.13.7 Boolean construction

25. Enumerate all sixteen two-input, one-output Boolean functions as four-bit output columns. Identify constants, projections, NOT variants, AND, OR, XOR, equality, NAND, and NOR.
26. Prove every Boolean identity in §1.10.7 by exhaustive truth tables. Then derive at least four algebraically from others.
27. Build XOR using only NAND. Count gates and determine logical depth under unit gate delay.
28. Express a three-input majority function using (a) sum-of-products, (b) product-of-sums, and (c) NAND only. Prove equivalence.
29. Design a four-to-one multiplexer from two-to-one multiplexers. Calculate dependency depth and list signals operating concurrently.
30. Design a three-to-eight decoder with enable. Specify every invalid or inactive condition.
31. For \(y=(a\land b)\lor(\lnot a\land c)\), trace a transition causing a static hazard under assigned path delays. Show how the consensus term prevents the output pulse.

### 1.13.8 Arithmetic circuits and representation

32. Derive full-adder sum and carry expressions from its eight-row truth table.
33. Trace an eight-bit ripple-carry addition in which carry propagates through every position. Compare with a case in which each bit generates or kills carry immediately.
34. Derive four-bit carry-lookahead expressions \(c_1\) through \(c_4\) from generate and propagate signals.
35. List every four-bit pattern under unsigned and two’s-complement interpretations. For each addition of two signed values, classify correct result, signed overflow, and carry.
36. Prove algebraically that complement-and-add-one forms the additive inverse modulo \(2^n\).
37. Design an add/subtract unit that XORs each \(b\) bit with a subtract control and uses that control as initial carry. Trace both operations.
38. Multiply two six-bit unsigned values by partial products. Determine required full result width and the consequence of retaining only six bits.
39. Design a variable logical shifter from multiplexer stages for shift amounts 1, 2, and 4. Explain how a three-bit amount composes them.
40. Specify ALU control, outputs, and flags for add, subtract, AND, OR, XOR, and signed/unsigned less-than.

### 1.13.9 State and clocking

41. Derive a D latch from an SR latch. Trace data changes while disabled, while enabled, and at disable transition.
42. Given minimum/maximum clock-to-output, path, setup, hold, and skew values, perform separate setup and hold checks. Do not repair one by changing an irrelevant quantity.
43. Explain metastability without saying the flip-flop “randomly chooses.” Identify the analogue cause, resolution interval, and probabilistic reliability measure.
44. Design a modulo-six counter with three state bits. Mark unused encodings and specify recovery from each.
45. Translate the turnstile state table into one-hot and binary encodings. Compare number of state bits and next-state logic.
46. Design a handshake for transferring a stable 16-bit word between unrelated clock domains. Trace request, capture, acknowledgement, and release.
47. Compare SRAM and DRAM cells, read behaviour, refresh, density, latency, and common hierarchy roles without treating either as an ISA guarantee.

### 1.13.10 Datapath and microarchitecture

48. Decode and encode twenty instructions under the fictional §1.10.23 format. Identify unused encodings and explain how an assembler should reject an out-of-range register.
49. Draw a single-cycle datapath for register ADD, immediate ADD, load, store, and conditional branch. Label every multiplexer choice and control signal.
50. Convert the datapath to a multi-cycle controller. Write a state-transition table and control word for each phase.
51. For ten instructions, construct a five-stage pipeline timing table. Mark structural, data, load-use, and control hazards; apply forwarding and stalls.
52. Compare branch predictors that always choose not taken, use one last-outcome bit, and use a two-bit saturating counter on a supplied branch trace.
53. Give an instruction sequence exhibiting true, anti-, and output name dependencies. Show which register renaming removes and which it cannot.
54. For a cache with a specified capacity, line size, associativity, and address width, calculate offset, set, tag, data capacity, and metadata lower bound.
55. Trace a memory-address sequence through direct-mapped and four-way caches. Classify compulsory, capacity, and conflict misses under the chosen model.
56. Construct a false-sharing example with two cores and two independent counters. Draw line ownership transfers and propose two layout repairs.
57. Calculate average access time for a two-level cache and memory hierarchy using conditional miss rates. Explain why summing independent penalties incorrectly can double-count.
58. Design interrupt and DMA handling for a network receive queue. Track buffer ownership at every step and identify the effect of process termination.
59. Add parity to eight data bits. Demonstrate every one-bit error is detected and construct a two-bit error that is not.

### 1.13.11 Integrated hardware dossier

60. Specify a complete eight-bit stored-program processor. Include:
    - instruction formats and illegal encodings;
    - eight-register file and special program-counter behaviour;
    - ALU operations and flags;
    - one-cycle or multi-cycle datapath;
    - controller transition table;
    - memory and device address map;
    - interrupt entry and return;
    - a direct-mapped cache;
    - a ten-instruction program and cycle trace;
    - critical-path estimate;
    - three failure conditions;
    - one implementation variation preserving the same ISA.

The dossier is correct only if another reader can reproduce every architectural state transition without guessing and can separately identify all microarchitectural choices.
