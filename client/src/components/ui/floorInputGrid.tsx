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
    const { dispatch } = useContext(AppContext)
    const [ messages, setMessages ] = useState<string[]>([])

    const { sendMessage, lastMessage } = useWebSocket('ws://127.0.0.1:8000/ws');

    useEffect(() => {
        if (lastMessage !== null) {
            setMessages((prev) => prev.concat(lastMessage.data))
        }
    }, [lastMessage, setMessages])

    const handleClickSendMessage = useCallback((e: any) => 
        sendMessage(JSON.stringify({
            "destination_level": e.target.value,
            "current_level": 11
        })),
        []
    );

    return (
        <div className="grid grid-cols-3 gap-y-5 justify-items-center">
            {[...Array(numberOfFloors)].map((_, i) =>
                <Card>
                    <Button size={"lg"} value={+i} onClick={handleClickSendMessage} >
                        {i}
                    </Button>
                </Card>
            )}
        </div>
    )
}