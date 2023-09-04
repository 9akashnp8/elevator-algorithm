import { createContext, useReducer, Dispatch } from "react";

import {
    FloorRequestReducer,
    CurrentFloorReducer,
    FloorRequestActions,
    CurrentFloorActions,
} from "./reducer";

type FCWithChildrenType = {
    children: React.ReactNode
}

export type FloorRequestType = {
    fromFloor: number | null,
    toFloor: number | null,
}

type InitialStateType = {
    floorRequest: FloorRequestType
    currentFloor: number,
}

const initialState: InitialStateType = {
    floorRequest: {
        fromFloor: 0,
        toFloor: 0
    },
    currentFloor: 0
}

const AppContext = createContext<{
    state: InitialStateType;
    dispatch: Dispatch<FloorRequestActions | CurrentFloorActions>;
}>({
    state: initialState,
    dispatch: () => null
});

const mainReducer = (
    {floorRequest, currentFloor}: InitialStateType,
    action: FloorRequestActions | CurrentFloorActions
) => {
    console.info(`
        ----STATE-UPDATE----
        ${JSON.stringify(floorRequest)}
        ${currentFloor}
    `)
    return {
        floorRequest: FloorRequestReducer(floorRequest, action),
        currentFloor: CurrentFloorReducer(currentFloor, action)
    }
}

const AppContextProvider = ({ children }: FCWithChildrenType) => {
    const [ state, dispatch ] = useReducer(mainReducer, initialState)

    return (
        <AppContext.Provider value={{ state, dispatch }}>
            {children}
        </AppContext.Provider>
    )
}

export { AppContext, AppContextProvider}
