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
    BLACK_WHITE = -2
    COMPOSITE = -3
    CROP = -4
    FADE_IN = -5
    FADE_OUT = -6
    INVERT_COLORS = -7
    MIRROR_X = -8
    MIRROR_Y = -9
    PAINTING = -10
    RESIZE = -11
    ROTATE = -12
    SPEED_UP = -13
    INVALID = -100
