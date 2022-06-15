import argparse
import logging
import os
import sys
import time

# logger formatter const
STR_FMT = '%(asctime)s - %(levelname)s : %(message)s'
DATE_FMT = '%d/%m/%Y %H:%M:%S'

def compare_folder(logger: logging.Logger, cur_datas, new_datas) -> None:
    """
    """
    logger.info("No files to delete",)
    logger.info("No new files",)
    logger.info("No files changed",)

def snapshot_folder(logger: logging.Logger, folder: str, depth: int, nbsep: int) -> dict:
    """
    """
    # new datas
    data_files = None

    # go for a walk
    for root, dirs, files in os.walk(folder):
        nbsep_root = root.count(os.sep) - nbsep
        # files
        for name in files:
            filename = os.path.join(root, name)

        # files
        for name in dirs:
            dirname = os.path.join(root, name)

        # depth ok
        if nbsep_root > depth:
            logger.debug("%s is more depth than the depth (%d) param", root, depth)
            dirs[:] = []

    return data_files

def main(logger: logging.Logger, folder: str, freq: int, logfile: str,
            depth: int, dest: list):
    """
    """
    if logfile is not None:
        # create file logger
        hdlr = logging.FileHandler(logfile)

        formatter = logging.Formatter(STR_FMT, DATE_FMT)
        hdlr.setFormatter(formatter)

        # add file handler to logger
        logger.addHandler(hdlr)

    # check folder
    if os.path.isdir(folder) is False:
        logger.error("%s is not a folder", folder)
        return

    # count nb sep from folder
    nbsep = folder.count(os.sep)

    # first snapshot
    logger.warning("Get first snapshot  ..... ")
    cur_dict_files = snapshot_folder(logger, folder, depth, nbsep)
    try:
        logger.warning("Polling starts  ..... ")
        while True:
            #sleep for a freq delay
            time.sleep(freq)

            # take a new one snapshot
            new_dict_files = snapshot_folder(logger, folder, depth, nbsep)

            #compare the two snapshots
            compare_folder(logger, cur_dict_files, new_dict_files)

            # save new snapshot
            cur_dict_files = new_dict_files
            new_dict_files = None

    except (KeyboardInterrupt, SystemExit) as e:
        logger.warning("This is the end ..... on %s", str(e))

    except Exception as e:
        logger.error("Error on %s", str(e))


def parseargs(logger: logging.Logger, parser: argparse.ArgumentParser) -> dict:
    """
    """
    #params
    delay = 15
    parser.add_argument('folder', nargs=1, type=str, help='Directory or folder to supervise')
    parser.add_argument('--log',  dest='logfile', type=str, default=None, help='Name and location of log file')
    parser.add_argument('--freq', dest='freq', type=int, default=delay, help=f'Delay beetween two comparaison - default is {delay}')
    parser.add_argument('--depth', dest='depth', type=int, default=3, help='Size of depth tree - default is 3')
    parser.add_argument('--debug', dest='debug', action='store_true', default=False, help='Debug - default is False')

    return parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    """
    main entry
    """
    # logger
    logging.basicConfig(datefmt=DATE_FMT,format=STR_FMT, level=logging.INFO)
    logger = logging.getLogger()

    # parser
    parser = argparse.ArgumentParser(description='Supervise a folder.')
    args = parseargs(logger,parser)
    print (args)

    #call main
    if args.debug is True:
        logger.setLevel(logging.DEBUG)

    main(logger, args.folder[0], args.freq, args.logfile, args.depth, ["yduprat@gmail.com"])
