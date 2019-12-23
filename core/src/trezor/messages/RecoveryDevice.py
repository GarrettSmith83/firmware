# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeRecoveryDeviceType = Literal[0, 1]
    except ImportError:
        pass


class RecoveryDevice(p.MessageType):
    MESSAGE_WIRE_TYPE = 45

    def __init__(
        self,
        word_count: int = None,
        passphrase_protection: bool = None,
        pin_protection: bool = None,
        language: str = None,
        label: str = None,
        enforce_wordlist: bool = None,
        type: EnumTypeRecoveryDeviceType = None,
        u2f_counter: int = None,
        dry_run: bool = None,
    ) -> None:
        self.word_count = word_count
        self.passphrase_protection = passphrase_protection
        self.pin_protection = pin_protection
        self.language = language
        self.label = label
        self.enforce_wordlist = enforce_wordlist
        self.type = type
        self.u2f_counter = u2f_counter
        self.dry_run = dry_run

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('word_count', p.UVarintType, 0),
            2: ('passphrase_protection', p.BoolType, 0),
            3: ('pin_protection', p.BoolType, 0),
            4: ('language', p.UnicodeType, 0),  # default=en-US
            5: ('label', p.UnicodeType, 0),
            6: ('enforce_wordlist', p.BoolType, 0),
            8: ('type', p.EnumType("RecoveryDeviceType", (0, 1)), 0),
            9: ('u2f_counter', p.UVarintType, 0),
            10: ('dry_run', p.BoolType, 0),
        }
