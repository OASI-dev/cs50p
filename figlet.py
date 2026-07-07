import sys
import pyfiglet

if len(sys.argv) != 3 or sys.argv[1] != "-f":
    sys.exit("Invalid usage")

font = sys.argv[2]

try:
    figlet = pyfiglet.Figlet(font=font)
except pyfiglet.FontNotFound:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))