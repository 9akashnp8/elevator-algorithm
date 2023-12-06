import { useContext } from 'react'

import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"

import { AppContext } from '../state/context'
import { ActionTypes } from '../state/reducer'

type Props = {
    numberOfFloors: number
} // reduce duplicate, import from floor grid comp.

export default function UserFloorSelect({ numberOfFloors }: Props) {
    const { dispatch } = useContext(AppContext);

    function handleClick(value: any) {
        dispatch({
            type: ActionTypes.SetUserFloor,
            payload: value
        })
    }
    return (
        <Select onValueChange={handleClick} >
            <SelectTrigger className="w-[180px]">
                <SelectValue placeholder="User Floor" />
            </SelectTrigger>
            <SelectContent>
                {[...Array(numberOfFloors)].map((_, i) =>
                    <SelectItem value={`${i}`}>Floor {i}</SelectItem>
                )}
            </SelectContent>
        </Select>
    )
}