import PyPDF2, sys

class PDF:
    # rotate pdf
    def PDFrotate(self, filenames, outputfiles, rotation):
        if len(filenames) == len(outputfiles):
            try:
                for counter in range(len(filenames)):
                    pdfFile = open(filenames[counter], 'rb')
                    pdfReader = PyPDF2.PdfFileReader(pdfFile)

                    # creating pdf Writer
                    pdfWriter = PyPDF2.PdfFileWriter()
                    # rotation every page
                    for page in range(pdfReader.numPages):
                        pageObject = pdfReader.getPage(page)
                        pageObject.rotateClockwise(rotation)

                        # adding rotated page to Writer
                        pdfWriter.addPage(pageObject)
                    # create rotated pdf
                    newFile = open(outputfiles[counter], 'wb')
                    pdfWriter.write(newFile)
                    pdfFile.close()
                    newFile.close()
            except Exception as e:
                print(e)
                sys.exit(1)
        else:
            print("Please use the same amount of outputfiles and inputfiles")
            sys.exit(1)
            
    # merge multiple PDFs together
    def PDFmerge(self,filenames, outputfile):
        try:
            pdfMerge = PyPDF2.PdfFileMerger()
            for pdf in filenames:
                pdfMerge.append(PyPDF2.PdfFileReader(pdf, 'rb'))
            pdfMerge.write(outputfile)
            print('Successfully merged the files together')
        except Exception as e:
            print(e)
            sys.exit(1)
            