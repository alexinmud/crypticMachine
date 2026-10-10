# CrypticMachine (.cm)

An advanced, un-sandboxed, 64-bit esoteric programming language (esolang) that bridges the gap between readable text tokens and direct hardware manipulation. CrypticMachine compiles directly down into high-performance standalone Windows executables (`.exe`) by injecting raw x86_64 inline assembly (`__asm__`) instructions and operating system level abstractions directly into physical CPU registers and host RAM layouts.

---

## Installation Guide

CrypticMachine is distributed as a completely standalone, portable execution RELEASE via **GitHub Releases**. You do not need Python or GCC installed on your computer to deploy the environment.

1. Navigate to the **Releases** section on the right side of this GitHub repository page.
2. Download the latest compiled production binary: `cmInstaller.exe`.
3. Create a folder in your local hard drive root named `cm` (e.g., `C:\cm`).
4. Move `cmInstaller.exe` into that folder.
5. Open the executable. The installer automatically deploys required host components, structures system directories, and configures your global environmental path mappings.

---

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
CrypticMachine bypasses standard software abstractions like variable labeling or dynamic array heaps. Instead, your programs interact directly with your physical computer chip:
* **The RAX Register:** The primary 64-bit hardware accumulator inside your physical CPU chip.
* **The RBX Register:** The secondary 64-bit hardware data register inside your physical CPU chip.
* **The RAM Pool Memory Chunk:** A continuous 1MB un-sandboxed array slice allocated directly inside your computer's physical RAM sticks.

### 2. Instruction Set Architecture (ISA)

| Instruction Token | Machine Opcode | Type | Execution Blueprint |
| :--- | :--- | :--- | :--- |
| **`©`** | `169` (`A9`) | 2-Byte | **Load RAX Register:** Copies the literal numeric byte pattern of the trailing character directly into the physical CPU's 64-bit `RAX` hardware register. |
| **`®`** | `162` (`A2`) | 2-Byte | **Load RBX Register:** Copies the literal numeric byte pattern of the trailing character directly into the physical CPU's 64-bit `RBX` hardware register. |
| **`+`** | `43` (`2B`) | 1-Byte | **Inline Hardware Add:** Forces the CPU's Arithmetic Logic Unit (ALU) to perform an inline assembly operation, merging the contents of the registers (`reg_rax += reg_rbx`). |
| **`[`** | `91` (`5B`) | 1-Byte | **Direct RAM Pointer Write:** Executes an inline pointer store command (`movb %%bl, (%%rax)`). This physically writes the character byte held in RBX directly to the raw RAM memory address stored in RAX. |
| **`]`** | `93` (`5D`) | 1-Byte | **Direct RAM Pointer Read:** Executes an inline pointer load command (`movzbq (%%rax), %%rax`). This commands the CPU to peek into the raw RAM memory address stored in RAX and read its data back into the processor. |
| **`?`** | `63` (`3F`) | 2-Byte | **Fixed-Width Hardware Branch:** Compares the active register against the trailing data byte character. If they are unequal, it forces the hardware program counter pointer to skip exactly 10 bytes forward to bypass adjacent victory operations. |
| **`!`** | `33` (`21`) | 2-Byte | **Unconditional Jump:** Instantly teleports the internal Program Counter address pointer directly to the absolute ROM instruction array slot index specified by the trailing character byte value. Used to build loop bounds. |
| **`<`** | `60` (`3C`) | 1-Byte | **Direct Echoed Keyboard Input:** Pauses processing loops completely, holding hardware threads until an immediate, unbuffered keyboard byte strikes, copying the captured value into RAX and echoing it onto the screen. Includes key release protection. |
| **`#`** | `35` (`23`) | 1-Byte | **Hardware Terminal Color:** Controls console colors by passing the register value straight to the Windows console host attribute manager (`SetConsoleTextAttribute`). |
| **`*`** | `42` (`2A`) | 1-Byte | **Motherboard Audio Beep:** Hardwires directly to the audio layer to play a sound at a frequency pitch determined by the `RAX` register value. |
| **`(10001101)`** | `141` (`8D`) | 1-Byte | **Store Console Output:** Grabs the lowest active byte sector from the RAX register layout and flushes its character pattern directly onto the terminal screen. |
| **`//0`** | `0` (`00`) | 1-Byte | **System Break:** Frees allocated virtual system RAM pools, shuts down active CPU processing pipelines, and exits back to shell parameters cleanly. |

---

## Code Blueprints & Examples

### Hello World
Because CM executes operations at raw register logic levels, printing text requires streaming individual bytes—loading data, writing, and repeating the sequence sequentially for every letter (including spaces!):
```text
©H(10001101)©e(10001101)©l(10001101)©l(10001101)©o(10001101)© (10001101)©W(10001101)©o(10001101)©r(10001101)©l(10001101)©d(10001101)//0
```

### Direct RAM Allocation, Storage, and Recovery
This advanced blueprint loads the RAM pool pointer address into the `RAX` hardware register, writes a character into the `RBX` register, burns it straight into a raw physical memory cell inside your computer's RAM sticks, reads it back, and prints it natively:
```text
©®X[](10001101)//0
```
* `©` points RAX to your base RAM memory cells.
* `®X` loads the text character `X` into RBX.
* `[` writes `X` straight to your system memory stick.
* `]` peeks inside that memory cell location to reload RAX.
* `(10001101)` prints out the final recovered data.

### Matrix Musical Guessing Game
This production script sets up an interactive musical puzzle application. It initializes a glowing green layout, waits for an unbuffered keypress to play a hardware tone, evaluates conditions, and branches dynamically. Wrong guesses flash a crimson error screen before jumping exactly back to the keyboard hook, while the secret trigger key (`A`) triggers an ascending multi-note victory scale:
```text
© #©g(10001101)©u(10001101)©e(10001101)©s(10001101)©s(10001101)©:(10001101)© (10001101)<?A©À*©È*©ð*//0© #©W(10001101)©R(10001101)©O(10001101)©N(10001101)©G(10001101)©!(00000014)
```
* `© #` flips terminal foreground text colors to Matrix Green.
* `<?A` traps a live hardware keypress, echoes it, and drops a fixed branch conditional evaluation.
* `©À*©È*©ð*//0` rings out an ascending 3-pitch victory chime sequence and halts on matching inputs.
* `© #` alters console screen outputs to Crimson Red when input values fail assertions.
* `!(00000014)` loops the hardware instruction register pointer exactly back to index position 14 (the `<` key capture hook) to continue game execution seamlessly.
