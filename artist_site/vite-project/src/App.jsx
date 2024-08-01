import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

import ArtistStats from './components/artist_stat_form'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <ArtistStats></ArtistStats>
      </div>
    </>
  )
}

export default App
