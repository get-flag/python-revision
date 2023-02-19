#!/bin/python

import argparse


parser = argparse.ArgumentParser(
	description = "The purpose",
	epilog = "Show how it can be used",
	)

parser.add_argument("-x", action="store", required= True, help="Description of X")
parser.add_argument("-y", help = "Description of y", default = False)
parser.add_argument("-z", help = "Description of z", required = False, type = int)

print(parser.parse_args())
