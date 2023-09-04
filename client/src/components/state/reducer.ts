
import { FloorRequestType } from "./context";

type ActionMap<M extends { [index: string]: any }> = {
    [Key in keyof M]: M[Key] extends undefined
    ? {
        type: Key;
    }
    : {
        type: Key;
        payload: M[Key];
    }
};

export enum ActionTypes {
    GoToFloor = 'GO_TO_FLOOR',
    SetCurrentFloor = 'SET_CURRENT_FLOOR',
}

// --- Floor Request ---
type FloorRequestPayload = {
    [ActionTypes.GoToFloor]: FloorRequestType
}

export type FloorRequestActions = ActionMap<FloorRequestPayload>[keyof ActionMap<FloorRequestPayload>]

export const FloorRequestReducer = (state: FloorRequestType, action: FloorRequestActions | CurrentFloorActions) => {
    switch (action.type) {
        case ActionTypes.GoToFloor:
            return {
                ...state,
                fromFloor: action.payload.fromFloor,
                toFloor: action.payload.toFloor
            }
        default:
            return state
    }
}

// --- Current Floor ---
type CurrentFloorPayload = {
    [ActionTypes.SetCurrentFloor]: number
}

export type CurrentFloorActions = ActionMap<CurrentFloorPayload>[keyof ActionMap<CurrentFloorPayload>]

export const CurrentFloorReducer = (state: number, action: FloorRequestActions | CurrentFloorActions) => {
    switch (action.type) {
        case ActionTypes.SetCurrentFloor:
            return action.payload
        default:
            return state
    }
}
