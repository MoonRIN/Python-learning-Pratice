def main():
    copySource = input("请输入源文件:").strip()
    copyDirect = input("请输入目标文件").strip()

    infile = open(copySource, "rb")
    outfile = open(coopyDirect, "wb")

    contLines = contChars = 0
    for line in infile:
     contLines += 1
     contChars += len(line)
     outfile.write(line)
    print("Copy finished", "Total copied", contLines, "line(s)", "and", contChars, "Chars")

    infile.close()
    outfile.close()

main()
