INVERTER_PORT = 10081

# App -> DTU start with 0xa3, responses start 0xa2
CMD_HEADER = b'HM'
CMD_APP_INFO_DATA_RES_DTO = b'\xa3\x01'
CMD_HB_RES_DTO = b'\xa3\x02'
CMD_REAL_DATA_RES_DTO = b'\xa3\x03'
CMD_W_INFO_RES_DTO = b'\xa3\x04'
CMD_COMMAND_RES_DTO = b'\xa3\x05'
CMD_COMMAND_STATUS_RES_DTO = b'\xa3\x06'
CMD_DEV_CONFIG_FETCH_RES_DTO = b'\xa3\x07'
CMD_DEV_CONFIG_PUT_RES_DTO = b'\xa3\x08'
CMD_GET_CONFIG = b'\xa3\x09'
CMD_SET_CONFIG = b'\xa3\x10'
CMD_REAL_RES_DTO = b'\xa3\x11'
CMD_GPST_RES_DTO = b'\xa3\x12'
CMD_AUTO_SEARCH = b'\xa3\x13'
CMD_NETWORK_INFO_RES = b'\xa3\x14'
CMD_APP_GET_HIST_POWER_RES = b'\xa3\x15'
CMD_APP_GET_HIST_ED_RES = b'\xa3\x16'
CMD_HB_RES_DTO_ALT = b'\x83\x01'
CMD_REGISTER_RES_DTO = b'\x83\x02'
CMD_STORAGE_DATA_RES = b'\x83\x03'
CMD_COMMAND_RES_DTO_2 = b'\x83\x05'
CMD_COMMAND_STATUS_RES_DTO_2 = b'\x83\x06'
CMD_DEV_CONFIG_FETCH_RES_DTO_2 = b'\x83\x07'
CMD_DEV_CONFIG_PUT_RES_DTO_2 = b'\x83\x08'
CMD_GET_CONFIG_RES = b'\xdb\x08'
CMD_SET_CONFIG_RES = b'\xdb\x07'

CMD_CLOUD_COMMAND_RES_DTO = b'\x23\x05'

CMD_ACTION_FIRMWARE_UPGRADE = 2
CMD_ACTION_RESTART = 3
CMD_ACTION_TURN_ON = 6
CMD_ACTION_TURN_OFF = 7
CMD_ACTION_POWER_LIMIT = 8
