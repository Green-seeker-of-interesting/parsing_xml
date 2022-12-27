from ODT import XmlFile


class CSVWriter:

    def write(self, file: XmlFile):
        treak = file.path.replace(".xml", ".csv")
        with open(treak, "w", encoding=file.encoding) as f:
            for payer in file.payers:
                f.writelines(str(payer))
