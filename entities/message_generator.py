import json

from communication_entities.messages.add_orchestrator_message import AddOrchestratorMessage
from communication_entities.messages.add_vnf_message import AddVNF
from communication_entities.messages.add_vnf_to_chain_message import AddVNFToChainMessage
from communication_entities.messages.lcm_messages.migration.migration_message import MigrationMessage
from communication_entities.messages.lcm_messages.request_service_scale_message import RequestServiceScaleMessage
from communication_entities.messages.process_data_message import ProcessDataMessage
from communication_entities.messages.request_update_all_vnffg_message import RequestUpdateAllVNFFGMessage
from communication_entities.messages.request_update_message import RequestUpdateMessage
from communication_entities.messages.vnf_forwarding_graph.request_update_all_vnffg_sequential_message import \
    RequestUpdateAllVNFFGSequentialMessage
from communication_entities.messages.vnf_forwarding_graph.update_vnf_fg_classifier_message import \
    UpdateVnfFgClassifierMessage
from communication_entities.messages.vnf_forwarding_graph.update_vnf_fg_rended_service_path_message import \
    UpdateVnfFgRenderedServicePathMessage
from entities.communication_entity_package import CommunicationEntityPackage
from entities.parameters.parameter_generator import ParameterGenerator
from entities.parameters.parameter_package import ParameterPackage
from utilities.command_package import CommandPackage
from utilities.logger import log
from utilities.message_type import MessageType


class MessageGenerator:

    def __init__(self, command:CommandPackage, json_file):
        self.command = command
        self.json_file = json_file

    def generate_message(self):
        m = None
        if self.command.message_type == "add_vnf":
            m = self.generate_add_message(self.command.vnf_host, self.command.vnf_port, self.command.get_vnf_name)
        elif self.command.message_type == "add_chain":
            m = self.generate_chain_message(self.command.vnf_host, self.command.vnf_port)
        elif self.command.message_type == "migration":
            m = self.generate_migration_message(self.command.get_vnf_name, self.command.new_name)
        elif self.command.message_type == "new_pop":
            print("Request new pop")
        elif self.command.message_type == "add_orchestrator":
            m = AddOrchestratorMessage(self.command.vnf_host,
                                       self.command.vnf_port,
                                       orchestrator_id=self.command.orchestrator_id)
        elif self.command.message_type == "process":
            m = self.generate_process_message()
        elif self.command.message_type == "update_vnffg_rsp":
            m = UpdateVnfFgRenderedServicePathMessage(self.command.vnf_identifier,
                                                      self.command.order,
                                                      self.command.ingress_connection_point,
                                                      self.command.egress_connection_point)
        elif self.command.message_type == "update_vnffg_classifier":
            m = UpdateVnfFgClassifierMessage(self.command.match_identifier,
                                             self.command.ip_proto,
                                             self.command.source_ip,
                                             self.command.destination_ip,
                                             self.command.source_port,
                                             self.command.destination_port)
        elif self.command.message_type == "request_update":
            m = RequestUpdateMessage(self.command.seed)
        elif self.command.message_type == "request_scaling_of_service":
            m = RequestServiceScaleMessage(self.command.service_id, self.command.seed)
        elif self.command.message_type == 'do_asynchronous_updates':
            m = RequestUpdateAllVNFFGMessage()
        elif self.command.message_type == 'do_sequential_updates':
            m = RequestUpdateAllVNFFGSequentialMessage()
        return m

    @staticmethod
    def generate_add_message(vnf_host, vnf_port, vnf_name):
        return AddVNF(vnf_host, vnf_port, vnf_name)

    @staticmethod
    def generate_migration_message(name, new_name):
        return MigrationMessage(name, new_name)

    @staticmethod
    def generate_chain_message(vnf_host, vnf_port):
        return AddVNFToChainMessage(vnf_host, vnf_port)

    def generate_process_message(self):
        messages = list()
        with open(self.json_file, 'r') as json_file:
            data = json.load(json_file)
            for service in data['services']:
                operations = service['operations']
                number_servers = len(operations)
                if 'annotation' in service['parameters']:
                    annotation_parameter = service['parameters']['annotation']
                if 'crop' in service['parameters']:
                    crop_parameter = service['parameters']['crop']
                if 'fade_in' in service['parameters']:
                    fade_in_parameter = service['parameters']['fade_in']
                if 'fade_out' in service['parameters']:
                    fade_out_parameter = service['parameters']['fade_out']
                file_parameter = service['parameters']['file']
                if 'resize' in service['parameters']:
                    resize_parameter = service['parameters']['resize']
                # print("Width: ", str(resize_parameter.width), "Height: ", str(resize_parameter.height))
                host_servers = service['host_servers']
                port_servers = service['port_servers']
                speed_factor = service['speed_factor']
                operations = self.parse_operations(operations)
                param_gen = ParameterGenerator(annotation_parameter,
                                               crop_parameter,
                                               fade_in_parameter,
                                               fade_out_parameter,
                                               file_parameter,
                                               resize_parameter)
                param_gen.generate_parameters()

                servers = list()
                for i in range(number_servers):
                    # print("Index: ", i)
                    servers.append(CommunicationEntityPackage(host_servers[i], int(port_servers[i])))

                parameters = ParameterPackage(annotation=param_gen.annotation,
                                              file_pack=param_gen.file,
                                              vnf_servers=servers,
                                              operations=operations,
                                              speed_factor=speed_factor,
                                              crop=param_gen.crop,
                                              fade_in=param_gen.fade_in,
                                              fade_out=param_gen.fade_out,
                                              resize=param_gen.resize)
                m = ProcessDataMessage(parameters)
                messages.append(m)
        return messages

    def parse_operations(self, operations):
        parsed_operations = list()
        for op in operations:
            parsed_operations.append(self.generate_operation(op))
        return parsed_operations

    # TODO: Add this method to the class that holds the all the types of VNFs
    @staticmethod
    def generate_operation(op):
        log.info(op)
        if op == "ANNOTATE":
            return MessageType.ANNOTATE
        if op == "BLACK_WHITE":
            return MessageType.BLACK_WHITE
        if op == "COMPOSITE":
            return MessageType.COMPOSITE
        if op == "CROP":
            return MessageType.CROP
        if op == "FADE_IN":
            return MessageType.FADE_IN
        if op == "FADE_OUT":
            return MessageType.FADE_OUT
        if op == "INVERT_COLORS":
            return MessageType.INVERT_COLORS
        if op == "MIRROR_X":
            return MessageType.MIRROR_X
        if op == "MIRROR_Y":
            return MessageType.MIRROR_Y
        if op == "PAINTING":
            return MessageType.PAINTING
        if op == "RESIZE":
            return MessageType.RESIZE
        if op == "ROTATE":
            return MessageType.ROTATE
        if op == "SPEED_UP":
            return MessageType.SPEED_UP
        return MessageType.INVALID
