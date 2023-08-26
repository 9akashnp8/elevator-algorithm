import { Flex } from '@radix-ui/themes';

import './index.css'

export default function MyApp() {
  return (
    <Flex direction="row" justify="between">
      <section className='section'>
        <h1>Floor Selection</h1>
      </section>
      <section className='section'>
        <h1>Elevator Diagram</h1>
      </section>
    </Flex>
  );
}