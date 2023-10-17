# Project 4: Simulation of Directory-based Cache Coherence: Programming Project

## Assumptions
1. ADD would only have numberic values (no memory locations)
2. If invalid instruction we just move on (like everyone does enentually)
3. State is stored in the cache as well.
4. If a core requests a modified value, it's own cache will save it as shared but only if it is not the modfier core itself.
5. If invalid in directory, pull from memory and set the state shared.