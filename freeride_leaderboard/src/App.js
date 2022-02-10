import React, { Component } from 'react';
import './App.css';
import './practice/Table.css'

function App() {
  const [entries, setEntries] = React.useState(null);

  React.useEffect(() => {
  fetch("/api")
      .then((res) => res.json())
      .then((data) => setEntries(data));
  }, []);

  return (
    <div className="App">
      <div className="header">
        <img src="/freeride_logo_transparent.png" alt="biker going down mountain terrain logo" width="300" height="300"/>
      </div>
      <div>
        <table class="Table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {entries && entries.map((info) => {
              return (
                <tr>
                  <td>{info.name}</td>
                  <td>{info.score}</td>
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default App;
