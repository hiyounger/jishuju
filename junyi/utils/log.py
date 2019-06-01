# -*- encoding:utf-8 -*-


def debug(msg):
    print("[DEBUG] " + str(msg))


def info(msg):
    print("[INFO] " + str(msg))


def error(msg):
    print("\033[1;31;40m %s \033[1;31;40m" % str(msg))