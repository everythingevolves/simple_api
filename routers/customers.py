from fastapi import APIRouter

from db.db_interface import DBInterface
from db.models import DBCustomer
from operations.customers import (
    CustomerCreateData,
    CustomerUpdateData,
    create_customer,
    read_all_customers,
    read_customer,
    update_customer
)

router = APIRouter()

@router.get("/customers")
def api_read_all_customers():
    customer_interface = DBInterface(DBCustomer)
    return read_all_customers(customer_interface=customer_interface)
# curl -X GET http://localhost:8000/customers

@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int):
    customer_interface = DBInterface(DBCustomer)
    return read_customer(customer_id=customer_id, customer_interface=customer_interface)

@router.post("/customer")
def api_create_customer(customer: CustomerCreateData):
    customer_interface = DBInterface(DBCustomer)
    return create_customer(data=customer, customer_interface=customer_interface)
# curl -X POST -H "Content-Type: application/json" \
# -d '{"first_name": "Susan", "last_name": "Ivanova", "email_address": "susan@b5.com"}' \
# http://localhost:8000/customer

@router.post("/customer/{customer_id}")
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    customer_interface = DBInterface(DBCustomer)
    return update_customer(customer_id=customer_id, data=customer, customer_interface=customer_interface)