import PyPDF2, sys, getopt, os
from PDFActions import PDF

def showHelp():
    print (sys.argv[0] + "-i <inputfile> -o <outputfile> -r <rotation steps clockwise> --merge/-m")
    sys.exit(0)

def main(argv):
    inputfiles = []
    outputfiles = []
    mode = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:r:m", ["help","input=", "output=", "rotation=", "merge"])
    except getopt.GetoptError:
        print ("Please use " + sys.argv[0] + " -i <inputfile> -o <outputfile>")
        sys.exit(1)
    for arg in args:
        arg = arg.replace(' ', '')
    for opt, arg in opts:
        if opt in  ('-h', '--help'):
            showHelp()
        elif opt in ('-i', '--input'):
            inputfiles = arg.split(',')
        elif opt in ('-o', '--output'):
            outputfiles = arg.split(',')
        elif opt in ('-r', '--rotation'):
            rotation = int(arg)
            mode = 'rotate'
        elif opt in ('-m', '--merge'):
            mode = 'merge'
        
    #test if inputfile exists
    for inputfile in inputfiles:
        if not os.path.exists(inputfile):
            print('File ' + inputfile +' does not exist')
            sys.exit(1)
    for outputfile in outputfiles:
        if os.path.exists(outputfile):
            print('File ' + outputfile +' already exist')
            sys.exit(1)
    if mode == 'rotate':
        if not rotation <= 0:
            steps = rotation*90
            PDF.PDFrotate(PDF, inputfiles, outputfiles, steps)
        else:
            print("Please use a higher value than 0")
            sys.exit(0)
    elif mode == 'merge':
        PDF.PDFmerge(PDF, filenames=inputfiles, outputfile=outputfiles[0])
            
if __name__ == "__main__":
    main(sys.argv[1:])

