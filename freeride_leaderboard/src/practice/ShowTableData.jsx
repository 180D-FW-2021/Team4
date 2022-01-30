import React from 'react'
import './Table.css'
import data from './data.json'

function ShowTableData() {
    const TableData = data.map (
        (info) => {
            return (
                <tr>
                    <td>{info.name}</td>
                    <td>{info.score}</td>
                </tr>
            )
        }
    )

    return(
        <div>
            <table class="Table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {TableData}
                </tbody>
            </table>
        </div>
    )
}

export default ShowTableData;