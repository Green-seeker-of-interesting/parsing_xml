from dataclasses import dataclass
from hashlib import md5


@dataclass
class Payer:
    personal_account: str  # key
    period: str  # key
    full_name: str = ""
    address: str = ""
    total: float = 0.00

    def __str__(self) -> str:
        out = map(str, [self.personal_account, self.full_name,
                  self.address, self.period, self.total])
        return "; ".join(out) + "\n"

    def __hash__(self) -> int:
        key = self.personal_account + self.period
        return int(md5(key.encode()).hexdigest(), 16)
