# 2.16 Exercises

### 2.16.1 Machine notation and translation

1. For the fictional 16-bit format in §2.2, encode `ADD R7, R2, R12` using opcode `0010`. Separate and label all four fields.
2. Invent one additional opcode requiring an immediate operand. Explain which existing field you repurpose and the range this choice permits.
3. Write assembly-like source for multiplying a non-negative integer by repeated addition. State a termination measure and the admitted-input condition.
4. Explain why an assembler cannot resolve an arbitrary forward label in a single irrevocable left-to-right emission pass unless it reserves or later repairs information.
5. Distinguish compile-time, link-time, load-time, and execution-time failures using one original example of each.

### 2.16.2 Language implementation reasoning

6. Classify each activity as parsing, semantic analysis, optimisation, code generation, interpretation, or linking: grouping tokens by grammar; resolving an external symbol; executing bytecode; proving a variable declaration exists; replacing a proven constant expression; selecting a target instruction.
7. Give a case in which JIT compilation is unlikely to recover its cost and a case in which it plausibly might. Name the workload properties rather than the product names.
8. Explain why a user-defined addition operation can make an apparently obvious algebraic optimisation invalid.
9. Draw a representation chain from higher-level source through an intermediate form to native instructions. For each arrow, name the program responsible for translation or execution.

### 2.16.3 Operating-system reasoning

10. A machine has one CPU core and three processes. A blocks on storage, B is runnable, and C is waiting for a network packet. State which can execute user instructions immediately and what events can change the others’ states.
11. Two processes each use virtual address `0x4000`. Give three mapping arrangements: isolated data, shared read-only code, and shared writable communication. State the permission and coordination implications.
12. Explain how a path can designate a different file without the path text changing. Distinguish directory entry, file object, open handle, and stored content.
13. A write call returns successfully, but power fails before data reaches persistent media. Explain why there is no contradiction unless the interface promised that durability level.
14. List the validation obligations of a kernel receiving an operation containing a user-space address and length.

### 2.16.4 Integrated exercise

15. Trace the life of a command-line program from source files to completion. Your account must include compiler or interpreter choice, object or bytecode representation, loader action, process creation, virtual-memory mapping, scheduling, one file read, one output write, and termination. At every step identify:
    - the active representation;
    - the component with authority;
    - retained state before and after;
    - one possible failure;
    - whether the claim is defined by a language, an ISA, an operating-system interface, or an empirical implementation.

### 2.16.5 Compiler and linker laboratory

16. Tokenise twenty expressions under an invented lexical grammar. Include longest-match conflicts, comments, Unicode identifiers, and indentation. State every ambiguity your grammar must settle.
17. Define a grammar for arithmetic with parentheses, unary minus, multiplication, and addition. Draw parse trees proving precedence and associativity.
18. Convert a three-branch source fragment into basic blocks and a control-flow graph. Translate name assignments to SSA form with merge operations.
19. For constant folding, dead-code elimination, common-subexpression elimination, and loop-invariant motion, give one valid and one invalid transformation distinguished by observable effects.
20. Design a two-pass assembler with labels, directives, symbol table, and relocation records. Hand-execute both passes on a twenty-line input.
21. Lay out text, read-only data, writable data, and zero-initialised regions for three object files. Resolve strong, weak, local, undefined, and duplicate symbols under an explicitly invented linker policy.
22. Calculate absolute and PC-relative relocations at several final addresses. Include one overflow and propose a linker diagnostic or relaxation.
23. Compare static and dynamic linking for update, memory sharing, deployment, startup, attack surface, and ABI compatibility.
24. Specify a calling convention for six integer arguments, one structure return, caller/callee-saved registers, stack alignment, and variadic calls. Trace a nested call.
25. Trace executable loading from path lookup through runtime entry, dynamic library resolution, constructors, source-level main, and termination.

### 2.16.6 Processes and scheduling

26. Draw state transitions among running, runnable, blocked, stopped, and terminated for two CPU-bound and two I/O-bound threads.
27. Compare round-robin schedules under five quantum sizes including measured context-switch cost. Calculate response, completion, wait, and overhead.
28. Construct a priority-starvation schedule and add ageing that eventually schedules the low-priority task.
29. Trace fork followed by exec, including address mappings, copy-on-write pages, descriptors, environment, process identifiers, and failed exec.
30. Demonstrate with a paper state graph how an inherited descriptor keeps a file or pipe endpoint alive.
31. Design a process supervisor with restart classifications, backoff, crash-loop limit, health evidence, and graceful stop.
32. Compare pipe, local socket, shared memory, file, and message queue for a one-gigabyte producer/consumer transfer. State framing, copies, synchronisation, crash behaviour, and authority.
33. Specify a request/reply protocol in which the client can time out after server success. Add operation identifiers and deduplication.

### 2.16.7 Virtual memory

34. Divide virtual addresses into page number and offset for several page sizes. Translate through supplied page tables and classify permission faults.
35. Design a two-level page table for a sparse address space. Calculate table memory under three populated-region patterns.
36. Trace demand paging for code, zero-filled anonymous memory, file-backed data, and a swapped page.
37. Trace copy-on-write after fork for a parent and two children. Count physical frames after selected writes.
38. Distinguish virtual size, resident set, proportional shared use, private dirty data, mapped files, and allocator retention for one process.
39. Construct a page-reference string that thrashes under a chosen frame allocation. Compare two replacement algorithms.
40. Design a memory-mapped record reader. Account for truncation, invalid offsets, concurrent writers, endianness, and durability.

### 2.16.8 Filesystems and devices

41. Draw directory entries, inode-like objects, hard links, symbolic links, open descriptions, and descriptors for a sequence of open, link, rename, unlink, duplicate, fork, and close operations.
42. Trace path resolution through relative components, symbolic links, a mount point, and insufficient traversal permission.
43. Design a path-safe file creation operation under a directory descriptor. Eliminate check/use re-resolution.
44. Compare buffered write, flush, kernel write, file synchronisation, directory synchronisation, and device completion under process-crash and power-loss models.
45. Construct a recoverable atomic-replacement protocol and test interruption after every step.
46. Compare metadata journaling, full data journaling, and copy-on-write snapshots for one multi-file application update. Identify what none guarantees.
47. Design a robust lock-file protocol, then explain why a kernel-supported exclusive open or advisory lock may be superior.
48. Trace a block read from process system call through page cache, filesystem, block layer, driver, DMA, interrupt, and completion.
49. Write a boot timeline from processor reset to one user-space Python process, identifying the trust and representation at every stage.

### 2.16.9 Integrated operating-system dossier

50. Specify a small protected multiprogramming system. Include privilege entry, process and thread records, scheduler, virtual-memory mapping, system-call validation, executable loading, filesystem objects, device driver, IPC, signals, termination, and recovery after power loss. Trace two adversarial processes attempting to read one another’s memory and files, and show exactly which hardware and kernel checks deny them.
