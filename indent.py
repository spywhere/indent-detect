import sys
import re
import os


def find_gcd(num1, num2):
    if num2 == 0:
        return num1
    return find_gcd(num2, num1 % num2)


def run(args):
    if len(args) < 2:
        print("No input file.")
        return
    input_file_path = args[1]
    if not os.path.exists(input_file_path):
        print("File is not exists.")
        return
    input_file = open(input_file_path, "r")
    lines = input_file.readlines()
    input_file.close()
    
    use_tab = 0
    sizes = []
    sample_size = 0
    for line in lines:
        if sample_size > 500:
            break
        
        matches = re.match("^([ \t]+)", line)
        if not matches:
            continue
        if matches.group(1).startswith("\t"):
            use_tab += 1
        sizes.append(len(matches.group(1)))
        
        sample_size += 1
    
    print("File: %s" % (os.path.basename(input_file_path)))
    print("Sizes: [%s]" % (", ".join([str(size) for size in sizes])))
    
    if len(sizes) <= 1:
        return
    gcds = []
    index1 = 0
    while index1 < len(sizes):
        index2 = index1 + 1
        while index2 < len(sizes):
            gcd_size = find_gcd(sizes[index1], sizes[index2])
            gcds.append(gcd_size)
            index2 += 1
        index1 += 1 
    gcd_count = {}
    for gcd in gcds:
        if str(gcd) in gcd_count:
            gcd_count[str(gcd)] += 1
        else:
            gcd_count[str(gcd)] = 1
    
    max_key = None
    max_value = -1
    print("GCDs:")
    for key, value in gcd_count.items():
        if max_key is None or max_value <= value:
            if max_key is None or max_value < value or int(key) < int(max_key):
                max_key = key
            max_value = value
        print("    %s: %s" % (key, value))
    print("Use tab: %s [%s/%s]" % (
        "Yes" if (use_tab / sample_size) > 0.5 else "No",
        use_tab,
        sample_size
    ))
    print("Final Size: %s" % (max_key))


if __name__ == "__main__":
    run(sys.argv)