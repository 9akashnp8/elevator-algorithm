
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
    GoToFloor = 'GO_TO_FLOOR'
}

type FloorType = {
    fromFloor: number | null,
    toFloor: number | null
}

type ActionPayload = {
    [ActionTypes.GoToFloor] : FloorType
}

export type ReducerActions = ActionMap<ActionPayload>[keyof ActionMap<ActionPayload>]

export const AppReducer = (state: FloorType, action: ReducerActions) => {
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