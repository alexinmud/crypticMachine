import re
import sys
import os
import subprocess

def parse_cryptic_machine(source_code):
    binary_stream = []
    tokens = re.findall(r'//0|\([^)]+\)|.', source_code)
    for token in tokens:
        if token == "//0":
            binary_stream.append("00000000")
        elif token.startswith("(") and token.endswith(")"):
            binary_stream.append(token[1:-1])
        else:
            binary_stream.append(format(ord(token), '08b'))
    return binary_stream

def generate_native_c_code(binary_bytes):
    byte_values = []
    for b in binary_bytes:
        try:
            byte_values.append(str(int(b, 2)))
        except ValueError:
            byte_values.append("0")
            
    bytes_array_str = ", ".join(byte_values)
    array_size = len(byte_values)

    c_source = f"""#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {{
    unsigned char rom[{array_size}] = {{ {bytes_array_str} }};
    unsigned char accumulator = 0;
    char virtual_screen = {{0}}; 
    int screen_index = 0;
    int pc = 0;
    int limit = {array_size};

    while (pc < limit) {{
        unsigned char current_byte = rom[pc];
        
        if (current_byte == 169) {{
            if (pc + 1 < limit) {{
                accumulator = rom[pc + 1];
                pc += 2;
            }} else {{
                break;
            }}
        }}
        else if (current_byte == 63) {{
            if (pc + 1 < limit) {{
                unsigned char compare_val = rom[pc + 1];
                pc += 2;
                if (accumulator != compare_val) {{
                    if (pc < limit) {{
                        unsigned char next_op = rom[pc];
                        if (next_op == 169 || next_op == 63 || next_op == 43 || next_op == 45 || next_op == 33) {{
                            pc += 2;
                        }} else {{
                            pc += 1;
                        }}
                    }}
                }}
            }} else {{
                break;
            }}
        }}
        else if (current_byte == 43) {{
            if (pc + 1 < limit) {{
                accumulator += rom[pc + 1];
                pc += 2;
            }} else {{
                break;
            }}
        }}
        else if (current_byte == 45) {{
            if (pc + 1 < limit) {{
                accumulator -= rom[pc + 1];
                pc += 2;
            }} else {{
                break;
            }}
        }}
        else if (current_byte == 33) {{
            if (pc + 1 < limit) {{
                int target_slot = (int)rom[pc + 1];
                if (target_slot >= 0 && target_slot < limit) {{
                    pc = target_slot;
                }} else {{
                    break;
                }}
            }} else {{
                break;
            }}
        }}
        else if (current_byte == 60) {{
            accumulator = (unsigned char)fgetc(stdin);
            pc += 1;
        }}
        else if (current_byte == 141) {{
            if (screen_index < 256) {{
                virtual_screen[screen_index] = (char)accumulator;
                printf("%c", virtual_screen[screen_index]);
                screen_index++;
            }}
            pc += 1;
        }}
        else if (current_byte == 0) {{
            return 0;
        }}
        else {{
            pc += 1;
        }}
    }}
    return 0;
}}
"""
    return c_source

def main():
    args = sys.argv[1:]
    if not args:
        print("Error: Missing input file.")
        print("Usage: cm [FILE_NAME].cm [-o OUTPUT_NAME] [--run]")
        sys.exit(1)
        
    should_run = False
    if args and args[-1] == '--run':
        should_run = True
        args = args[:-1]
        
    input_filename = None
    output_name = None
    
    i = 0
    while i < len(args):
        if args[i] == '-o':
            if i + 1 < len(args):
                output_name = args[i + 1]
                i += 2
            else:
                print("Error: -o flag requires an output name string.")
                sys.exit(1)
        else:
            if input_filename is None:
                input_filename = args[i]
            i += 1

    if not input_filename:
        print("Error: No input .cm file specified.")
        sys.exit(1)
    if not input_filename.endswith('.cm'):
        print(f"Error: {input_filename} must end in .cm")
        sys.exit(1)
    if not os.path.exists(input_filename):
        print(f"Error: {input_filename} not found.")
        sys.exit(1)
        
    if should_run:
        exe_filename = os.path.abspath(input_filename.replace('.cm', '_run_temp.exe'))
    else:
        if output_name:
            exe_filename = output_name if output_name.lower().endswith('.exe') else output_name + '.exe'
            exe_filename = os.path.abspath(exe_filename)
        else:
            exe_filename = os.path.abspath(input_filename.replace('.cm', '.exe'))
        
    with open(input_filename, 'r', encoding='utf-8') as f:
        source_code = f.read()
        
    if not should_run:
        print(f"Compiling {input_filename}...")
    
    binary_bytes = parse_cryptic_machine(source_code)
    c_code = generate_native_c_code(binary_bytes)
    
    c_filename = os.path.abspath(input_filename.replace('.cm', '_temp.c'))
    with open(c_filename, 'w', encoding='utf-8') as f:
        f.write(c_code)
    
    compilation_success = False
    try:
        subprocess.run(["gcc", c_filename, "-o", exe_filename], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        compilation_success = True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("\nError: Compilation failed. Ensure GCC is working correctly.")
    finally:
        if os.path.exists(c_filename):
            os.remove(c_filename)
        
    if compilation_success:
        if should_run:
            run_cmd = f'"{exe_filename}"'
            subprocess.run(run_cmd, shell=True)
            if os.path.exists(exe_filename):
                os.remove(exe_filename)
        else:
            print(f"Compiled {input_filename}")

if __name__ == '__main__':
    main()
