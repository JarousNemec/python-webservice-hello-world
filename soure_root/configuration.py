import logging
import os
import sys
import uuid
import platform
import socket

host = "127.0.0.1"
port = 80
ssl = False
manager_ssl = False

windows_dev_root = "c:\\bizerba\\statistics\\"
linux_root = "/bizerba/statistics"

tesco_sftp_user = 'svc_sftp_Bizerba'
tesco_sftp_pass = 'BYTEYTBGX86kxj'
tesco_sftp_host = 'sftptesco.tesco-europe.com'

bizerba_scale_ftp_user = "bizuser"
bizerba_scale_ftp_password = "bizerba"


AUTOMAT_CONN_STR = "DefaultEndpointsProtocol=https;AccountName=bizerbaimagedb;AccountKey=MRjyEMcBiHjkm7K/RuKDOLVzQbUnKMvHYH9Zwy/iGQ+tLxDH9xsN5C48QfT/ERq8rPBdPcOlxy7G+AStF18bWw==;EndpointSuffix=core.windows.net"
FILETRACK_CONN_STR = "DefaultEndpointsProtocol=https;AccountName=bizerbafiletrack;AccountKey=RIYPopgb1iOBDYkZWN29cow1U0YFUmgbK3PZg3Fg3PDW7zjOaFygPOzkuvyOGDmmBUX1yTPU4TgR+AStDpmKsw==;EndpointSuffix=core.windows.net"

STORAGEACCOUNTURL = "https://bizerbaimagedb.blob.core.windows.net"
STORAGEACCOUNTKEY = "MRjyEMcBiHjkm7K/RuKDOLVzQbUnKMvHYH9Zwy/iGQ+tLxDH9xsN5C48QfT/ERq8rPBdPcOlxy7G+AStF18bWw=="
CONTAINERNAME = "statistics"

def is_windows():
    return platform.system() == 'Windows'


def get_datastorage_directory():
    return os.path.join(windows_dev_root, "data") if is_windows() else os.path.join(linux_root, "data")


def get_log_directory():
    return os.path.join(windows_dev_root, "log") if is_windows() else os.path.join(linux_root, "log")

