import { animated, useSpring } from "@react-spring/web";

export default function Elevator() {
    const [ springs, api ] = useSpring(() => ({
        from: { bottom: 0 }
    }))

    function handleClick() {
        api.start({
            from: { bottom: 0 },
            to: { bottom: 100 }
        })
    }

    return (
        <animated.div
            onClick={handleClick}
            style={{
                position: 'absolute',
                left: '50%',
                transform: 'translateX(-50%)',
                width: 80,
                height: 80,
                background: '#ff6d6d',
                borderRadius: 8,
                ...springs
            }}
        />
    )
}