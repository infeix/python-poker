from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Game:
    
    cards: List[str] = field(default_factory=list)