import argparse

parser = argparse.ArgumentParser(
	description = "test short and long options",
	epilog = "This field for example",
)

parser.add_argument("-x", "--long_option", help="Long option example")

print(parser.parse_args())



#usage: python <program_name> -x
#usage2: python <program_name> --long_option
