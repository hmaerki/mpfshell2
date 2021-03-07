from mp import pyboard_query

def example_A():
    _board = pyboard_query.ConnectComport('COM9')
    # This call will list a 'connected' com port.
    pyboard_query.BoardQueryBase.print_all()

def example_B():
    print('start')
    scanner = pyboard_query.BoardQueryPyboard('scanner_pyb_2020')
    compact = pyboard_query.BoardQueryPyboard('compact_2012')
    pyboard_query.Connect([compact, scanner])
    print('done')

def example_pyboard_firmwareupdate():
    anypyboard = pyboard_query.ConnectPyboard(hwtype=None)
    anypyboard.systemexit_firmware_required(min='1.13', max='1.15')

def main():
    anypyboard = pyboard_query.ConnectComport(comport=None, product=pyboard_query.Product.Pyboard)
    anypyboard.close()
    anypyboard = pyboard_query.ConnectPyboard(hwtype=None, product=pyboard_query.Product.Pyboard)
    anypyboard.close()

    pyboard_query.BoardQueryBase.print_all()
    example_pyboard_firmwareupdate()

if __name__ == "__main__":
    main()
