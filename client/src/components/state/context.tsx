import { createContext, useReducer, Dispatch } from "react";

import { AppReducer, ReducerActions } from "./reducer";

type FCWithChildrenType = {
    children: React.ReactNode
}

type InitialStateType = {
    fromFloor: number | null,
    toFloor: number | null
}

const initialState: InitialStateType = {
    fromFloor: null,
    toFloor: null
}

const AppContext = createContext<{
    state: InitialStateType;
    dispatch: Dispatch<ReducerActions>;
}>({
    state: initialState,
    dispatch: () => null
});

const AppContextProvider = ({ children }: FCWithChildrenType) => {
    const [ state, dispatch ] = useReducer(AppReducer, initialState)

    return (
        <AppContext.Provider value={{ state, dispatch }}>
            {children}
        </AppContext.Provider>
    )
}

export { AppContext, AppContextProvider}
