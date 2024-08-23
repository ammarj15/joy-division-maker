import React from 'react'
import '../styles/History.scss'

function History({ history }) {

    return (
    <div className='history'>
       <h2>History: </h2>
        <div className="history-container">
        {history.length > 0 ? (
            history.map((item, index) => (
                <div key={index} className="history-item">
                    <img
                        src={`data:image/png;base64,${item.image}`}
                        alt={`Generated art ${index + 1}`}
                        style={{ width: '100px', height: '100px', margin: '10px' }}
                    />
                    {/* <p>{new Date(item.timestamp).toLocaleString()}&nbsp;</p> */}
                </div>
        ))
        ) : (
            <p>No history to display.</p>
        )}
    </div>
    </div>
    );
}

export default History;