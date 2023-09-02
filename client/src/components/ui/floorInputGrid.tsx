import { useContext } from "react"

import { Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

import { AppContext } from "../state/context"
import { ActionTypes } from "../state/reducer"

type Props = {
    numberOfFloors: number
}

export default function FloorInputGrid({ numberOfFloors }: Props) {
    const { dispatch } = useContext(AppContext)

    function handleClick(e: any) {
        dispatch({
            type: ActionTypes.GoToFloor,
            payload: {
                fromFloor: 0, // get current floor from state once movement complete
                toFloor: +e.target.value
            }
        })
    }

    return (
        <div className="grid grid-cols-3 gap-y-5 justify-items-center">
            {[...Array(numberOfFloors)].map((_, i) =>
                <Card>
                    <Button size={"lg"} value={i} onClick={handleClick} >
                        {i}
                    </Button>
                </Card>
            )}
        </div>
    )
}