from pydantic import BaseModel
from typing import Optional

from operations.interface import DataInterface
from db.engine import DBSession
from db.models import DBCustomer, to_dict


class CustomerCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str

class CustomerUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]    

def read_all_customers(customer_interface: DataInterface):
    return customer_interface.read_all()

def read_customer(customer_id: int, customer_interface: DataInterface):
    return customer_interface.read_by_id(customer_id)

def create_customer(data: CustomerCreateData, customer_interface: DataInterface) -> DBCustomer:
    customer = DBCustomer(**data.dict())
    return customer_interface.create(customer)

def update_customer(customer_id: int, data: CustomerUpdateData, customer_interface: DataInterface):
    return customer_interface.update(id=customer_id, data=data.dict())

def delete_customer(customer_id: int, customer_interface: DataInterface):
    return customer_interface.delete(id)