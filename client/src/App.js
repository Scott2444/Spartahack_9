import React, { useState, useEffect } from 'react'
import './App.css';
import Box from './Box';

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div className="center">
      <h1>2024 Election Statistical Prediction</h1>
      <Box/>
      {/* {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ): (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )} */}
    </div>
  )
}

export default App