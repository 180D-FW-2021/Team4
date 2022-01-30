import React, { Component } from 'react';
//import ShowTableData from './practice/ShowTableData'
import './App.css';
import './practice/Table.css'

function App() {
  const [entries, setEntries] = React.useState(null);

  React.useEffect(() => {
  //   fetch("/api")
  //     .then((res) => res.json())
  //     .then((data) => setData());
  // }, []);

  fetch("/api")
      .then((res) => res.json())
      .then((data) => setEntries(data));
  }, []);

  // return (
  //   <div className="App">
  //     <p>{entries && entries.map((entries, index) => (
  //       <div key={index}>
  //         {entries.name}
  //       </div>
  //     ))}</p>
  //     <h1>Test table data</h1>
  //     <ShowTableData/>
  //   </div>
  // )

  return (
    <div className="App">
      <h1>Test table data</h1>
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
