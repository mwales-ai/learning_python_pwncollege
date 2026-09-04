#!/usr/bin/env python3

import sys, hashlib, binascii, subprocess, os

from typing import Dict, List, Tuple

def debug(msg:str):
    if(False):
        sys.stderr.write(msg + "\n")

def run_cmd(cmd: List[str], stdin_text:str ="", alt_user:str = None, timeout=None, cwd=None, env=None) -> Tuple[str, str, int]:
    """
    Run an external process, feed it text on stdin, block until it finishes,
    and return (stdout, stderr, returncode). Raises on timeout if specified.
    """

    if alt_user:
        run_cmd = ["runuser", "-u", alt_user]
        run_cmd.extend(cmd)

        # runas requires real user be set to root as well
        os.setuid(0)
    else:
        run_cmd = cmd

    try:
        cp = subprocess.run(
            run_cmd,                      # e.g. ["grep", "-n", "foo"]
            input=stdin_text,         # text to send to stdin
            capture_output=True,      # capture stdout and stderr
            text=True,                # use str instead of bytes
            timeout=timeout,          # optional: seconds
            cwd=cwd, env=env,         # optional: working dir / env
            check=False               # don't raise on nonzero exit
        )
        
        return cp.stdout, cp.stderr, cp.returncode
    except subprocess.TimeoutExpired as e:
        # e.stdout / e.stderr may contain partial output
        raise 

def read_in_file(path:str) -> list[ list[str] ]:
    ret_val = []
    with open(path, "r") as f:
        file_data = f.read().strip()
        for test_case in file_data.split("END_TEST_CASE"):
            test_case = test_case.strip()
            if test_case == "":
                break
            lines_of_tc = []
                
            for single_line in test_case.split("\n"):
                lines_of_tc.append(single_line.strip())
            ret_val.append(lines_of_tc)
    return ret_val

def convert_str_to_hash(text: str) -> str:
    verifyHash = hashlib.sha256()
    verifyHash.update(text.strip().encode("utf-8"))
    hash_str = verifyHash.digest().hex()
    return hash_str

def convert_strs_to_hashes(text: List[str]) -> List[str]:
    ret_val = []
    for single_line in text:
        if (single_line == ""):
            continue
        ret_val.append(convert_str_to_hash(single_line))
    return ret_val
   
def execute_tc(test_data: List[str], hash_file, solution_script:str) -> bool:
    print(f"Going to execute your script {solution_script} with the following input:")
    print(test_data)

    tc_out, tc_err, tc_code = run_cmd([solution_script], "\n".join(test_data))
    hashes_out = convert_strs_to_hashes(tc_out.split("\n"))

    print("Your programs output:")
    print(tc_out)

    print("Hashes:")
    print(hashes_out)

    if tc_err:
        print("Your programs stderr (ignored):")
        print(tc_err)

    for single_line in hashes_out:
        hash_file.write(single_line + "\n")

    hash_file.write("END_TEST_CASE\n")
    return True

def main(argv):
    if len(argv) != 4:
        print("Creates hashes.txt file needed for evaluation script!")
        print("")
        print(" Arg 1: script.py (script that will generate desired output")
        print(" Arg 2: test_cases.txt  (test cases delimited by END_TEST_CASE")
        print(" Arg 3: path/to/hashes.txt (output file we will generate)")
        return

    good_script = argv[1]
    test_case_path = argv[2]
    hash_output_path = argv[3]

    #verify_hashes = read_in_file("/challenge/.eval_data/hashes.txt")
    test_data = read_in_file(test_case_path)

    hash_file = open(hash_output_path, "w")

    for tc_text in test_data:
        print("Starting test case")
        if not execute_tc(tc_text, hash_file, good_script):
            sys.exit()

    print("Done writing hashes")
    hash_file.close()

if __name__ == "__main__":
    main(sys.argv)
