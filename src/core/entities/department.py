from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DepartmentEntity:
    name: str
    cost_center: str
    integration_code: str
    company: str
    is_active: Optional[bool] = True
    id: Optional[str] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
