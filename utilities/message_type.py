from enum import Enum


class MessageType(Enum):
    MIGRATION = 1
    SEARCH_VNF = 2
    ADD_VNF = 3
    ADD_ORCHESTRATOR = 4
    VNF_NOT_FOUND = 5
    VNF_FOUND = 6
    BEGIN = 7
    MSG_RECEIVED = 8
    MIGRATION_TOPOLOGY = 9
    MP4_FORMAT = 10
    WEB_FORMAT = 11
    ANNOTATE = -1
    CROP = -2
    INVERT_COLORS = -3
    RESIZE = -4
    SPEED_UP = -5
