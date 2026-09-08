#!/usr/bin/env python3
"""
Run a golden script over a challenge's test cases and write the hash files the
judge compares against.

  gen_hashes.py <golden_script> <test_cases.txt> <hashes.txt> [options]

    --args FILE            command line arguments per case, END_TEST_CASE
                           delimited, one argument per line
    --stderr-hashes FILE   also hash stderr, so the judge checks it
    --exit-codes FILE      also record exit status, so the judge checks it

Only stdout is judged unless you ask for more.  Whatever you generate here,
the judge's .eval_data must contain the same set of files, with the same
number of test cases in each.
"""

import sys, hashlib, subprocess, os

from typing import List, Tuple

# Golden scripts should be fast; a hang here means the script is broken.
TEST_CASE_TIMEOUT = 10

def debug(msg:str):
    if(False):
        sys.stderr.write(msg + "\n")

def run_cmd(cmd: List[str], stdin_text:str ="", alt_user:str = None, timeout=None, cwd=None, env=None) -> Tuple[str, str, int]:
    """
    Run an external process, feed it text on stdin, block until it finishes,
    and return (stdout, stderr, returncode). Raises on timeout if specified.
    """

    if alt_user:
        run_cmd = ["runuser", "-u", alt_user, "--"]
        run_cmd.extend(cmd)
        os.setuid(0)
    else:
        run_cmd = cmd

    try:
        cp = subprocess.run(
            run_cmd,
            input=stdin_text,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=cwd, env=env,
            check=False
        )
        return cp.stdout, cp.stderr, cp.returncode
    except subprocess.TimeoutExpired as e:
        raise

def read_in_file(path:str) -> list[ list[str] ]:
    """
    END_TEST_CASE is a TERMINATOR, not a separator: a section with no lines in
    it is a real test case, meaning "this program reads nothing from stdin".
    Only the trailing text after the final terminator is discarded.  This must
    match read_in_file() in the judge `run` script exactly.
    """
    ret_val = []
    with open(path, "r") as f:
        file_data = f.read()

    for section in file_data.split("END_TEST_CASE")[:-1]:
        lines_of_tc = []
        for single_line in section.split("\n"):
            single_line = single_line.strip()
            if single_line != "":
                lines_of_tc.append(single_line)
        ret_val.append(lines_of_tc)
    return ret_val

def convert_str_to_hash(text: str) -> str:
    verifyHash = hashlib.sha256()
    verifyHash.update(text.strip().encode("utf-8"))
    return verifyHash.digest().hex()

def clean_output_lines(text: str) -> List[str]:
    """
    Split program output into the lines we actually judge: stripped, with
    blank lines dropped.  This MUST match clean_output_lines() in the judge
    `run` script or the generated hashes will not line up.
    """
    ret_val = []
    for single_line in text.split("\n"):
        single_line = single_line.strip()
        if single_line == "":
            continue
        ret_val.append(single_line)
    return ret_val

def convert_strs_to_hashes(text: List[str]) -> List[str]:
    ret_val = []
    for single_line in text:
        if (single_line.strip() == ""):
            continue
        ret_val.append(convert_str_to_hash(single_line))
    return ret_val

def parse_args(argv):
    opts = {"args": None, "stderr": None, "exit": None}
    positional = []
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--args":            opts["args"]   = argv[i+1]; i += 2
        elif a == "--stderr-hashes": opts["stderr"] = argv[i+1]; i += 2
        elif a == "--exit-codes":    opts["exit"]   = argv[i+1]; i += 2
        elif a.startswith("--"):
            print(f"unknown option {a}", file=sys.stderr); sys.exit(2)
        else:
            positional.append(a); i += 1
    return opts, positional

def main(argv):
    opts, positional = parse_args(argv)
    if len(positional) != 3:
        print(__doc__.strip(), file=sys.stderr)
        return 1

    good_script, test_case_path, hash_output_path = positional

    test_data = read_in_file(test_case_path)
    arg_data = read_in_file(opts["args"]) if opts["args"] else None

    if arg_data is not None and len(arg_data) != len(test_data):
        print(f"args file has {len(arg_data)} cases but test_cases has "
              f"{len(test_data)}", file=sys.stderr)
        return 1

    out_hashes, err_hashes, codes = [], [], []

    for i, tc_text in enumerate(test_data):
        args = arg_data[i] if arg_data is not None else []
        cmd = [good_script] + list(args)
        print(f"Starting test case {i+1}: {' '.join(cmd)}")

        try:
            tc_out, tc_err, tc_code = run_cmd(cmd, "\n".join(tc_text),
                                              timeout=TEST_CASE_TIMEOUT)
        except subprocess.TimeoutExpired:
            print(f"!! Golden script timed out after {TEST_CASE_TIMEOUT}s "
                  f"- refusing to write hashes", file=sys.stderr)
            return 1

        out_lines = clean_output_lines(tc_out)
        err_lines = clean_output_lines(tc_err)

        print("Golden script stdout:")
        print(tc_out)
        if tc_err:
            label = "stderr" if opts["stderr"] else "stderr (ignored by the judge)"
            print(f"Golden script {label}:")
            print(tc_err)
        print(f"Exit status: {tc_code}")

        # A golden script that crashed would silently bake an empty or partial
        # expected output into the hashes, making the challenge unsolvable.
        # An expected nonzero exit is legitimate, but only if we were asked to
        # record exit codes on purpose.
        if tc_code != 0 and opts["exit"] is None:
            print(f"!! Golden script exited {tc_code} and --exit-codes was not "
                  f"given - refusing to write hashes", file=sys.stderr)
            return 1

        if len(out_lines) == 0 and opts["stderr"] is None:
            print("!! Golden script produced no stdout - refusing to write "
                  "hashes", file=sys.stderr)
            return 1

        out_hashes.append(convert_strs_to_hashes(out_lines))
        err_hashes.append(convert_strs_to_hashes(err_lines))
        codes.append(tc_code)

    def write_sections(path, sections):
        with open(path, "w") as f:
            for section in sections:
                for h in section:
                    f.write(h + "\n")
                f.write("END_TEST_CASE\n")

    write_sections(hash_output_path, out_hashes)
    if opts["stderr"]:
        write_sections(opts["stderr"], err_hashes)
    if opts["exit"]:
        with open(opts["exit"], "w") as f:
            for c in codes:
                f.write(f"{c}\n")

    print(f"Done writing {len(test_data)} test cases of hashes")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
