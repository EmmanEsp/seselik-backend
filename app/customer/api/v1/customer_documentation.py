
create_customer_responses = {
    201: {
        "content": {
            "application/json": {
                "example":{
                    "status": "success",
                    "status_code": 201,
                    "data": None
                }
            }
        }
    },
    400: {
        "content": {
            "application/json": {
                "example":{
                    "status": "fail",
                    "status_code": 400,
                    "data": {"email": "Email already in use."}
                }
            }
        }
    }
}
