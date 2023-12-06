import { useContext } from "react";
import { animated, useSpring } from "@react-spring/web";

import { AppContext } from "./state/context";

export default function Elevator() {
    const { state } = useContext(AppContext)
    const floorBreakPoint = Math.round(window.innerHeight / 10)

    const springs = useSpring({
        from: { bottom: 0 },
        to: { bottom: state.currentFloor! * floorBreakPoint }
    })

    return (
        <animated.div
            style={{
                position: 'absolute',
                left: '50%',
                transform: 'translateX(-50%)',
                width: 80,
                height: 80,
                background: '#ff6d6d',
                borderRadius: 8,
                display: 'grid',
                placeItems: 'center',
                ...springs
            }}
        >
            <p className="text-2xl text-white font-bold" >{state.currentFloor}</p>
        </animated.div>
    )
}