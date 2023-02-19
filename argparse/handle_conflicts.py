import argparse

parser = argparse.ArgumentParser(
	description="What is done?",
	epilog="How it is done, example?",
)


#create a group for conflicting options

group = parser.add_mutually_exclusive_group()

group.add_argument("-y", action="store")
group.add_argument("-n", action="store")

parser.add_argument("-z",action="store")

#example usage python $0 -y yes -n no -z 4
#o/p: error: argument -n: not allowed with argument -y
print(parser.parse_args())
