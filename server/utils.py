
def initial_req_msg(
    destination_floor: str,
    request_from: str,
    current_floor: str
):
    return (
        f"""
        Want to go: {destination_floor},
        Request from: {request_from},
        Elevator currently on: {current_floor},
        """
    )