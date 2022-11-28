import sys


def main():
    if len(sys.argv) < 2:
        print("please using the command line as 'python cfm2vtk.py filename.ts'")
        exit(1)
    filename = sys.argv[1]
    fi = open(filename, "r")
    fn = filename.split(".")
    fo = open(str(fn[0])+".vtk", "w")

    fo.write("# vtk DataFile Version 1.0\n")
    fo.write("VTK file converted from GeoCAD .ts file\n")
    fo.write("ASCII\n")
    fo.write("\n")
    fo.write("DATASET UNSTRUCTURED_GRID\n")

    vrtx = list()
    trgl = list()
    while True:
        line = fi.readline()
        name = line.split(" ")[0]
        if (name == "VRTX"):
            vrtx.append(line)
        elif (name == "TRGL"):
            trgl.append(line)
        if not line:
            break
    vrtx_max = vrtx[-1].split()[1]
    fo.write("POINTS"+" "+vrtx_max+" "+"float\n")
    #print(" ".join(vrtx[-1].split()[2:]))
    for index in range(len(vrtx)):
        fo.write(" ".join(vrtx[index].split()[2:])+"\n")
    trgl_max = len(trgl)
    fo.write("CELLS"+" "+str(trgl_max)+" "+str(trgl_max*4)+"\n")
    for index in range(trgl_max):
        #fo.write("3"+"  "+"  ".join(trgl[index].split()[1:])+"\n")
        trgl_split = trgl[index].split()
        #In .vtk file, point index starts from 0
        #fo.write("3"+" "+trgl_split[1] +" " + trgl_split[2] +" "+trgl_split[3] +"\n")
        fo.write("3"+" "+ str(int(trgl_split[1])-1) +" " + str(int(trgl_split[2])-1) +" "+ str(int(trgl_split[3])-1) +"\n    ") 
    fo.write("CELL_TYPES"+" "+str(trgl_max)+"\n")
    for index in range(trgl_max):
        fo.write("5\n")
    fo.write("\n")
    fi.close()
    fo.close()


if __name__ == "__main__":
    main()
