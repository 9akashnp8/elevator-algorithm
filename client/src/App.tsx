import { useState } from 'react'

import '@/styles/global.css'
import FloorInputGrid from './components/ui/floorInputGrid'
import ElevatorUpdatesBox from './components/ui/elevatorUpdatesBox'
import Elevator from './components/elevator'

function App() {
  const [count, setCount] = useState(0)

  return (
    <main className='flex justify-between h-screen'>
      <section className='floorControl | flex flex-col justify-between bg-slate-400 grow'>
        <div className='floorInput my-auto'>
          <FloorInputGrid  numberOfFloors={10}/>
        </div>
        <div className='floorUpdates'>
          <ElevatorUpdatesBox />
        </div>
      </section>
      <section className='elevatorViz | bg-slate-600 grow'>
        <div className='relative w-full h-screen'>
          <Elevator />
        </div>
      </section>
    </main>
  )
}

export default App
