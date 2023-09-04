import { useContext, useState, useEffect, useCallback } from "react"
import { useWebSocket } from "react-use-websocket/dist/lib/use-websocket";

import { Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

import { AppContext } from "../state/context"
import { ActionTypes } from "../state/reducer"

type Props = {
    numberOfFloors: number
}

export default function FloorInputGrid({ numberOfFloors }: Props) {
    const { state, dispatch } = useContext(AppContext)
    const [ messages, setMessages ] = useState<any[]>([])

    const { sendMessage, lastMessage } = useWebSocket('ws://127.0.0.1:8000/ws');

    useEffect(() => {
        if (lastMessage !== null) {
            let message = JSON.parse(lastMessage.data)
            let currentFloor = message.current
            setMessages((prev) => prev.concat(message))
            dispatch({
                type: ActionTypes.SetCurrentFloor,
                payload: currentFloor
            })
        }
    }, [lastMessage, setMessages])

    const handleClickSendMessage = useCallback((e: any) => 
        sendMessage(JSON.stringify({
            "destination_level": +e.target.value,
            "current_level": state.currentFloor
        })),
        []
    );

    return (
        <div className="grid grid-cols-3 gap-y-5 justify-items-center">
            {[...Array(numberOfFloors)].map((_, i) =>
                <Card>
                    <Button size={"lg"} value={i} onClick={handleClickSendMessage} >
                        {i}
                    </Button>
                </Card>
            )}
        </div>
    )
}