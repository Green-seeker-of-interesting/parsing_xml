from dataclasses import dataclass


@dataclass
class GeneralInfo:
    date_file: str  # reg
    file_number: str = ''
    type_info: str = ''
    recipient_id: str = ''
    sender_id: str = ''
