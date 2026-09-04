#!/usr/bin/env python3

'''
Pass this the script the desired output from a challenge.  Run this script
in a directoy that has flag.txt.  The script will hash the desired user
output into 2 hashes.  One of the hashes we use later in a judge script to
verify the output is correct, the other hash is used to encrypt the flag.
This script then creates a judge.py script that the user can run to check
their output, if their output is correct, they get the decrypted flag.
'''

import sys, hashlib, binascii, base64

def debug(msg):
	if(True):
		sys.stderr.write(msg + "\n")

# This is the judge_template.py base64 encoded so this script can be run anywhere
CODE_JUDGE_TEMPLATE = """
IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoKaW1wb3J0IHN5cywgaGFzaGxpYiwgYmluYXNjaWkKClZF
UklGWV9IQVNIRVMgPSAxMzM3X1ZFUklGWV9IQVNIXzEzMzcKCmRlZiBkZWJ1Zyhtc2c6c3RyKToK
CWlmKEZhbHNlKToKCQlzeXMuc3RkZXJyLndyaXRlKG1zZyArICJcbiIpCgpkZWYgY2xlYW5MaW5l
RW5kaW5ncyh0ZXh0OiBzdHIpIC0+IGxpc3Rbc3RyXToKCWNsZWFuT3V0cHV0ID0gW10KCXRleHRM
aW5lcyA9IHRleHQuc3BsaXQoIlxuIikKCWZvciBzaW5nbGVMaW5lIGluIHRleHRMaW5lczoKCQlj
bGVhbk91dHB1dC5hcHBlbmQoc2luZ2xlTGluZS5zdHJpcCgpKQoJcmV0dXJuIGNsZWFuT3V0cHV0
CgpkZWYgY3JlYXRlVmVyaWZ5SGFzaGVzKHRleHQ6IGxpc3Rbc3RyXSkgLT4gbGlzdFtieXRlc106
CglyZXRWYWwgPSBbXQoJZm9yIHNpbmdsZUxpbmUgaW4gdGV4dDoKCgkJdmVyaWZ5SGFzaCA9IGhh
c2hsaWIuc2hhMjU2KCkKCQl2ZXJpZnlIYXNoLnVwZGF0ZShzaW5nbGVMaW5lLmVuY29kZSgidXRm
LTgiKSkKCQlyZXRWYWwuYXBwZW5kKHZlcmlmeUhhc2guZGlnZXN0KCkpCgoJcmV0dXJuIHJldFZh
bAoKZGVmIG1haW4oYXJncyk6CglyYXdPdXRwdXQgPSBzeXMuc3RkaW4ucmVhZCgpLnN0cmlwKCkK
CgljbGVhbk91dHB1dCA9IGNsZWFuTGluZUVuZGluZ3MocmF3T3V0cHV0KQoJCgl2ZXJpZnlIYXNo
ZXMgPSBjcmVhdGVWZXJpZnlIYXNoZXMoY2xlYW5PdXRwdXQpCgoJZm9yIChpLCBsKSBpbiBlbnVt
ZXJhdGUoY2xlYW5PdXRwdXQpOgoJCWlmIChpID49IGxlbihWRVJJRllfSEFTSEVTKSApOgoJCQlw
cmludCgiWW91IGhhdmUgZXh0cmEgbGluZXMgb2Ygb3V0cHV0ISIpCgkJCXJldHVybgoKCQlpZiAo
VkVSSUZZX0hBU0hFU1tpXSAhPSBiaW5hc2NpaS5oZXhsaWZ5KHZlcmlmeUhhc2hlc1tpXSkpOgoJ
CQlwcmludCgiT3V0cHV0IGluY29ycmVjdCIpCgkJCXByaW50KGYiTGluZSB7aSsxfToge2x9IikK
CQkJcmV0dXJuCgkJCQoJaWYgKGxlbihjbGVhbk91dHB1dCkgIT0gbGVuKFZFUklGWV9IQVNIRVMp
KToKCQlwcmludCgiTWlzc2luZyBsaW5lcyBvZiBvdXRwdXQiKQoJCXJldHVybgoKCSMgRGlzcGxh
eSB0aGUgZmxhZwoJZmxhZyA9IG9wZW4oIi9mbGFnIiwiciIpLnJlYWQoKQoJCglwcmludCgiQ29u
Z3JhdHMhIikKCXByaW50KGZsYWcpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgoJbWFpbihz
eXMuYXJndikK
"""

def cleanLineEndings(text: str) -> list[str]:
	cleanOutput = []
	textLines = text.split("\n")
	for singleLine in textLines:
		cleanOutput.append(singleLine.strip())
	return cleanOutput

def createVerifyHashes(text: list[str]) -> list[bytes]:
	retVal = []
	for singleLine in text:

		verifyHash = hashlib.sha256()
		verifyHash.update(singleLine.encode("utf-8"))
		retVal.append(verifyHash.digest())
		
		# debug(f"  Line with hash {verifyHash.digest()} is {singleLine}")

	return retVal
	
def convertHashListIntoHexList(hashList: list[bytes]) -> str:
	retVal = '[   b"'
	hashHexList = []
	for h in hashList:
		hashHexList.append(binascii.hexlify(h).decode("utf-8"))
	
	retVal += '", \n   b"'.join(hashHexList)
	retVal += '" ]\n'
	return retVal

def xorByteArray(a, b):
	# This bit of cleverness from stackoverflow post
	# https://stackoverflow.com/questions/52851023/python-3-xor-bytearrays
	retVal = (bytes(x ^ y for (x,y) in zip(a,b)))
	return retVal

def getJudgeTemplate():
	jtraw = base64.b64decode(CODE_JUDGE_TEMPLATE)
	return jtraw.decode("utf-8")

def main(args):
	rawOutput = sys.stdin.read().strip()

	cleanOutput = cleanLineEndings(rawOutput)
	
	verifyHashes = createVerifyHashes(cleanOutput)
	debug("Verify Hash  = {}".format(convertHashListIntoHexList(verifyHashes)))
	
	judgeText = getJudgeTemplate()
	judgeText = judgeText.replace("1337_VERIFY_HASH_1337", convertHashListIntoHexList(verifyHashes))
	print(judgeText)

	sys.stderr.write("Judge Script Output Complete\n")



if __name__ == "__main__":
	main(sys.argv)
