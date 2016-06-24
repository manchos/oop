# -*- coding: utf-8 -*-

network = ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super")

def check_connection(network, first, second):
    for link in network:

