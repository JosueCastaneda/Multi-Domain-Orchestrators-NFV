from enum import Enum


class StringConstants(Enum):
    SEND_PREVIOUS_VNF_P = 'Sending SendQueuePMessage to previous VNF'
    SEND_PREVIOUS_VNF_Q = 'Sending SendQueueQMessage to previous VNF'
    SEND_NEW_VNF_R = 'Sending R to new VNF'
    SEND_PREVIOUS_VNF_SWITCH = 'Sending Switch message to previous VNF'
    SEND_NEW_VNF_DEACTIVATE_RECURSIVE = 'Send MigrationDeactivateRecursiveMessage to new VNF'
    SEND_PREVIOUS_VNF_ACK = 'Sending ACK message to previous VNF'
    SEND_PREVIOUS_VNF_MIGRATION_DEACTIVATE = 'Sending deactivate message migration to previous VNF'
    SEND_NEW_VNF_BEGIN_MIGRATION = 'Sending begin migration to new VNF'
    SEND_NEW_VNF_TERMINATE_MIGRATION_NO_RECURSION = 'Send TerminateMessageWithoutRecursion to new VNF'
    SEND_NEW_VNF_ACK = 'Sending ACK message to new VNF'
    SEND_NEW_VNF_MIGRATION_HAS_ENDED = 'Sending terminate message to new VNF. Migration has ended'
    SEND_NEW_VNF_QUEUES = 'Sending all queues to new VNF'
    SEND_NEW_VNF_TERMINATE_MESSAGE = 'Send TerminateMessage to new VNF'