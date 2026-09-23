# 1.12 Common misconceptions consolidated

1. **“Binary values exist because electricity is either on or off.”** Electricity varies continuously. Circuits define tolerant ranges and use restoration to obtain dependable logical distinctions.
2. **“The bit pattern determines its own meaning.”** Meaning comes from an interpretation contract. The same pattern may be an integer, character fragment, instruction, address, or arbitrary data.
3. **“A clock cycle equals one instruction.”** Cycles coordinate circuit state. Instructions may span cycles, overlap, or complete at varying rates.
4. **“The von Neumann model is a photograph of every modern processor.”** It is an architectural abstraction. Caches, pipelines, multiple cores, and separate internal paths refine its implementation.
5. **“Memory addresses are the values stored there.”** An address designates a location; content is the current pattern at that location.
6. **“A successful output proves the machine or program is correct.”** One observation establishes only that one execution produced that output under one state. Correctness requires a specification and an argument covering the admitted inputs.
7. **“Higher-level software escapes physics.”** Software relies on lower layers, but stable abstraction contracts make most physical details irrelevant to a particular reasoning task.
