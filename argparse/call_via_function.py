import argparse


def get_argparse():
	parser = argparse.ArgumentParser(
		description="A simple argument parser",
		epilog="This just tells how to use, upon using -h option",
	)
	return parser.parse_args()

if __name__=="__main__":
	get_argparse()

