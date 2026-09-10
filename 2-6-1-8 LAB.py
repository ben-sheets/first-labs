#Scenario
#
#    You are about to create a multifunction device (MFD) that can scan and print documents;
#    the system consists of a scanner and a printer;
#    your task is to create blueprints for it and deliver the implementations;
#    create an abstract class representing a scanner that enforces the following methods:
#        scan_document – returns a string indicating that the document has been scanned;
#        get_scanner_status – returns information about the scanner (max. resolution, serial number)
#    Create an abstract class representing a printer that enforces the following methods:
#        print_document – returns a string indicating that the document has been printed;
#        get_printer_status – returns information about the printer (max. resolution, serial number)
#    Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
#        MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
#        MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
#        MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.
#    Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.


import abc

class MFD(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass
    def get_scanner_status(self):
        pass


class MFD1(MFD):
    def scan_document(self):
        print("Document scanned in Black and White at 300dpi")
    def get_scanner_status(self):
        print("Max Resolution 300dpi, Serial Number: 94jkf9f")
    def printer(self):
        print("Printing in Black and White at 300dpi")


class MFD2(MFD):
    def scan_document(self):
        print("Document scanned in Color at 600 dpi")
    def get_scanner_status(self):
        print("Max Resolution 600dpi, Serial Number 94jf0fj")
    def printer(self):
        print("Printing in Color at 600dpi")
    def print_history(self):
        print("Printing log of last 7 days worth of print jobs")


class MFD3(MFD):
    def scan_document(self):
        print("Document scanned in Color at 1200 dpi")
    def get_scanner_status(self):
        print("Max Resolution 2400dpi, SerialNumber kdfiu38dfjf")
    def printer(self):
        print("Printing in Color at 1200 dpi")
    def print_history(self):
        print("Printing log of last 90 days worth of print jobs")
    def fax(self):
        print("Sending fax...")

print("################# Multifunction Device One #################")
one = MFD1()
one.scan_document()
one.get_scanner_status()
one.printer()
print("################# Multifunction Device Two #################")
two = MFD2()
two.scan_document()
two.get_scanner_status()
two.printer()
two.print_history()
print("################# Multifunction Device Three #################")
three = MFD3()
three.scan_document()
three.get_scanner_status()
three.printer()
three.print_history()
three.fax()
