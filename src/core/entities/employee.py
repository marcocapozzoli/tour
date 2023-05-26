from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EmployeeEntity:
    full_name: str
    email: str
    phone: str
    birthday: datetime
    entry_date: datetime
    departure_date: datetime
    city: str
    department: str
    is_active: Optional[bool] = True
    id: Optional[str] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
