# Ariana Borlak
# python3 passwords.py

import hashlib
import binascii
import signal
import sys

def compute_hashes_1():
	hash_dict = {}
	hash_count = 0

	words = [line.strip().lower() for line in open('words.txt')]
	for word in words:
		password = word # type=string

		encoded_password = password.encode('utf-8') # type=bytes

		hasher = hashlib.sha256(encoded_password)
		digest = hasher.digest() # type=bytes

		digest_as_hex = binascii.hexlify(digest) # type=bytes

		digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string

		hash_dict[digest_as_hex_string] = word
		hash_count += 1
	return hash_dict, hash_count


def crack_pwds_1(hashes):
	first = open("cracked1.txt", 'w')
	pwd_count = 0

	rows = [line.split(":") for line in open('passwords1.txt')]

	for row in rows:
		pwd_hash = row[1]
		if pwd_hash in hashes: #if the password hash is in hashes
			first.write(f"{row[0]}:{hashes[pwd_hash]}\n")
			pwd_count += 1
	first.close()
	return pwd_count


def compute_hashes_2():
	pwd_dict = {}
	pwd_count = 0

	global hashcount
	hashcount = 0

	for line in open('passwords2.txt'):
		split_line = line.split(":")
		pwd_dict[split_line[1]] = split_line[0]

	words = [line.strip().lower() for line in open('words.txt')]

	second = open("cracked2.txt", 'w')
	for word in words:
		for next in words:
			password = word + next # type=string

			encoded_password = password.encode('utf-8') # type=bytes
			hasher = hashlib.sha256(encoded_password)
			digest = hasher.digest() # type=bytes
			digest_as_hex = binascii.hexlify(digest) # type=bytes
			digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string

			if digest_as_hex_string in pwd_dict:
				second.write(f"{pwd_dict[digest_as_hex_string]}:{password}\n")
				pwd_count += 1

			hashcount += 1
	second.close()
	return hashcount, pwd_count

def compute_hashes_3():
	pwd_dict = {}
	pwd_count = 0

	global hashcount
	hashcount = 0

	for line in open('passwords3.txt'):
		split_line = line.split(":")
		pwd_dict[split_line[1]] = split_line[0]

	words = [line.strip().lower() for line in open('words.txt')]

	second = open("cracked3.txt", 'w')
	for word in words:
		for next in words:
			password = word + next # type=string

			encoded_password = password.encode('utf-8') # type=bytes
			hasher = hashlib.sha256(encoded_password)
			digest = hasher.digest() # type=bytes
			digest_as_hex = binascii.hexlify(digest) # type=bytes
			digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string

			if digest_as_hex_string in pwd_dict:
				second.write(f"{pwd_dict[digest_as_hex_string]}:{password}\n")
				pwd_count += 1

			hashcount += 1
	second.close()
	return hashcount, pwd_count

def signal_handler(sig, frame):
	print(f"Number of hashes computed: {hashcount}")
	sys.exit(0)


def main():
	signal.signal(signal.SIGINT, signal_handler)

	# PART 1 code:
	hashes, num_hashes = compute_hashes_1()
	num_pwds = crack_pwds_1(hashes)
	print(f"Hashes computed: {num_hashes}\nNumber of cracked passwords: {num_pwds}")

	# PART 2 code:
	# num_hashes, num_pwds = compute_hashes_2()
	# print(f"Hashes computed: {num_hashes}\nNumber of cracked passwords: {num_pwds}")

	# PART 3 code:




if __name__ == "__main__":
	main()