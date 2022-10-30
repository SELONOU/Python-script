with open("output_lines.txt","w") as output:
    with open("file_input.txt") as lines:
        for line in lines:
            if "methane" in line:
                df=line.replace("\n","")
                output.write(df+"\n")



