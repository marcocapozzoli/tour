from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Department:
    name: str
    cost_center: str
    integration_code: str
    company: str
    is_active: Optional[bool] = True
    id: Optional[str] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
