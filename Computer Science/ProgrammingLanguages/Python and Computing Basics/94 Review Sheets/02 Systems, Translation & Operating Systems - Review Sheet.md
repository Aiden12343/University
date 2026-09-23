# 2.15 Common misconceptions consolidated

1. **“A programming language is either compiled or interpreted.”** Implementations can compile source to an intermediate form, interpret that form, and JIT-compile hot paths in one execution system.
2. **“Assembly and machine code are the same representation.”** Assembly is symbolic source; an assembler encodes it.
3. **“A compiler translates one source line into one instruction.”** Source constructs and machine operations have no universal one-to-one relation.
4. **“An operating system is the windows and icons.”** A graphical interface is an application or service layer. The OS includes kernel mechanisms governing processors, memory, devices, processes, and persistent names.
5. **“A program and a process are synonyms.”** A program can be a passive executable representation; a process is a live protected execution environment.
6. **“Every file operation reaches a disk immediately.”** Runtime and kernel caches, device queues, and asynchronous completion separate program-level requests from physical persistence.
7. **“One virtual address identifies one physical cell globally.”** Translation is contextual; different processes can map the same virtual number differently.
8. **“Kernel mode means trusted code is correct.”** Privilege grants authority. It increases the consequences of defects and therefore demands stronger validation.
