# CrypticMachine (.cm)

An advanced, Turing-complete, low-level esoteric programming language (esolang) designed to mirror raw 8-bit microprocessor hardware layouts. CrypticMachine compiles directly down into high-performance standalone Windows executables (`.exe`) via an automated C-transpilation build pipeline.

---

## Installation Guide

CrypticMachine is distributed as a completely standalone, portable execution RELEASE via **GitHub Releases**. You do not need Python or GCC installed on your computer to deploy the environment.

1. Navigate to the **Releases** section on the right side of this GitHub repository page.
2. Download the latest compiled production binary: `cmInstaller.exe`.
3. Create a folder in your local hard drive called "cm"
4. Move `cmInstaller.exe` into a folder named `cm` on your local hard drive.
5. Open the executable

## Quick Start & CLI Toolchain

Once installed, you can open a terminal in **any directory or folder** on your computer and interact with your code using the global command engine keyword **`cm`**.

### Usage Syntax
```cmd
cm [FILE_NAME].cm [-o OUTPUT_NAME (optional)] [--run (optional)]
```

### Core CLI Flags
* **`--run`** *(Just-In-Time Mode)*: Transpiles and executes your `.cm` code immediately inside the active terminal window at hardware speed, wiping all temporary binaries automatically upon termination. No trash files are left behind.
* **`-o [Name]`** *(Compiler Mode)*: Compiles your low-level code directly into a permanent, distributable binary application asset (e.g., `cm main.cm -o MatrixApp` creates a standalone `MatrixApp.exe`).

---

## CrypticMachine Hardware Wiki

### 1. Hardware Architecture Logic
CrypticMachine bypasses standard software abstractions like variable labeling or dynamic array heaps. Instead, your programs interact directly with a singular processing layout:
* **The 8-bit Accumulator:** A singular, isolated hardware memory register holding a value between `0` and `255`.
* **The Virtual Screen Buffer:** A linear 256-byte cache tracking console output layout sequences.
* **The Program Counter (PC):** An internal address pointer reading bytecode instructions index-by-index sequentially.

### 2. Instruction Set Architecture (ISA)

| Instruction Token | Machine Opcode | Type | Execution Blueprint |
| :--- | :--- | :--- | :--- |
| **`©`** | `169` (`A9`) | 2-Byte | **Load Accumulator:** Copies the literal numeric byte pattern of the immediate trailing character directly into the internal register. |
| **`?`** | `63` (`3F`) | 2-Byte | **Conditional If Equal:** Compares the register against the trailing data byte character. If they are unequal, it increments the PC to jump clean past the next command sequence. |
| **`+`** | `43` (`2B`) | 2-Byte | **Arithmetic Add:** Adds the numeric ASCII integer value of the trailing character directly to the accumulator register value. |
| **`-`** | `45` (`2D`) | 2-Byte | **Arithmetic Subtract:** Subtracts the numeric ASCII integer value of the trailing character directly from the accumulator register value. |
| **`!`** | `33` (`21`) | 2-Byte | **Unconditional Jump:** Instantly teleports the Program Counter to target the absolute ROM array index position specified by the trailing character byte value. Used to build loop bounds. |
| **`<`** | `60` (`3C`) | 1-Byte | **Hardware Input:** Halts processing loops entirely until a keyboard byte strikes, copying the captured value into the register. |
| **`(10001101)`** | `141` (`8D`) | 1-Byte | **Store Output:** Flashes the character pattern held inside the accumulator directly onto the console window monitor screen layout, advancing the pointer index. |
| **`//0`** | `0` (`00`) | 1-Byte | **System Break:** Instantly shuts down processor cycles and cleanly halts execution parameters. |

---

## Code Blueprints & Examples

### Hello World
Because CM executes operations at raw clock-cycle logic levels, multi-character printing requires loading data, writing, and repeating the sequence sequentially for every letter (including spaces!):
```text
©H(10001101)©e(10001101)©l(10001101)©l(10001101)©o(10001101)© (10001101)©W(10001101)©o(10001101)©r(10001101)©l(10001101)©d(10001101)//0
```

### Conditional Branches (`If` Blocks)
**True Branch Conditions:**
```text
©A?A©Y(10001101)//0
```
*Loads `A`. Checks if the register equals `A`. Since the assertion is True, it steps forward normally, loading and executing the printer block to display **`Y`**.*

**False Branch Conditions (Skipping Operations):**
```text
©X?A©Y(10001101)//0
```
*Loads `X`. Checks if the register equals `A`. Since the assertion is False, it immediately jumps the PC index past the next command, executing the halt code and displaying absolutely nothing.*

### Interactive Live Terminal Feedback Loops (The Keyboard Echo)
This program spins an infinite low-level execution loop. It forces the CPU to pause, captures whatever physical character you strike on your keyboard, outputs it back to your active shell interface, and loops right back to step one infinitely:
```text
<!(10001101)!(00000000)
```
* `<` captures keyboard input.
* `!(10001101)` outputs the character.
* `!(00000000)` instantly teleports the program counter directly back to address slot `0` (the `<` input hook), overriding standard top-to-bottom compilation endings.
